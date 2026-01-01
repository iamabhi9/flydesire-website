"""
fetch_wayback.py

Download a Wayback snapshot HTML and attempt to download referenced assets into `assets/`.

Caveats: The Wayback Machine rewrites asset URLs; this script tries to find the archived asset URLs in the HTML and download them. It is best run locally.
"""
import os
import re
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

SNAPSHOT = 'https://web.archive.org/web/20211229051040/http://flydesire.com/'
OUT_DIR = 'archived'
ASSETS_DIR = 'assets'

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

print('Fetching snapshot:', SNAPSHOT)
res = requests.get(SNAPSHOT, timeout=30)
res.raise_for_status()
html = res.text

with open(os.path.join(OUT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)

soup = BeautifulSoup(html, 'html.parser')

def abs_url(src):
    if not src: return None
    src = src.strip()
    # If Wayback rewritten (starts with /web/), make absolute Wayback URL
    if src.startswith('http'):
        return src
    if src.startswith('/web/'):
        return urljoin('https://web.archive.org', src)
    # relative to snapshot base
    return urljoin(SNAPSHOT, src)

assets = set()
for tag, attr in [('img','src'), ('script','src'), ('link','href')]:
    for t in soup.find_all(tag):
        val = t.get(attr)
        if not val: continue
        a = abs_url(val)
        if a:
            assets.add(a)

print(f'Found {len(assets)} assets — downloading to {ASSETS_DIR}/')

for a in sorted(assets):
    try:
        parsed = urlparse(a)
        name = os.path.basename(parsed.path)
        if not name:
            name = re.sub(r'[^a-zA-Z0-9]', '_', a)[:40]
        outpath = os.path.join(ASSETS_DIR, name)
        if os.path.exists(outpath):
            print('Skipping exists:', name)
            continue
        r = requests.get(a, timeout=30)
        if r.status_code == 200:
            with open(outpath, 'wb') as f:
                f.write(r.content)
            print('Saved', name)
        else:
            print('Failed', a, '->', r.status_code)
    except Exception as e:
        print('Error downloading', a, e)

print('Done. Check archived/index.html and assets/')
