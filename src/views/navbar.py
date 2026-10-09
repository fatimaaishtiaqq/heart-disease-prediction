import streamlit as st
from src.icons import ICONS

def render_navbar():
    active_page = st.session_state.current_page
    about_active_cls = "active" if active_page == "about" else ""
    how_active_cls = "active" if active_page == "how_it_works" else ""

    st.markdown(f"""<div class="top-navbar">
<a href="?page=predictor" target="_self" class="nav-brand-link">
<div class="nav-brand-icon">{ICONS['heart_pulse']}</div>
<div class="nav-brand-text">HeartHealth <span class="nav-brand-accent">AI</span></div>
</a>
<div class="nav-right-cluster">
<nav class="nav-menu-links">
<a href="?page=about" target="_self" class="nav-text-link {about_active_cls}">About Model</a>
<a href="?page=how_it_works" target="_self" class="nav-text-link {how_active_cls}">How It Works</a>
</nav>
<div class="nav-pill-badge">
<div class="green-dot"></div>
<span>ML Project</span>
</div>
</div>
</div>""", unsafe_allow_html=True)
