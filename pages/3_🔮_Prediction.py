
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Dropout Prediction",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Student Dropout Prediction")
st.write("Enter the student's details to predict the dropout status.")

model = joblib.load("student_dropout_model.pkl")

st.subheader("👤 Student Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 15, 50, 20)
    family_income = st.number_input("Family Income", 0.0, 1000000.0, 30000.0)
    daily_study_hours = st.number_input("Daily Study Hours", 0.0, 24.0, 3.0)
    attendance_rate = st.number_input("Attendance Rate (%)", 0.0, 100.0, 80.0)
    assignment_delay = st.number_input("Assignment Delay Days", 0.0, 100.0, 2.0)
    travel_time = st.number_input("Travel Time (Minutes)", 0.0, 300.0, 30.0)
    stress_index = st.number_input("Stress Index", 0.0, 10.0, 5.0)
    gpa = st.number_input("GPA", 0.0, 10.0, 7.0)
    semester_gpa = st.number_input("Semester GPA", 0.0, 10.0, 7.0)

with col2:
    cgpa = st.number_input("CGPA", 0.0, 10.0, 7.0)
    commitment = st.number_input(
        "Total Daily Commitment (Minutes)",
        0.0, 1440.0, 300.0
    )

    gender = st.selectbox("Gender", ["Male", "Female"])
    internet = st.selectbox("Internet Access", ["Yes", "No"])
    part_time = st.selectbox("Part-Time Job", ["Yes", "No"])
    scholarship = st.selectbox("Scholarship", ["Yes", "No"])

    semester_year = st.selectbox(
        "Semester Year",
        [1, 2, 3, 4]
    )

with col3:
    department = st.selectbox(
        "Department",
        ["BUSINESS", "CS", "ENGINEERING", "SCIENCE"]
    )

    parental_education = st.selectbox(
        "Parental Education",
        ["High School", "Master", "PhD"]
    )

    performance = st.selectbox(
        "Performance Category",
        ["Excellent", "Needs Improvement"]
    )

st.divider()

if st.button("🔮 Predict Dropout", use_container_width=True):

    input_data = pd.DataFrame([{
        "Age": age,
        "Family_Income": family_income,
        "Daily_Study_Hours": daily_study_hours,
        "Attendance_Rate": attendance_rate,
        "Assignment_Delay_Days": assignment_delay,
        "Travel_Time_Minutes": travel_time,
        "Stress_Index": stress_index,
        "GPA": gpa,
        "Semester_GPA": semester_gpa,
        "CGPA": cgpa,
        "Total_Daily_Commitment_Mins": commitment,
        "Gender_Male": 1 if gender == "Male" else 0,
        "Internet_Access_Yes": 1 if internet == "Yes" else 0,
        "Part_Time_Job_Yes": 1 if part_time == "Yes" else 0,
        "Scholarship_Yes": 1 if scholarship == "Yes" else 0,
        "Semester_Year 2": 1 if semester_year == 2 else 0,
        "Semester_Year 3": 1 if semester_year == 3 else 0,
        "Semester_Year 4": 1 if semester_year == 4 else 0,
        "Department_BUSINESS": 1 if department == "BUSINESS" else 0,
        "Department_CS": 1 if department == "CS" else 0,
        "Department_ENGINEERING": 1 if department == "ENGINEERING" else 0,
        "Department_SCIENCE": 1 if department == "SCIENCE" else 0,
        "Parental_Education_High School":
            1 if parental_education == "High School" else 0,
        "Parental_Education_Master":
            1 if parental_education == "Master" else 0,
        "Parental_Education_PhD":
            1 if parental_education == "PhD" else 0,
        "Performance_Category_Excellent":
            1 if performance == "Excellent" else 0,
        "Performance_Category_Needs Improvement":
            1 if performance == "Needs Improvement" else 0
    }])

    input_data = input_data[model.feature_names_in_]

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    st.divider()
    st.subheader("📋 Prediction Result")

    if prediction == 1:
        st.error("⚠️ Prediction: Dropout")
    else:
        st.success("✅ Prediction: Not Dropout")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Not Dropout Probability",
            f"{probabilities[0] * 100:.1f}%"
        )

    with col2:
        st.metric(
            "Dropout Probability",
            f"{probabilities[1] * 100:.1f}%"
        )

    probability_df = pd.DataFrame({
        "Status": ["Not Dropout", "Dropout"],
        "Probability": probabilities
    })

    st.bar_chart(
        probability_df.set_index("Status")
    )
