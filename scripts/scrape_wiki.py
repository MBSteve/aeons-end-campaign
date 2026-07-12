#!/usr/bin/env python3
"""
Aeon's End Wiki Scraper
=======================
Scrapes https://aeonsend.wiki.gg for card images, lore, and stats.
Uses the MediaWiki API with standard library only (no pip install needed).

Usage:
    python scripts/scrape_wiki.py --all
    python scripts/scrape_wiki.py --mages
    python scripts/scrape_wiki.py --mage "Adelheim"
    python scripts/scrape_wiki.py --dry-run
"""

import os, sys, json, time, re, urllib.request, urllib.error
from pathlib import Path
from html import unescape as html_unescape
from urllib.parse import unquote

WIKI_API = "https://aeonsend.wiki.gg/api.php"
WIKI_BASE = "https://aeonsend.wiki.gg"
HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "AeonsEndCampaign" / "ReferenceImages"
DELAY = 1.0
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AeonsEndCampaign/1.0"

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

MAGES = {
    "Adelheim": "Adelheim", "Brama": "Brama", "Jian": "Jian", "Kadir": "Kadir",
    "Lash": "Lash", "Mist (AE)": "Mist", "Phaedraxa": "Phaedraxa",
    "Xaxos (AE)": "Xaxos", "Dezmodia": "Dezmodia", "Garu": "Garu",
    "Gex": "Gex", "Mazahaedron": "Mazahaedron", "Mist (WE)": "Mist_(War_Eternal)",
    "Quilius": "Quilius", "Ulgimor": "Ulgimor", "Yan Magda": "Yan_Magda",
    "Nym": "Nym", "Reeve": "Reeve", "Z'hana": "Z%27hana", "Malastar": "Malastar",
    "Indira": "Indira", "Remnant": "Remnant", "Sparrow": "Sparrow",
    "Xaxos (V)": "Xaxos_(The_Void)",
}

NEMESES = {
    "Rageborne": "Rageborne", "Carapace Queen": "Carapace_Queen",
    "Crooked Mask": "Crooked_Mask", "Prince of Gluttons": "Prince_of_Gluttons",
    "Gate Witch": "Gate_Witch", "Magus of Cloaks": "Magus_of_Cloaks",
    "Hollow Crown": "Hollow_Crown", "Umbra Titan": "Umbra_Titan",
    "Horde-Crone": "Horde-Crone", "Blight Lord": "Blight_Lord",
    "Wayward One": "Wayward_One", "Thrice-Dead Prophet": "Thrice-Dead_Prophet",
    "Wraithmonger": "Wraithmonger",
    "Knight Of Shackles": "Knight_of_Shackles",
    "Maiden Of Thorns": "Maiden_of_Thorns",
}

def api(url):
    req = urllib.request.Request(url + "&format=json", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def get_html(page):
    log(f"  Fetching wiki page...")
    data = api(f"{WIKI_API}?action=parse&page={page}&prop=text")
    html = data.get("parse", {}).get("text", {}).get("*", "")
    log(f"  Got {len(html):,} bytes of HTML")
    return html

def get_file_url(name):
    data = api(f"{WIKI_API}?action=query&titles=File:{name}&prop=imageinfo&iiprop=url")
    for pid, pd in data.get("query", {}).get("pages", {}).items():
        if pid != "-1" and pd.get("imageinfo"):
            return pd["imageinfo"][0]["url"]
    return None

def dl(url, dest):
    if dest.exists():
        log(f"  SKIP {dest.name} (exists)")
        return True
    if not url.startswith("http"):
        url = WIKI_BASE + url
    # resolve thumbnail -> full
    if "/thumb/" in url:
        m = re.match(r"(.*)/thumb/(.*?)/(\d+px-.*)", url)
        if m:
            url = f"{m.group(1)}/{m.group(2)}"
    log(f"  Downloading image...")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            dest.parent.mkdir(parents=True, exist_ok=True)
            with open(dest, "wb") as f:
                f.write(r.read())
        log(f"  Saved {dest.name} ({dest.stat().st_size:,} bytes)")
        return True
    except Exception as e:
        log(f"  IMAGE FAILED: {e}")
        return False

def find_img(html):
    front = back = None
    for m in re.finditer(r'<img[^>]*src="([^"]+)"', html):
        fname = unquote(m.group(1).split("/")[-1]).lower()
        if "front" in fname and not front:
            front = m.group(1)
        if "back" in fname and not back:
            back = m.group(1)
    return front, back

def get_section(html, sid):
    p = re.compile(r'<h[2-4][^>]*><span[^>]*id="' + re.escape(sid) + r'"[^>]*>.*?</h[2-4]>(.*?)(?=<h[2-4]\b|$)', re.DOTALL)
    m = p.search(html)
    if not m:
        return ""
    t = re.sub(r'<[^>]+>', ' ', m.group(1))
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'\[?\s*edit\s*\|\s*edit source\s*\]?', '', t).strip()
    t = html_unescape(t)
    # Strip leading/trailing quotes from wiki dialogue text
    t = t.strip('"').strip("'").strip()
    return t

