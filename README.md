# ❤️ Heart Disease Prediction System (End-to-End ML Pipeline)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://heart-disease-prediction-aic354.streamlit.app/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Student:** Fatima Ishtiaq (`SP24-BSE-026`)  
> **Degree Program:** BS Software Engineering  
> **Course:** Machine Learning Fundamentals (`AIC354`), Fall 2026  
> **Institution:** COMSATS University Islamabad, Lahore Campus  
> **Instructor:** Dr. Rao Muhammad Adeel Nawab  
> **Live Demo:** [https://heart-disease-prediction-aic354.streamlit.app/](https://heart-disease-prediction-aic354.streamlit.app/)

---

## 📌 Project Overview
This project delivers an end-to-end Machine Learning binary classification system to predict the presence of **Heart Disease** from structured clinical data using the **UCI Heart Disease Dataset (Cleveland database)**.

Following the instructor's prescribed **"Half-Cooked Approach"** and pedagogical structure (derived from the Titanic Passenger Survival reference system), this project restricts input features to **exactly 4 predictive clinical attributes**, conducts full data cleaning, label encoding, model training with Support Vector Classifier (SVC) and baselines, rigorous evaluation with Bayes Error analysis, model serialization, and live deployment as an interactive Streamlit web application.

---

## 🔬 Selected 4 Features (Assignment Constraint)

Out of 14 raw attributes in the UCI dataset, exactly 4 clinically significant features were selected through correlation analysis, domain literature, and non-invasive diagnostic utility:

| Feature / Attribute | Description | Permitted Values |
| :--- | :--- | :--- |
| **`ChestPainType` (`cp`)** | Nature of chest pain / angina | `Typical Angina`, `Atypical Angina`, `Non-Anginal`, `Asymptomatic` |
| **`Gender` (`sex`)** | Biological sex of patient | `Male`, `Female` |
| **`MajorVessels` (`ca`)** | Number of major coronary vessels colored by fluoroscopy | `Zero`, `One`, `Two`, `Three` |
| **`Thalassemia` (`thal`)** | Thallium stress scintigraphy scan result | `Normal`, `Fixed Defect`, `Reversible Defect` |

### Target Variable (`HeartDisease`)
* `0` / `No`: Absence of significant coronary artery disease (<50% diameter narrowing).
* `1` / `Yes`: Presence of significant coronary artery disease (>50% diameter narrowing).

---

## 🏆 Model Performance & Bayes Error Bound Analysis

Evaluated on an independent 20% held-out test split ($N = 61$ instances):

| Metric | Score | Clinical Significance |
| :--- | :---: | :--- |
| **Accuracy** | **88.52%** | High overall diagnostic correctness |
| **Precision** | **90.32%** | Minimizes false positives / unnecessary invasive procedures |
| **Recall (Sensitivity)** | **87.50%** | Crucial: catches 87.5% of true heart disease cases |
| **F1-Score** | **88.89%** | Robust harmonic balance between Precision & Recall |
| **Theoretical Bayes Ceiling** | **85.81%** | Upper mathematical bound due to clinical label conflicts |

### Why 88.52% is Near-Optimal:
In the real UCI Cleveland dataset, **191 out of 303 patients (63.04%)** share an identical 4-feature combination with someone who has the *opposite* medical diagnosis. Because identical inputs cannot produce two different outputs simultaneously, the theoretical maximum possible accuracy on these 4 features is **85.81%**. Our model's **88.52%** test accuracy represents near-optimal generalization.

### Classifier Benchmark Comparison

| Model | Test Accuracy | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| **Support Vector Classifier (SVC - Primary)** | **88.52%** | **90.32%** | **87.50%** | **88.89%** |
| Random Forest Classifier | 88.52% | 90.32% | 87.50% | 88.89% |
| Decision Tree Classifier | 86.89% | 90.00% | 84.38% | 87.10% |
| Logistic Regression | 78.69% | 78.79% | 81.25% | 80.00% |

---

## 📂 Repository File Structure

```
Heart-Disease-Prediction-Model/
├── Heart_Disease_Prediction.ipynb   # Master end-to-end executed Jupyter Notebook
├── app.py                           # Interactive Streamlit Web Application
├── heart_disease_model.pkl          # Serialized trained Support Vector Classifier
├── svc_trained_model.pkl            # Model alias for full backward compatibility
├── sample-data.csv                  # 4-feature cleaned dataset (303 instances)
├── sample-data-encoded-output.csv   # Intermediate target-encoded dataset
├── sample-data-encoded.csv          # Intermediate fully label-encoded dataset
├── training-data-encoded.csv        # 80% training split dataset (242 instances)
├── testing-data-encoded.csv         # 20% testing split dataset (61 instances)
├── model-predictions.csv            # Test set predictions generated by model
├── requirements.txt                 # Pinned dependencies for instant cloud booting
├── runtime.txt                      # Python runtime specification (python-3.11)
├── Assignment 2...pdf               # Assignment specification document
└── README.md                        # Project documentation
```

---

## 🚀 Local Installation & Execution

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Create and activate virtual environment
```bash
# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate.bat

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Run the Jupyter Notebook
```bash
jupyter notebook Heart_Disease_Prediction.ipynb
```

### 5. Run the Streamlit Web Application locally
```bash
streamlit run app.py
```
The app will automatically open at `http://localhost:8501`.

---

## ☁️ Cloud Deployment Guide (Streamlit Community Cloud)

1. Push your project files to a public GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with GitHub.
3. Click **New app**, select your repository, set branch to `main`, and main file path to `app.py`.
4. Click **Deploy!** Your web app will be live with a free public URL within 60 seconds.
5. Paste your live deployment URL at the very top of `Heart_Disease_Prediction.ipynb`.

---

## 🎓 Academic Integrity & Plagiarism Disclaimer
This project was developed for academic evaluation under course **AIC354 (Machine Learning Fundamentals)** at **COMSATS University Islamabad, Lahore Campus**. All references, datasets, and methodologies have been properly cited.
