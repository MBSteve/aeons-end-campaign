"""Debug Brama headings"""
import urllib.request, json, re

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AeonsEndCampaign/1.0"
WIKI_API = "https://aeonsend.wiki.gg/api.php"

req = urllib.request.Request(
    f"{WIKI_API}?action=parse&page=Brama&prop=text&format=json",
    headers={"User-Agent": UA}
)
with urllib.request.urlopen(req, timeout=10) as r:
    data = json.loads(r.read())

html = data["parse"]["text"]["*"]

# Find ALL heading-like patterns
for pattern_name, pattern in [
    ("span[id=...]", r'<h[2-4][^>]*><span[^>]*id="([^"]+)"'),
    ("mw-headline", r'class="mw-headline"[^>]*id="([^"]+)"'),
    ("anchor", r'<a[^>]*name="([^"]*lore[^"]*)"'),
]:
    matches = re.findall(pattern, html, re.IGNORECASE)
    if matches:
        print(f"{pattern_name} matches: {matches}")

# Dump all <h2> sections
sections = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
print(f"\nTotal <h2> sections found: {len(sections)}")
for s in sections:
    text = re.sub(r'<[^>]+>', '', s).strip()
    ids = re.findall(r'id="([^"]+)"', s)
    print(f"  <h2> id={ids} text='{text}'")