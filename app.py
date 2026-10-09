import streamlit as st
from src.config import init_page_config, init_navigation_state
from src.styles import apply_custom_styles
from src.views.navbar import render_navbar
from src.views.predictor import render_predictor_page
from src.views.about import render_about_page
from src.views.how_it_works import render_how_it_works_page
from src.views.footer import render_footer

# Page configuration
init_page_config()

# Navigation state
init_navigation_state()

# Custom styles
apply_custom_styles()

# Top navigation bar
render_navbar()

# Page router
if st.session_state.current_page == "predictor":
    render_predictor_page()
elif st.session_state.current_page == "about":
    render_about_page()
elif st.session_state.current_page == "how_it_works":
    render_how_it_works_page()

# Footer
render_footer()
