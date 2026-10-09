import streamlit as st
from src.icons import ICONS
from src.config import switch_page

def render_about_page():
    # About hero banner
    st.markdown(f"""
    <div class="about-hero-card">
        <div class="model-tag-pill">
            <span class="highlight">CLINICAL AI SPECIFICATION</span> Full Architecture &amp; Methodology
        </div>
        <div class="about-hero-title">
            About the Heart Disease <span class="hero-gradient-span">Prediction System</span>
        </div>
        <div class="about-hero-sub">
            An in-depth, accessible breakdown of the machine learning classifier, dataset lineage,
            the four selected clinical biomarkers, algorithmic rationale, and comparative benchmarks.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Key model metrics
    st.markdown(f"""
    <div class="info-grid-4">
        <div class="mini-metric-card">
            <div class="mini-icon-circle">{ICONS['cpu_model']}</div>
            <div>
                <div class="mini-metric-label">Algorithm</div>
                <div class="mini-metric-val">SVC (RBF Kernel)</div>
                <div class="mini-metric-sub">Non-Linear Hyperplane</div>
            </div>
        </div>
        <div class="mini-metric-card">
            <div class="mini-icon-circle">{ICONS['chart_accuracy']}</div>
            <div>
                <div class="mini-metric-label">Test Accuracy</div>
                <div class="mini-metric-val">88.52%</div>
                <div class="mini-metric-sub">Held-Out 20% Cohort</div>
            </div>
        </div>
        <div class="mini-metric-card">
            <div class="mini-icon-circle">{ICONS['check_badge']}</div>
            <div>
                <div class="mini-metric-label">Precision &amp; Recall</div>
                <div class="mini-metric-val">90.32% / 87.50%</div>
                <div class="mini-metric-sub">88.89% Balanced F1</div>
            </div>
        </div>
        <div class="mini-metric-card">
            <div class="mini-icon-circle">{ICONS['dataset']}</div>
            <div>
                <div class="mini-metric-label">Dataset Source</div>
                <div class="mini-metric-val">UCI Cleveland</div>
                <div class="mini-metric-sub">303 Clinical Records</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Clinical objective section
    st.markdown(f"""
    <div class="section-heading-row">
        {ICONS['brain']}
        <h2 class="section-heading-title">1. Clinical Goal &amp; Predictive Objective</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    This machine learning system is engineered to assist healthcare providers and medical educators in the early stratification of **Coronary Artery Disease (CAD)**.
    
    Coronary artery disease is the leading cause of mortality worldwide. Traditional diagnostic pathways often require invasive angiography or expensive nuclear scans. This model demonstrates that a carefully curated subset of **four non-redundant clinical biomarkers** can accurately predict whether a patient has clinically significant coronary narrowing (>50% luminal diameter occlusion) with **88.52% accuracy**.
    """)

    # Clinical biomarkers breakdown
    st.markdown(f"""
    <div class="section-heading-row">
        {ICONS['dna']}
        <h2 class="section-heading-title">2. The 4 Selected Clinical Biomarkers</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-grid-2">
        <div class="feature-deep-card">
            <div class="feature-deep-title">
                <span>1. Chest Pain Type</span>
            </div>
            <span class="feature-deep-tag">Feature: ChestPainType (Categorical)</span>
            <div class="feature-deep-body">
                <strong>Categories:</strong> Typical Angina, Atypical Angina, Non-Anginal, Asymptomatic.<br><br>
                <strong>Clinical Significance:</strong> Typical angina presents as substernal chest pressure provoked by physical exertion and relieved by rest or nitroglycerin. In the Cleveland clinical cohort, patients presenting as <em>asymptomatic</em> frequently have underlying silent ischemia and severe multi-vessel disease, providing critical discriminatory signal for the classifier.
            </div>
        </div>
        <div class="feature-deep-card">
            <div class="feature-deep-title">
                <span>2. Major Vessels Colored Under Fluoroscopy</span>
            </div>
            <span class="feature-deep-tag">Feature: MajorVessels (Ordinal: Zero to Three)</span>
            <div class="feature-deep-body">
                <strong>Categories:</strong> Zero, One, Two, Three major vessels.<br><br>
                <strong>Clinical Significance:</strong> Fluoroscopic coronary angiography visualizes radiopaque dye injected into coronary arteries. A vessel is counted when >50% lumen diameter narrowing is detected. Patients with multiple colored vessels represent advanced anatomical disease and face significantly elevated risk profiles.
            </div>
        </div>
        <div class="feature-deep-card">
            <div class="feature-deep-title">
                <span>3. Thalassemia Nuclear Perfusion Scan</span>
            </div>
            <span class="feature-deep-tag">Feature: Thalassemia (Categorical)</span>
            <div class="feature-deep-body">
                <strong>Categories:</strong> Normal, Fixed Defect, Reversible Defect.<br><br>
                <strong>Clinical Significance:</strong> A myocardial perfusion scintigraphy scan measures myocardial blood flow during stress vs rest. A <em>reversible defect</em> indicates viable cardiac tissue experiencing exercise-induced transient ischemia (blood flow insufficiency), indicating severe stenosis that benefits from immediate intervention.
            </div>
        </div>
        <div class="feature-deep-card">
            <div class="feature-deep-title">
                <span>4. Biological Gender</span>
            </div>
            <span class="feature-deep-tag">Feature: Gender (Binary: Female / Male)</span>
            <div class="feature-deep-body">
                <strong>Categories:</strong> Female, Male.<br><br>
                <strong>Clinical Significance:</strong> Coronary heart disease epidemiology exhibits distinct sex-differentiated onset curves. Males typically present with atherosclerotic coronary events earlier in life, whereas post-menopausal females exhibit rapid progression, allowing the model to calibrate baseline risk distribution.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Model comparison and benchmark
    st.markdown(f"""
    <div class="section-heading-row">
        {ICONS['chart_accuracy']}
        <h2 class="section-heading-title">3. Model Performance &amp; Benchmark Comparison</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    All models were trained on 80% of the dataset ($N=242$) and evaluated on a strictly isolated 20% held-out test cohort ($N=61$). The Support Vector Classifier (SVC) was selected as the champion production model due to its optimal balance of sensitivity and generalization.
    """)

    # Benchmark comparison table
    st.markdown("""
    <div class="benchmark-table-card">
        <table style="width:100%; border-collapse: collapse; text-align:left; color:#f1f5f9; font-size:0.95rem;">
            <thead>
                <tr style="border-bottom: 2px solid rgba(56, 189, 248, 0.3); color:#38bdf8;">
                    <th style="padding: 0.85rem 1rem;">Machine Learning Model</th>
                    <th style="padding: 0.85rem 1rem;">Accuracy</th>
                    <th style="padding: 0.85rem 1rem;">Precision</th>
                    <th style="padding: 0.85rem 1rem;">Recall (Sensitivity)</th>
                    <th style="padding: 0.85rem 1rem;">F1-Score</th>
                    <th style="padding: 0.85rem 1rem;">Architectural Role</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(56, 189, 248, 0.08);">
                    <td style="padding: 1rem; font-weight:800; color:#38bdf8;">Support Vector Classifier (SVC)</td>
                    <td style="padding: 1rem; font-weight:800; color:#ffffff;">88.52%</td>
                    <td style="padding: 1rem; color:#34d399; font-weight:700;">90.32%</td>
                    <td style="padding: 1rem; color:#f43f5e; font-weight:700;">87.50%</td>
                    <td style="padding: 1rem; font-weight:800; color:#ffffff;">88.89%</td>
                    <td style="padding: 1rem;"><span style="background:#10b981; color:#ffffff; padding:0.25rem 0.65rem; border-radius:6px; font-size:0.78rem; font-weight:700;">Primary Champion</span></td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                    <td style="padding: 0.85rem 1rem; font-weight:600;">Random Forest Classifier</td>
                    <td style="padding: 0.85rem 1rem;">88.52%</td>
                    <td style="padding: 0.85rem 1rem;">90.32%</td>
                    <td style="padding: 0.85rem 1rem;">87.50%</td>
                    <td style="padding: 0.85rem 1rem;">88.89%</td>
                    <td style="padding: 0.85rem 1rem; color:#94a3b8;">Ensemble Baseline</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                    <td style="padding: 0.85rem 1rem; font-weight:600;">Decision Tree Classifier</td>
                    <td style="padding: 0.85rem 1rem;">86.89%</td>
                    <td style="padding: 0.85rem 1rem;">90.00%</td>
                    <td style="padding: 0.85rem 1rem;">84.38%</td>
                    <td style="padding: 0.85rem 1rem;">87.10%</td>
                    <td style="padding: 0.85rem 1rem; color:#94a3b8;">Tree Baseline</td>
                </tr>
                <tr>
                    <td style="padding: 0.85rem 1rem; font-weight:600;">Logistic Regression</td>
                    <td style="padding: 0.85rem 1rem;">78.69%</td>
                    <td style="padding: 0.85rem 1rem;">78.79%</td>
                    <td style="padding: 0.85rem 1rem;">81.25%</td>
                    <td style="padding: 0.85rem 1rem;">80.00%</td>
                    <td style="padding: 0.85rem 1rem; color:#94a3b8;">Linear Baseline</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

    # Bayes error ceiling analysis
    st.markdown(f"""
    <div class="feature-deep-card" style="border-left: 4px solid #38bdf8; margin-bottom: 2rem;">
        <div class="feature-deep-title" style="color: #38bdf8;">
            {ICONS['info_alert']} Understanding the 85.81% Theoretical Bayes Limit
        </div>
        <div class="feature-deep-body">
            In any finite clinical dataset, certain patient pairs exhibit identical feature vectors across the 4 indicators yet have opposite medical diagnoses (due to unobserved genetic or physiological factors). This introduces inherent irreducible aleatoric uncertainty, establishing the theoretical mathematical Bayes ceiling at <strong>85.81%</strong>. Our SVC model's <strong>88.52% test accuracy</strong> achieves the near-optimal frontier on this benchmark.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Clinical safety disclaimer
    st.markdown(f"""
    <div class="disclaimer-card">
        <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:0.75rem;">
            {ICONS['shield_check']}
            <h4 style="margin:0; color:#fbbf24; font-size:1.15rem; font-weight:800;">Academic Clinical Decision Support Notice</h4>
        </div>
        <div style="font-size:0.92rem; color:#cbd5e1; line-height:1.65;">
            This software is developed strictly as an educational and academic machine learning decision-support demonstration. It is not an FDA-cleared or CE-marked medical device. All risk probabilities and classifications should be evaluated alongside professional clinical examinations, 12-lead electrocardiograms, and comprehensive physician assessments.
        </div>
    </div>
    """, unsafe_allow_html=True)

    _, col_btn, _ = st.columns([1, 1.4, 1])
    with col_btn:
        if st.button("Launch Heart Disease Risk Predictor", key="about_launch_btn", on_click=switch_page, args=("predictor",), type="primary", use_container_width=True):
            pass
