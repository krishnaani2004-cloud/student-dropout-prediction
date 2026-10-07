
import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About the Project")

st.subheader("🎓 Student Dropout Prediction System")

st.write(
    "This project uses Machine Learning to predict whether a student "
    "is likely to drop out based on academic, personal, financial, "
    "attendance and lifestyle-related factors."
)

st.divider()

st.subheader("🎯 Project Objective")

st.write(
    "The main objective is to identify students who may be at risk "
    "of dropping out and provide an early prediction that can help "
    "educational institutions take appropriate preventive measures."
)

st.divider()

st.subheader("⚙️ Technologies Used")

tech = [
    "Python",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Streamlit",
    "Joblib",
    "Google Colab"
]

for item in tech:
    st.write("• " + item)

st.divider()

st.subheader("🤖 Machine Learning Workflow")

workflow = [
    "Data Collection",
    "Data Preprocessing",
    "Exploratory Data Analysis",
    "Feature Engineering",
    "Train-Test Split",
    "Feature Selection",
    "Model Training",
    "Hyperparameter Tuning",
    "Model Evaluation",
    "Prediction"
]

for i, step in enumerate(workflow, 1):
    st.write(f"**{i}.** {step}")

st.divider()

st.subheader("🌲 Final Machine Learning Model")

st.write(
    "The application uses a Random Forest classification model "
    "inside a machine learning pipeline."
)

st.write(
    "**Pipeline:** StandardScaler → SelectKBest → Random Forest"
)

st.divider()

st.subheader("📈 Final Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Accuracy", "79.95%")

with col2:
    st.metric("F1 Score", "77.96%")

with col3:
    st.metric("ROC-AUC", "80.20%")

st.divider()

st.success(
    "This application provides an easy-to-use interface for "
    "predicting student dropout risk using Machine Learning."
)
