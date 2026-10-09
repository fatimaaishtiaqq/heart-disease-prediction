import streamlit as st

def apply_custom_styles():
    st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">

<style>
    /* Global Reset & Base Typography */
    * {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        box-sizing: border-box;
    }
    
    /* Full Screen Width Expansion */
    .block-container {
        padding-top: 1.25rem !important;
        padding-bottom: 2.5rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Disable Transparent Streamlit Header Overlay */
    header[data-testid="stHeader"],
    div[data-testid="stHeader"],
    .stAppHeader,
    .st-emotion-cache-18ni7ap,
    .st-emotion-cache-zq5wmm,
    .st-emotion-cache-12fmjuu,
    .st-emotion-cache-10trblm {
        display: none !important;
        height: 0 !important;
        min-height: 0 !important;
        pointer-events: none !important;
        visibility: hidden !important;
        z-index: -1 !important;
    }
    #MainMenu, footer {
        visibility: hidden !important;
    }
    [data-testid="stHeaderActionElements"],
    a[data-testid="stHeaderAnchor"],
    .st-emotion-cache-15zrgzn,
    a.header-anchor,
    .css-15zrgzn {
        display: none !important;
        pointer-events: none !important;
    }

    /* Global Dark Cyber-Medical Background */
    .stApp {
        background: radial-gradient(circle at 10% 10%, rgba(56, 189, 248, 0.05) 0%, transparent 45%),
                    radial-gradient(circle at 90% 15%, rgba(236, 72, 153, 0.06) 0%, transparent 45%),
                    radial-gradient(circle at 50% 90%, rgba(99, 102, 241, 0.05) 0%, transparent 55%),
                    #070b14;
        color: #f1f5f9;
    }

    /* Top Navigation Bar Styling */
    .top-navbar {
        position: relative !important;
        z-index: 99999 !important;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.5rem 0 1.25rem 0;
        margin-bottom: 1.5rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        width: 100%;
    }
    
    .nav-brand-link {
        position: relative !important;
        z-index: 99999 !important;
        display: inline-flex !important;
        align-items: center !important;
        gap: 0.85rem !important;
        text-decoration: none !important;
        cursor: pointer !important;
        padding: 0.45rem 0.85rem !important;
        margin: -0.45rem -0.85rem !important;
        border-radius: 14px !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        user-select: none !important;
    }
    .nav-brand-link:hover {
        transform: translateY(-1px) !important;
        background: rgba(255, 255, 255, 0.06) !important;
    }
    .nav-brand-link:hover .nav-brand-icon {
        box-shadow: 0 0 24px rgba(236, 72, 153, 0.45) !important;
        border-color: rgba(236, 72, 153, 0.6) !important;
    }
    .nav-brand-link:active {
        transform: scale(0.98) !important;
    }
    .nav-brand-link * {
        pointer-events: none !important;
        cursor: pointer !important;
    }
    .nav-brand-icon {
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, rgba(236, 72, 153, 0.22) 0%, rgba(56, 189, 248, 0.22) 100%);
        border: 1px solid rgba(236, 72, 153, 0.35);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 18px rgba(236, 72, 153, 0.25);
        transition: all 0.2s ease;
    }
    .nav-brand-text {
        font-size: 1.4rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.025em;
        line-height: 1;
    }
    .nav-brand-accent {
        color: #38bdf8;
        font-weight: 800;
    }

    .nav-right-cluster {
        position: relative !important;
        z-index: 99999 !important;
        display: flex;
        align-items: center;
        gap: 2.25rem;
    }

    .nav-menu-links {
        position: relative !important;
        z-index: 99999 !important;
        display: flex;
        align-items: center;
        gap: 1.5rem;
    }

    .nav-text-link {
        position: relative !important;
        z-index: 99999 !important;
        color: #94a3b8 !important;
        font-size: 0.96rem;
        font-weight: 600;
        text-decoration: none !important;
        padding: 0.55rem 0.95rem !important;
        border-radius: 8px;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        user-select: none !important;
    }
    .nav-text-link * {
        pointer-events: none !important;
        cursor: pointer !important;
    }
    .nav-text-link:hover {
        color: #ffffff !important;
        background: rgba(255, 255, 255, 0.08) !important;
        transform: translateY(-1px);
    }
    .nav-text-link.active {
        color: #38bdf8 !important;
        font-weight: 700;
        background: rgba(56, 189, 248, 0.1) !important;
        box-shadow: inset 0 0 0 1px rgba(56, 189, 248, 0.3) !important;
    }

    .nav-pill-badge {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 0.4rem 1rem;
        border-radius: 9999px;
        font-size: 0.82rem;
        font-weight: 700;
        color: #38bdf8;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.12);
        white-space: nowrap;
    }
    .green-dot {
        width: 8px;
        height: 8px;
        background-color: #10b981;
        border-radius: 50%;
        box-shadow: 0 0 10px #10b981;
    }

    /* Hero Section Card */
    .hero-container {
        background: linear-gradient(135deg, rgba(13, 23, 48, 0.8) 0%, rgba(8, 14, 30, 0.95) 100%);
        border: 1px solid rgba(56, 189, 248, 0.18);
        border-radius: 24px;
        padding: 2.2rem 2.5rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 50px -15px rgba(0, 0, 0, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }
    .hero-container::before {
        content: '';
        position: absolute;
        top: -40%;
        right: 15%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(236, 72, 153, 0.15) 0%, rgba(56, 189, 248, 0.1) 40%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
    }

    /* Model Category Tag Pill */
    .model-tag-pill {
        display: inline-flex;
        align-items: center;
        background: rgba(15, 23, 42, 0.9);
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 0.35rem 0.9rem;
        border-radius: 9999px;
        font-size: 0.84rem;
        font-weight: 600;
        margin-bottom: 1.25rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }
    .model-tag-pill span.highlight {
        color: #38bdf8;
        font-weight: 800;
        margin-right: 0.4rem;
    }

    /* Main Hero Headline */
    .hero-headline-single {
        font-size: clamp(1.8rem, 2.7vw, 2.85rem);
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.03em;
        line-height: 1.15;
        margin: 0 0 0.85rem 0;
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    .hero-gradient-span {
        background: linear-gradient(90deg, #ec4899 0%, #f43f5e 40%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    .hero-desc {
        color: #94a3b8;
        font-size: 1.05rem;
        line-height: 1.6;
        max-width: 620px;
        margin-bottom: 1.75rem;
    }

    /* Hero mini metric cards */
    .hero-metrics-row {
        display: flex;
        gap: 1.1rem;
        flex-wrap: wrap;
        width: 100%;
    }
    .mini-metric-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 0.85rem 1.25rem;
        display: flex;
        align-items: center;
        gap: 0.85rem;
        backdrop-filter: blur(10px);
        flex: 1 1 180px;
        min-width: 170px;
        transition: transform 0.2s, border-color 0.2s;
    }
    .mini-metric-card:hover {
        border-color: rgba(56, 189, 248, 0.4);
        transform: translateY(-2px);
    }
    .mini-icon-circle {
        width: 40px;
        height: 40px;
        border-radius: 12px;
        background: rgba(30, 41, 59, 0.9);
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid rgba(56, 189, 248, 0.25);
    }
    .mini-metric-label {
        font-size: 0.72rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .mini-metric-val {
        font-size: 1rem;
        font-weight: 800;
        color: #f1f5f9;
    }
    .mini-metric-sub {
        font-size: 0.74rem;
        color: #94a3b8;
    }

    /* Hero visual column */
    .hero-right-visual {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
        text-align: center;
    }
    .hero-img-wrapper {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .hero-heart-img {
        max-width: 100%;
        max-height: 270px;
        object-fit: contain;
        border-radius: 20px;
        filter: drop-shadow(0 0 35px rgba(56, 189, 248, 0.3));
        animation: floatHeart 6s infinite ease-in-out;
    }
    @keyframes floatHeart {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-7px); }
    }
    
    .hero-slogan-box {
        margin-top: 1.15rem;
        text-align: center;
        width: 100%;
    }
    .slogan-title {
        font-size: clamp(1.15rem, 1.8vw, 1.45rem);
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.02em;
        line-height: 1.35;
    }
    .slogan-highlight {
        background: linear-gradient(90deg, #38bdf8 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    .slogan-sub {
        font-size: 0.76rem;
        color: #64748b;
        font-weight: 600;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        margin-top: 0.3rem;
    }

    /* Main container panels */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(135deg, rgba(13, 23, 48, 0.78) 0%, rgba(8, 14, 30, 0.94) 100%) !important;
        border: 1px solid rgba(56, 189, 248, 0.18) !important;
        border-radius: 22px !important;
        padding: 2.2rem 2.2rem 2.5rem 2.2rem !important;
        backdrop-filter: blur(16px) !important;
        box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(255, 255, 255, 0.08) !important;
        min-height: 460px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
    }
    .panel-header {
        display: flex;
        align-items: center;
        gap: 0.9rem;
        margin-bottom: 1.75rem;
    }
    .panel-header-icon {
        width: 48px;
        height: 48px;
        border-radius: 14px;
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
    }
    .panel-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: #ffffff;
        margin: 0;
        letter-spacing: -0.01em;
    }
    .panel-sub {
        font-size: 0.9rem;
        color: #94a3b8;
        margin: 0.15rem 0 0 0;
    }

    /* Selectbox dropdown styling */
    div[data-baseweb="select"] {
        background-color: rgba(15, 23, 42, 0.85) !important;
        border: 1px solid rgba(56, 189, 248, 0.18) !important;
        border-radius: 14px !important;
        color: #f1f5f9 !important;
        transition: all 0.2s !important;
    }
    div[data-baseweb="select"]:hover {
        border-color: rgba(56, 189, 248, 0.45) !important;
        box-shadow: 0 0 14px rgba(56, 189, 248, 0.2) !important;
    }
    div[data-baseweb="popover"] {
        background-color: #0b1329 !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
        border-radius: 14px !important;
    }
    label[data-testid="stWidgetLabel"] {
        font-weight: 600 !important;
        font-size: 0.94rem !important;
        color: #e2e8f0 !important;
        margin-bottom: 0.4rem !important;
    }

    /* Action buttons */
    div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ec4899 0%, #a855f7 50%, #3b82f6 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding: 0.75rem 1.85rem !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        box-shadow: 0 6px 25px rgba(236, 72, 153, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.35) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: auto !important;
        max-width: fit-content !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0.5rem auto !important;
        cursor: pointer !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 35px rgba(236, 72, 153, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.45) !important;
        filter: brightness(1.1) !important;
    }
    
    div[data-testid="stVerticalBlockBorderWrapper"] .stButton>button {
        width: 100% !important;
        max-width: 100% !important;
        padding: 0.9rem 2rem !important;
        font-size: 1.05rem !important;
        font-weight: 800 !important;
        margin-top: 1.25rem !important;
    }

    /* Placeholder state */
    .clean-placeholder-container {
        padding: 3.5rem 1.5rem 2rem 1.5rem;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        flex-grow: 1;
        width: 100%;
    }
    .placeholder-icon-circle {
        width: 72px;
        height: 72px;
        border-radius: 50%;
        background: rgba(56, 189, 248, 0.1);
        border: 1px solid rgba(56, 189, 248, 0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.15);
    }
    .placeholder-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    .placeholder-sub {
        font-size: 0.94rem;
        color: #94a3b8;
        max-width: 360px;
        line-height: 1.6;
        margin: 0 auto;
    }

    /* Active risk states */
    .active-risk-card-danger {
        background: radial-gradient(circle at 10% 10%, rgba(244, 63, 94, 0.22) 0%, transparent 60%),
                    linear-gradient(135deg, rgba(35, 10, 24, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 2px solid #f43f5e;
        border-radius: 18px;
        padding: 1.85rem;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 0 40px rgba(244, 63, 94, 0.3);
        animation: fadeIn 0.4s ease-in-out;
    }
    .active-risk-card-success {
        background: radial-gradient(circle at 10% 10%, rgba(16, 185, 129, 0.22) 0%, transparent 60%),
                    linear-gradient(135deg, rgba(6, 35, 25, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 2px solid #10b981;
        border-radius: 18px;
        padding: 1.85rem;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 0 40px rgba(16, 185, 129, 0.3);
        animation: fadeIn 0.4s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* About and How It Works page styles */
    .about-hero-card {
        background: linear-gradient(135deg, rgba(13, 23, 48, 0.85) 0%, rgba(8, 14, 30, 0.98) 100%);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 24px;
        padding: 2.5rem 3rem;
        margin-bottom: 2rem;
        box-shadow: 0 20px 50px -15px rgba(0, 0, 0, 0.7);
        position: relative;
        overflow: hidden;
    }
    .about-hero-title {
        font-size: clamp(2rem, 3.2vw, 3rem);
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.03em;
        line-height: 1.15;
        margin: 0.5rem 0 0.85rem 0;
    }
    .about-hero-sub {
        color: #94a3b8;
        font-size: 1.1rem;
        line-height: 1.65;
        max-width: 850px;
    }
    
    .section-heading-row {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin: 2.5rem 0 1.25rem 0;
    }
    .section-heading-title {
        font-size: 1.55rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.02em;
        margin: 0;
    }

    .info-grid-2 {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
        margin-bottom: 2rem;
    }
    .info-grid-4 {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.25rem;
        margin-bottom: 2rem;
    }
    
    .feature-deep-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.8) 0%, rgba(10, 18, 36, 0.95) 100%);
        border: 1px solid rgba(56, 189, 248, 0.15);
        border-radius: 18px;
        padding: 1.75rem;
        transition: transform 0.2s, border-color 0.2s;
    }
    .feature-deep-card:hover {
        border-color: rgba(56, 189, 248, 0.4);
        transform: translateY(-3px);
    }
    .feature-deep-title {
        font-size: 1.15rem;
        font-weight: 800;
        color: #f1f5f9;
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .feature-deep-tag {
        display: inline-block;
        background: rgba(56, 189, 248, 0.12);
        color: #38bdf8;
        font-size: 0.76rem;
        font-weight: 700;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        margin-bottom: 0.75rem;
    }
    .feature-deep-body {
        font-size: 0.92rem;
        color: #94a3b8;
        line-height: 1.6;
    }

    .benchmark-table-card {
        background: linear-gradient(135deg, rgba(13, 23, 48, 0.8) 0%, rgba(8, 14, 30, 0.95) 100%);
        border: 1px solid rgba(56, 189, 248, 0.16);
        border-radius: 20px;
        padding: 1.75rem 2rem;
        margin-bottom: 2rem;
    }

    .disclaimer-card {
        background: linear-gradient(135deg, rgba(30, 25, 15, 0.6) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(245, 158, 11, 0.3);
        border-radius: 18px;
        padding: 1.75rem 2rem;
        margin-top: 2rem;
        margin-bottom: 2.5rem;
    }

    /* Footer Bar */
    .site-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.75rem 0 0.5rem 0;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        margin-top: 2.5rem;
        width: 100%;
    }
    .footer-left {
        display: flex;
        align-items: center;
        gap: 0.9rem;
    }
    .footer-right {
        display: flex;
        align-items: center;
        gap: 0.9rem;
        text-align: right;
    }
    .footer-title {
        font-size: 0.92rem;
        font-weight: 700;
        color: #e2e8f0;
    }
    .footer-sub {
        font-size: 0.8rem;
        color: #64748b;
        margin-top: 0.1rem;
    }

    /* Responsive design breakpoints */
    @media (max-width: 1200px) {
        .block-container {
            padding-left: 1.75rem !important;
            padding-right: 1.75rem !important;
        }
        .info-grid-4 {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    @media (max-width: 992px) {
        .info-grid-2, .info-grid-4 {
            grid-template-columns: 1fr;
        }
        .hero-metrics-row {
            flex-direction: column;
        }
        .site-footer {
            flex-direction: column;
            align-items: flex-start;
            gap: 1.25rem;
        }
        .footer-right {
            text-align: left;
        }
    }
    @media (max-width: 768px) {
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
        .top-navbar {
            flex-direction: column;
            align-items: flex-start;
            gap: 1rem;
        }
        .nav-right-cluster {
            width: 100%;
            justify-content: space-between;
            gap: 0.75rem;
        }
        .nav-menu-links {
            gap: 0.75rem;
        }
        .about-hero-card {
            padding: 1.75rem 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)
