import streamlit as st
from src.icons import ICONS
from src.model import get_hero_b64, predict_heart_disease

def render_predictor_page():
    hero_b64 = get_hero_b64()

    # Hero section
    hero_col1, hero_col2 = st.columns([1.5, 1.0], gap="large")

    with hero_col1:
        st.markdown(f"""
        <div class="model-tag-pill">
            <span class="highlight">SVC</span> Machine Learning Model
        </div>
        <div class="hero-headline-single">
            Heart Disease <span class="hero-gradient-span">Risk Predictor</span>
        </div>
        <div class="hero-desc">
            This tool uses a Support Vector Classifier (SVC) model to predict whether
            a patient is at risk of heart disease based on key clinical health indicators.
        </div>
        <div class="hero-metrics-row">
            <div class="mini-metric-card">
                <div class="mini-icon-circle">
                    {ICONS['dataset']}
                </div>
                <div>
                    <div class="mini-metric-label">Dataset</div>
                    <div class="mini-metric-val">UCI Cleveland</div>
                    <div class="mini-metric-sub">(303 records)</div>
                </div>
            </div>
            <div class="mini-metric-card">
                <div class="mini-icon-circle">
                    {ICONS['cpu_model']}
                </div>
                <div>
                    <div class="mini-metric-label">Model</div>
                    <div class="mini-metric-val">Support Vector</div>
                    <div class="mini-metric-sub">Classifier (SVC)</div>
                </div>
            </div>
            <div class="mini-metric-card">
                <div class="mini-icon-circle">
                    {ICONS['chart_accuracy']}
                </div>
                <div>
                    <div class="mini-metric-label">Test Accuracy</div>
                    <div class="mini-metric-val">88.52%</div>
                    <div class="mini-metric-sub">(held-out test set)</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with hero_col2:
        if hero_b64:
            img_tag = f'<img src="data:image/jpeg;base64,{hero_b64}" class="hero-heart-img" alt="3D Heart AI">'
        else:
            img_tag = f'<div style="width: 140px; height: 140px; display: flex; align-items: center; justify-content: center;">{ICONS["heart_pulse"]}</div>'

        st.markdown(f"""<div class="hero-right-visual">
<div class="hero-img-wrapper">
{img_tag}
</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Main dashboard panels
    main_col1, main_col2 = st.columns([1.1, 1.0], gap="large")

    # Patient health indicators input panel
    with main_col1:
        with st.container(border=True):
            st.markdown(f"""
            <div class="panel-header">
                <div class="panel-header-icon">
                    {ICONS['patient']}
                </div>
                <div>
                    <div class="panel-title">Patient Health Indicators</div>
                    <div class="panel-sub">Enter the following information to get a prediction from the model.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            input_grid_col1, input_grid_col2 = st.columns(2)

            with input_grid_col1:
                cp_val = st.selectbox(
                    "Chest Pain Type",
                    options=["Asymptomatic", "Non-Anginal", "Atypical Angina", "Typical Angina"],
                    index=0,
                    help="Typical Angina: substernal chest pressure. Atypical: non-classical pain. Non-Anginal: unrelated spasms. Asymptomatic: silent ischemia."
                )

                gender_val = st.selectbox(
                    "Gender",
                    options=["Male", "Female"],
                    index=0,
                    help="Biological sex of the patient (males present higher statistical incidence in early cohorts)."
                )

            with input_grid_col2:
                vessels_val = st.selectbox(
                    "Major Vessels Colored (Fluoroscopy)",
                    options=["Zero", "One", "Two", "Three"],
                    index=2,
                    help="Number of major coronary arteries (0 to 3) showing >50% stenosis under fluoroscopy."
                )

                thal_val = st.selectbox(
                    "Thalassemia Nuclear Scan",
                    options=["Normal", "Fixed Defect", "Reversible Defect"],
                    index=2,
                    help="Normal: uniform perfusion. Fixed: prior infarction scar. Reversible: transient exercise-induced ischemia."
                )

            predict_action = st.button("Predict Heart Disease Risk →", type="primary", use_container_width=True)

    # Prediction result panel
    with main_col2:
        with st.container(border=True):
            st.markdown(f"""
            <div class="panel-header">
                <div class="panel-header-icon" style="background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%);">
                    {ICONS['stethoscope']}
                </div>
                <div>
                    <div class="panel-title">Prediction Result</div>
                    <div class="panel-sub">Real-time machine learning inference outcome.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if predict_action:
                pred, risk_probability, encoded_df = predict_heart_disease(cp_val, gender_val, vessels_val, thal_val)

                if pred == 1:
                    st.markdown(f"""
                    <div class="active-risk-card-danger">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <div>
                                <div style="color: #fda4af; font-size: 0.85rem; font-weight: 700; text-transform:uppercase; letter-spacing:0.04em;">Diagnostic Outcome</div>
                                <h3 style="color: #ffffff; margin: 0.25rem 0 0 0; font-size: 1.45rem; font-weight: 800;">HEART DISEASE DETECTED</h3>
                            </div>
                            <div style="background: rgba(0,0,0,0.45); padding: 0.5rem 1.1rem; border-radius: 12px; border: 1px solid rgba(244, 63, 94, 0.4); text-align:right;">
                                <span style="font-size:0.75rem; color:#fca5a5; font-weight:600;">Estimated Risk</span>
                                <div style="font-size:1.4rem; font-weight:800; color:#fda4af;">{risk_probability:.1f}%</div>
                            </div>
                        </div>
                        <p style="color: #fecdd3; font-size: 0.92rem; line-height: 1.55; margin: 0.85rem 0 0 0;">
                            The Support Vector Classifier identifies significant probability of coronary artery stenosis (&gt;50% luminal occlusion). Recommend immediate clinical review.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="active-risk-card-success">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <div>
                                <div style="color: #6ee7b7; font-size: 0.85rem; font-weight: 700; text-transform:uppercase; letter-spacing:0.04em;">Diagnostic Outcome</div>
                                <h3 style="color: #ffffff; margin: 0.25rem 0 0 0; font-size: 1.45rem; font-weight: 800;">NO HEART DISEASE (HEALTHY)</h3>
                            </div>
                            <div style="background: rgba(0,0,0,0.45); padding: 0.5rem 1.1rem; border-radius: 12px; border: 1px solid rgba(16, 185, 129, 0.4); text-align:right;">
                                <span style="font-size:0.75rem; color:#a7f3d0; font-weight:600;">Estimated Risk</span>
                                <div style="font-size:1.4rem; font-weight:800; color:#6ee7b7;">{risk_probability:.1f}%</div>
                            </div>
                        </div>
                        <p style="color: #a7f3d0; font-size: 0.92rem; line-height: 1.55; margin: 0.85rem 0 0 0;">
                            The Support Vector Classifier indicates absence of significant coronary narrowing based on the 4 provided clinical biomarkers.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                with st.expander("View Encoded Feature Vector"):
                    st.dataframe(encoded_df, hide_index=True)
            else:
                st.markdown(f"""
                <div class="clean-placeholder-container">
                    <div class="placeholder-icon-circle">
                        {ICONS['stethoscope']}
                    </div>
                    <div class="placeholder-title">Your prediction will appear here</div>
                    <div class="placeholder-sub">
                        After submitting the patient indicators, the model will analyze the data and show the result.
                    </div>
                </div>
                """, unsafe_allow_html=True)
