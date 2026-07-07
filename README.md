# Vedant Moktali — Portfolio

Single-page portfolio site. Static HTML, no build step, no dependencies.

## Option A — GitHub Pages (recommended)

Free, fast, no server, no sleep. The site is just `index.html`.

1. Create a new GitHub repo (e.g. `portfolio`). For the cleanest URL, name it
   `<your-username>.github.io` — the site then lives at `https://<your-username>.github.io/`.
2. Upload `index.html` (and this README) to the repo root. Commit to `main`.
3. In the repo: **Settings → Pages → Source: Deploy from a branch → Branch: main / (root) → Save**.
4. Wait ~1 minute. Your site is live at
   `https://<your-username>.github.io/` (or `https://<your-username>.github.io/portfolio/` if you used a named repo).

To update the site later, just edit `index.html` and commit. Pages redeploys automatically.

Custom domain (optional): Settings → Pages → Custom domain, then add a CNAME
record at your DNS provider pointing to `<your-username>.github.io`.

## Option B — Streamlit Community Cloud

Works, but the app sleeps when idle (visitors see a wake-up delay) and the URL
carries Streamlit branding. Only use this if you specifically want it.

1. Push this repo to GitHub including `streamlit_app.py` and `requirements.txt`.
2. Go to https://share.streamlit.io, sign in with GitHub, click **New app**.
3. Pick this repo, branch `main`, main file `streamlit_app.py`. Deploy.
4. The site is served at `https://<app-name>.streamlit.app`.

## Files

| File | Purpose |
|---|---|
| `index.html` | The entire site (GitHub Pages serves this directly) |
| `streamlit_app.py` | Wrapper that serves `index.html` inside Streamlit |
| `requirements.txt` | Streamlit dependency (only needed for Option B) |

## Pending placeholders in index.html

- LinkedIn link (`data-placeholder="linkedin"`) — replace `#` with the real profile URL
- Resume link (`data-placeholder="resume"`) — add the resume PDF to the repo and point the link at it
