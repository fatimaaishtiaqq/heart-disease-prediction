from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "heart_disease_model.pkl"
FALLBACK_MODEL_PATH = BASE_DIR / "svc_trained_model.pkl"
HERO_IMG_PATH = BASE_DIR / "heart_hero.jpg"

def init_page_config():
    st.set_page_config(
        page_title="HeartHealth AI | Heart Disease Risk Predictor",
        page_icon="❤️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def switch_page(target_page: str):
    st.session_state.current_page = target_page
    st.query_params["page"] = target_page

def init_navigation_state():
    query_page = st.query_params.get("page", None)
    if query_page in ["predictor", "about", "how_it_works"]:
        st.session_state.current_page = query_page
    elif "current_page" not in st.session_state:
        st.session_state.current_page = "predictor"
