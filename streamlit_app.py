"""Streamlit wrapper for the static portfolio.

Serves index.html inside a Streamlit app. Note: GitHub Pages is the better
host for a static site (no sleep, no branding) — see README.md, Option A.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Vedant Moktali — Every side of the table",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit chrome (header, footer, padding) so the site fills the page.
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

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")

# Height is fixed because components.html renders in an iframe and cannot
# auto-size. 7000px covers the full page; adjust if you add content.
components.html(html, height=7000, scrolling=True)
