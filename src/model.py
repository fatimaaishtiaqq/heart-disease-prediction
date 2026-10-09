import base64
import pickle
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from src.config import MODEL_PATH, FALLBACK_MODEL_PATH, HERO_IMG_PATH

@st.cache_resource
def get_model():
    target_path = MODEL_PATH if MODEL_PATH.exists() else FALLBACK_MODEL_PATH
    with open(target_path, "rb") as f:
        return pickle.load(f)

@st.cache_resource
def get_label_encoders():
    encoders = {}
    encoders["ChestPainType"] = LabelEncoder().fit(["Typical Angina", "Atypical Angina", "Non-Anginal", "Asymptomatic"])
    encoders["Gender"] = LabelEncoder().fit(["Female", "Male"])
    encoders["MajorVessels"] = LabelEncoder().fit(["Zero", "One", "Two", "Three"])
    encoders["Thalassemia"] = LabelEncoder().fit(["Normal", "Fixed Defect", "Reversible Defect"])
    return encoders

@st.cache_data
def get_hero_b64():
    if HERO_IMG_PATH.exists():
        with open(HERO_IMG_PATH, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

def predict_heart_disease(cp_val: str, gender_val: str, vessels_val: str, thal_val: str):
    model = get_model()
    encoders = get_label_encoders()

    cp_enc = int(encoders["ChestPainType"].transform([cp_val])[0])
    gender_enc = int(encoders["Gender"].transform([gender_val])[0])
    vessels_enc = int(encoders["MajorVessels"].transform([vessels_val])[0])
    thal_enc = int(encoders["Thalassemia"].transform([thal_val])[0])

    encoded_df = pd.DataFrame({
        "ChestPainType": [cp_enc],
        "Gender": [gender_enc],
        "MajorVessels": [vessels_enc],
        "Thalassemia": [thal_enc]
    })

    pred = int(model.predict(encoded_df)[0])
    decision_score = float(model.decision_function(encoded_df)[0])
    risk_probability = float(1.0 / (1.0 + np.exp(-decision_score * 1.5)) * 100)

    return pred, risk_probability, encoded_df
