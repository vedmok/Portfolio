# Vedant Moktali — Portfolio ($VDNT)

Single-page portfolio. Static HTML + one image, no build step. Converted from
a design-canvas export to standalone files: the canvas runtime (templating,
theme toggle, expandable sections, hover styles) has been replaced with plain
CSS and vanilla JS, so the page works on any static host.

## Repo contents

| File | Purpose |
|---|---|
| `index.html` | The entire site |
| `uploads/photo-1784118397140.png` | Hero portrait (referenced by index.html) |
| `streamlit_app.py` | Wrapper to serve the site on Streamlit (Option B) |
| `requirements.txt` | Streamlit dependency (Option B only) |

## Option A — GitHub Pages (recommended)

1. Create a repo. For the cleanest URL, name it `<your-username>.github.io`.
2. Upload all files, keeping the `uploads/` folder structure. Commit to `main`.
3. **Settings → Pages → Source: Deploy from a branch → main / (root) → Save.**
4. Live in ~1 minute at `https://<your-username>.github.io/` (or `/<repo-name>/`).

Updates: edit `index.html`, commit, Pages redeploys automatically.

## Option B — Streamlit Community Cloud

Works, with tradeoffs: the app sleeps when idle (first visitor waits for
wake-up), the URL is `<app>.streamlit.app`, and the page renders inside an
iframe with a fixed height (adjust the `height=9500` in `streamlit_app.py`
if content is added and gets cut off).

1. Push this repo to GitHub.
2. At https://share.streamlit.io → **New app** → this repo, branch `main`,
   main file `streamlit_app.py` → Deploy.

## Site features (all self-contained)

- Dark/light theme toggle, persisted in localStorage
- Reading progress bar and hero parallax
- Expandable "receipts" sections per role
- Scroll-reveal animations
- Company logos loaded from favicon service; broken logos auto-hide

## Pending placeholders in index.html

- LinkedIn link (`data-placeholder="linkedin"`) — replace `href="#"` with the profile URL
- Resume link (`data-placeholder="resume"`) — add the PDF to the repo and point the link at it
