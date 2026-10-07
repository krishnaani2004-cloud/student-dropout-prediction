
import streamlit as st

st.set_page_config(
    page_title="Home - Student Dropout Prediction",
    page_icon="🏠",
    layout="wide"
)

st.title("🎓 Student Dropout Prediction System")

st.markdown("""
## Welcome!

This application uses **Machine Learning** to predict whether
a student is at risk of dropping out.

### What this application provides

- 🔮 **Dropout Prediction**
- 📊 **Student & Dataset Dashboard**
- 📈 **Model Performance Analysis**
- 🔍 **Student Clustering**
- 👤 **Student Profile**
- ℹ️ **Project Information**

### Machine Learning Workflow

**Data Collection → Data Preprocessing → EDA → Feature Selection
→ Model Training → Hyperparameter Tuning → Prediction**

### Final Model

The application uses a **Random Forest Classifier** integrated
with a preprocessing and feature-selection pipeline.

### Model Performance

- Accuracy: **79.95%**
- Precision: **78.00%**
- Recall: **79.95%**
- F1 Score: **77.96%**
- ROC-AUC: **80.20%**
""")

st.info(
    "Use the navigation menu on the left to explore the different sections."
)
