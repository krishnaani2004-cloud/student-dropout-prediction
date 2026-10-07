
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance")

st.write(
    "Performance of the final Student Dropout Prediction "
    "machine learning model."
)

st.subheader("🏆 Final Model Metrics")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Accuracy", "79.95%")

with col2:
    st.metric("Precision", "78.00%")

with col3:
    st.metric("Recall", "79.95%")

with col4:
    st.metric("F1 Score", "77.96%")

with col5:
    st.metric("ROC-AUC", "80.20%")

st.divider()

st.subheader("📊 Classification Report")

report = pd.DataFrame({
    "Class": ["Not Dropout", "Dropout"],
    "Precision": [0.83, 0.63],
    "Recall": [0.93, 0.37],
    "F1 Score": [0.88, 0.46],
    "Support": [1529, 471]
})

st.dataframe(
    report,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("📌 Model Interpretation")

st.write(
    "The model performs well in identifying students who are "
    "not likely to drop out. The dropout class is more difficult "
    "to identify, which is reflected in its lower recall."
)

st.info(
    "The final model uses a machine learning pipeline containing "
    "feature scaling, feature selection and Random Forest classification."
)

st.subheader("🎯 ROC-AUC Score")

st.progress(0.802)

st.write("ROC-AUC: **0.802**")

st.success(
    "The model achieved an overall accuracy of 79.95% "
    "and an ROC-AUC score of 80.20%."
)
