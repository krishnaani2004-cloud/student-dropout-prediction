
import streamlit as st

st.set_page_config(
    page_title="Student Profile",
    page_icon="👤",
    layout="wide"
)

st.title("👤 Student Profile")

st.write(
    "This page provides an overview of the student attributes "
    "used by the dropout prediction system."
)

st.subheader("📚 Academic Information")

col1, col2 = st.columns(2)

with col1:
    st.info("🎓 GPA, Semester GPA and CGPA are used to assess academic performance.")
    st.info("📅 Semester Year indicates the student's current academic year.")
    st.info("📊 Performance Category represents the student's overall performance.")

with col2:
    st.info("📌 Attendance Rate represents regularity in attending classes.")
    st.info("📝 Assignment Delay Days represents delays in submitting assignments.")
    st.info("⏱️ Daily Study Hours represents the student's study time.")

st.divider()

st.subheader("🏠 Personal & Lifestyle Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Age**")
    st.write("Student age")

    st.write("**Family Income**")
    st.write("Family financial background")

with col2:
    st.write("**Travel Time**")
    st.write("Daily travel time")

    st.write("**Stress Index**")
    st.write("Student stress level")

with col3:
    st.write("**Part-Time Job**")
    st.write("Whether the student has a part-time job")

    st.write("**Scholarship**")
    st.write("Whether the student receives a scholarship")

st.divider()

st.subheader("💻 Other Factors")

factor_data = {
    "Feature": [
        "Gender",
        "Internet Access",
        "Department",
        "Parental Education",
        "Total Daily Commitment"
    ],
    "Description": [
        "Student gender",
        "Availability of internet access",
        "Student's academic department",
        "Parent's education level",
        "Total time committed to daily activities"
    ]
}

st.table(factor_data)

st.success(
    "These student attributes are processed by the machine learning "
    "model to predict whether the student is likely to drop out."
)
