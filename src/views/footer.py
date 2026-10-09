import streamlit as st
from src.icons import ICONS

def render_footer():
    st.markdown(f"""
<div class="site-footer">
    <div class="footer-left">
        {ICONS['academic_cap']}
        <div>
            <div class="footer-title">Academic Machine Learning Project</div>
            <div class="footer-sub">Fatima Ishtiaq (SP24-BSE-026) | BS Software Engineering | COMSATS University Islamabad, Lahore Campus</div>
        </div>
    </div>
    <div class="footer-right">
        <div>
            <div class="footer-title">Supervised By</div>
            <div class="footer-sub">Dr. Rao Muhammad Adeel Nawab</div>
        </div>
        {ICONS['academic_mentor']}
    </div>
</div>
""", unsafe_allow_html=True)
