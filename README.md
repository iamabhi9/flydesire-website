# FlyDesire Website (Rebuild)

This repository contains a responsive, modernized static HTML/CSS rebuild scaffold for the archived FlyDesire site. It includes a small script to download the Wayback Machine snapshot and extract assets locally so you (or I) can populate the repo with the original images and files.

Files included:
- `index.html` — responsive static site scaffold (hero, services, portfolio, contact)
- `css/style.css` — basic responsive styles
- `js/main.js` — small UI helpers (mobile menu, smooth scroll, form stub)
- `assets/logo.svg` — placeholder logo; will be replaced by the archived logo when you run the fetch script
- `fetch_wayback.py` — script that downloads the archived snapshot HTML and assets from the Wayback Machine snapshot URL and saves them into `assets/` and `archived/`
- `.gitignore` — ignores typical Python / site artifacts

Quick start
1. Clone the repo:
   ```bash
   git clone https://github.com/iamabhi9/flydesire-website.git
   cd flydesire-website
   ```

2. Replace the Formspree form ID in `index.html` (search for `FORMSPREE_ID`) or use your preferred form backend.

3. (Optional) Fetch archived assets automatically by running the included Python script (requires Python 3.8+, requests, beautifulsoup4):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python fetch_wayback.py
   ```
   This will download the archived HTML into `archived/` and save images/CSS/JS into `assets/`. After that, open `index.html` locally to see the site with original assets.

4. Open `index.html` in your browser or deploy to GitHub Pages / Netlify / Vercel.

Notes
- The `fetch_wayback.py` script is provided to automate asset extraction from the Wayback snapshot: `https://web.archive.org/web/20211229051040/http://flydesire.com/`.
- I used a placeholder Formspree action URL in the contact form. Replace `FORMSPREE_ID` in `index.html` with your actual Formspree form id or your preferred form endpoint.

If you want, I can run the fetch script and commit the extracted assets to the repo for you — provide an authorization or allow me to run web fetches. Otherwise run the script locally and push the results.