def get_infobox(html):
    data = {}
    m = re.search(r'<table[^>]*class="[^"]*infobox[^"]*"[^>]*>(.*?)</table>', html, re.DOTALL)
    if not m:
        return data
    for row in re.findall(r'<tr[^>]*>(.*?)</tr>', m.group(1), re.DOTALL):
        th = re.search(r'<th[^>]*>(.*?)</th>', row, re.DOTALL)
        td = re.search(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
        if th and td:
            k = re.sub(r'<[^>]+>', '', th.group(1)).strip()
            v = re.sub(r'<[^>]+>', ' ', td.group(1)).strip()
            data[k] = re.sub(r'\s+', ' ', v)
    return data

def scrape_mage(name, page):
    log(f"--- MAGE: {name} ---")
    d = OUT / "Mages" / name.replace(" ", "_")
    d.mkdir(parents=True, exist_ok=True)
    try:
        html = get_html(page)
    except Exception as e:
        log(f"ERROR: {e}")
        return None
    time.sleep(DELAY)

    infobox = get_infobox(html)
    over = get_section(html, "Overview") or get_section(html, "Mage_Overview")
    abil = get_section(html, "Ability")
    lore = get_section(html, "Lore") or get_section(html, "Story")
    strat = get_section(html, "Tips_.26_Strategy") or get_section(html, "Tips_&_Strategy") or get_section(html, "Strategy")
    trivia = get_section(html, "Trivia")
    log(f"  Lore:{'YES' if lore else 'no'} Strat:{'YES' if strat else 'no'} Trivia:{'YES' if trivia else 'no'}")

    ufront, uback = find_img(html)
    images = {}
    if ufront:
        images["front"] = "front.jpg"
        dl(ufront, d / "front.jpg")
    if uback:
        images["back"] = "back.jpg"
        dl(uback, d / "back.jpg")

    data = {
        "type": "mage", "name": name,
        "wiki": f"{WIKI_BASE}/wiki/{page}",
        "infobox": infobox, "overview": over, "ability": abil,
        "lore": lore, "strategy": strat, "trivia": trivia, "images": images,
    }
    with open(d / "data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    log(f"Saved {d / 'data.json'}")
    return data

def scrape_nemesis(name, page):
    log(f"--- NEMESIS: {name} ---")
    d = OUT / "Nemeses" / name.replace(" ", "_")
    d.mkdir(parents=True, exist_ok=True)
    try:
        html = get_html(page)
    except Exception as e:
        log(f"ERROR: {e}")
        return None
    time.sleep(DELAY)

    infobox = get_infobox(html)
    over = get_section(html, "Overview")
    setup = get_section(html, "Setup")
    unleash = get_section(html, "Unleash")
    rules = get_section(html, "Additional_Rules") or get_section(html, "Additional Rules")
    strat = get_section(html, "Tips_.26_Strategy") or get_section(html, "Tips_&_Strategy") or get_section(html, "Strategy")
    lore = get_section(html, "Lore") or get_section(html, "Story")
    log(f"  Lore:{'YES' if lore else 'no'} Setup:{'YES' if setup else 'no'} Unleash:{'YES' if unleash else 'no'} Rules:{'YES' if rules else 'no'}")

    ufront, uback = find_img(html)
    images = {}
    if ufront:
        images["front"] = "front.jpg"
        dl(ufront, d / "front.jpg")
    if uback:
        images["back"] = "back.jpg"
        dl(uback, d / "back.jpg")

    data = {
        "type": "nemesis", "name": name,
        "wiki": f"{WIKI_BASE}/wiki/{page}",
        "infobox": infobox, "overview": over, "setup": setup,
        "unleash": unleash, "additional_rules": rules,
        "strategy": strat, "lore": lore, "images": images,
    }
    with open(d / "data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    log(f"Saved {d / 'data.json'}")
    return data

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--all", action="store_true")
    p.add_argument("--mages", action="store_true")
    p.add_argument("--nemeses", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--mage", type=str)
    p.add_argument("--nemesis", type=str)
    args = p.parse_args()
    if not any([args.all, args.mages, args.nemeses, args.mage, args.nemesis]):
        p.print_help(); return

    results = {"mages": {}, "nemeses": {}}

    if args.all or args.mages or args.mage:
        items = {}
        if args.mage:
            if args.mage not in MAGES:
                log(f"Unknown mage '{args.mage}'"); return
            items = {args.mage: MAGES[args.mage]}
        else:
            items = MAGES
        log(f"Scraping {len(items)} mages...")
        for i, (n, pn) in enumerate(items.items(), 1):
            log(f"[{i}/{len(items)}] {n}")
            if args.dry_run:
                log(f"  Would fetch: {WIKI_BASE}/wiki/{pn}")
                continue
            try:
                d = scrape_mage(n, pn)
                if d: results["mages"][n] = d
            except Exception as e:
                log(f"ERROR on {n}: {e}")
                import traceback; traceback.print_exc()

    if args.all or args.nemeses or args.nemesis:
        items = {}
        if args.nemesis:
            if args.nemesis not in NEMESES:
                log(f"Unknown nemesis '{args.nemesis}'"); return
            items = {args.nemesis: NEMESES[args.nemesis]}
        else:
            items = NEMESES
        log(f"Scraping {len(items)} nemeses...")
        for i, (n, pn) in enumerate(items.items(), 1):
            log(f"[{i}/{len(items)}] {n}")
            if args.dry_run:
                log(f"  Would fetch: {WIKI_BASE}/wiki/{pn}")
                continue
            try:
                d = scrape_nemesis(n, pn)
                if d: results["nemeses"][n] = d
            except Exception as e:
                log(f"ERROR on {n}: {e}")
                import traceback; traceback.print_exc()

    if not args.dry_run:
        mc, nc = len(results["mages"]), len(results["nemeses"])
        log(f"DONE: {mc} mages, {nc} nemeses saved to {OUT}")
        with open(OUT / "index.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        log(f"Index: {OUT / 'index.json'}")

if __name__ == "__main__":
    main()