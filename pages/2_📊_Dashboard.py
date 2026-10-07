
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard - Student Dropout Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Dropout Dashboard")

st.markdown("### Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Students", "10,000")

with col2:
    st.metric("Not Dropout", "7,646")

with col3:
    st.metric("Dropout", "2,354")

with col4:
    st.metric("Dropout Rate", "23.54%")

st.divider()

st.subheader("🎯 Target Distribution")

target_data = pd.DataFrame({
    "Status": ["Not Dropout", "Dropout"],
    "Students": [7646, 2354]
})

st.bar_chart(
    target_data.set_index("Status")
)

st.subheader("📌 Dataset Information")

info = pd.DataFrame({
    "Item": [
        "Total Records",
        "Input Features",
        "Target Column",
        "Target Classes"
    ],
    "Value": [
        "10,000",
        "27",
        "Dropout",
        "0 = Not Dropout, 1 = Dropout"
    ]
})

st.dataframe(info, use_container_width=True)

st.info(
    "The dashboard provides an overview of the student dataset "
    "and the distribution of the dropout target variable."
)
