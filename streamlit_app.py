"""Streamlit wrapper for the static portfolio.

Serves index.html inside a Streamlit app. The site references a local image
(uploads/photo-*.png) which iframes can't load from disk, so it is inlined
as base64 at render time.

Note: GitHub Pages remains the better host for a static site (no cold-start
sleep, cleaner URL, better SEO) — see README.md.
"""

import base64
import re
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Vedant Moktali — $VDNT, long position",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {min-height: 100vh;}
    </style>
    """,
    unsafe_allow_html=True,
)

root = Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")


def inline_local_images(markup: str) -> str:
    """Replace local <img src="..."> paths with base64 data URIs."""

    def repl(match: re.Match) -> str:
        src = match.group(1)
        path = root / src
        if not path.is_file():
            return match.group(0)
        data = base64.b64encode(path.read_bytes()).decode("ascii")
        suffix = path.suffix.lstrip(".").lower() or "png"
        return f'src="data:image/{suffix};base64,{data}"'

    return re.sub(r'src="((?!https?:|data:)[^"]+)"', repl, markup)


html = inline_local_images(html)

# Fixed height because components.html renders in an iframe and cannot
# auto-size. Increase if you add content and the bottom gets cut off.
components.html(html, height=9500, scrolling=True)
