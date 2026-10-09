import streamlit as st
from src.config import switch_page

def render_how_it_works_page():
    # How it works hero banner
    st.markdown(f"""
    <div class="about-hero-card">
        <div class="model-tag-pill">
            <span class="highlight">SYSTEM PIPELINE</span> End-to-End Inference Workflow
        </div>
        <div class="about-hero-title">
            How HeartHealth <span class="hero-gradient-span">AI Works</span>
        </div>
        <div class="about-hero-sub">
            A step-by-step walkthrough of how raw patient health indicators are processed, encoded,
            and evaluated by the Support Vector Classifier in real-time.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-grid-2">
        <div class="feature-deep-card">
            <div class="feature-deep-title">
                <span style="color:#38bdf8; font-weight:800;">Step 1:</span> Clinical Input Gathering
            </div>
            <div class="feature-deep-body">
                The healthcare practitioner enters four non-invasive indicators via the interactive dashboard: Chest Pain Type, Gender, Major Vessels colored, and Thalassemia scan results.
            </div>
        </div>
        <div class="feature-deep-card">
            <div class="feature-deep-title">
                <span style="color:#ec4899; font-weight:800;">Step 2:</span> Categorical Label Encoding
            </div>
            <div class="feature-deep-body">
                Input strings are transformed into a normalized 4-dimensional mathematical feature vector using pre-calibrated scikit-learn LabelEncoders to match the training data manifold.
            </div>
        </div>
        <div class="feature-deep-card">
            <div class="feature-deep-title">
                <span style="color:#a855f7; font-weight:800;">Step 3:</span> Hyperplane Decision Mapping
            </div>
            <div class="feature-deep-body">
                The Support Vector Classifier applies a Radial Basis Function (RBF) kernel to project the 4-dimensional vector into higher-dimensional space to compute the signed distance to the optimal separating hyperplane.
            </div>
        </div>
        <div class="feature-deep-card">
            <div class="feature-deep-title">
                <span style="color:#10b981; font-weight:800;">Step 4:</span> Real-Time Risk Stratification
            </div>
            <div class="feature-deep-body">
                The decision function score is mapped via logistic sigmoid calibration to produce a continuous 0–100% Risk Probability score and a binary Diagnostic Outcome (Healthy vs Detected).
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    _, col_how_btn, _ = st.columns([1, 1.4, 1])
    with col_how_btn:
        if st.button("Launch Heart Disease Risk Predictor", key="how_launch_btn", on_click=switch_page, args=("predictor",), type="primary", use_container_width=True):
            pass
