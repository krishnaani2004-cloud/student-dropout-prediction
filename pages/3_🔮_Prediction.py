import streamlit as st
import pandas as pd
import joblib

# LOAD EXACT NOTEBOOK MODEL
deployment = joblib.load("student_dropout_deployment.pkl")

scaler = deployment["scaler"]
selector = deployment["selector"]
model = deployment["model"]
threshold = deployment["threshold"]
feature_names = deployment["feature_names"]

st.title("🔮 Student Dropout Prediction")

st.write(
    "Enter the student's details to predict the dropout risk."
)

st.divider()

# STUDENT INFORMATION
st.header("Student Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age", 15, 60, 22
    )

    family_income = st.number_input(
        "Family Income", 0, value=30000
    )

    daily_study_hours = st.number_input(
        "Daily Study Hours",
        0.0,
        24.0,
        4.0
    )

with col2:
    attendance_rate = st.number_input(
        "Attendance Rate (%)",
        0.0,
        100.0,
        75.0
    )

    assignment_delay_days = st.number_input(
        "Assignment Delay Days",
        0,
        value=2
    )

    travel_time_minutes = st.number_input(
        "Travel Time (Minutes)",
        0,
        value=30
    )

with col3:
    stress_index = st.number_input(
        "Stress Index",
        0.0,
        10.0,
        5.0
    )

    gpa = st.number_input(
        "GPA",
        0.0,
        10.0,
        7.5
    )

    semester_gpa = st.number_input(
        "Semester GPA",
        0.0,
        10.0,
        7.8
    )

cgpa = st.number_input(
    "CGPA",
    0.0,
    10.0,
    7.6
)

total_daily_commitment = st.number_input(
    "Total Daily Commitment (Minutes)",
    0,
    value=480
)

st.subheader("Personal Information")

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

internet_access = st.selectbox(
    "Internet Access",
    ["Yes", "No"]
)

part_time_job = st.selectbox(
    "Part-Time Job",
    ["Yes", "No"]
)

scholarship = st.selectbox(
    "Scholarship",
    ["Yes", "No"]
)

semester_year = st.selectbox(
    "Semester Year",
    [1, 2, 3, 4]
)

department = st.selectbox(
    "Department",
    ["BUSINESS", "CS", "ENGINEERING", "SCIENCE"]
)

parental_education = st.selectbox(
    "Parental Education",
    ["High School", "Master", "PhD"]
)

performance_category = st.selectbox(
    "Performance Category",
    ["Excellent", "Needs Improvement"]
)

st.divider()

# PREDICTION
if st.button("🔮 Predict Dropout", type="primary"):

    input_data = pd.DataFrame([{

        "Age": age,

        "Family_Income": family_income,

        "Daily_Study_Hours": daily_study_hours,

        "Attendance_Rate": attendance_rate,

        "Assignment_Delay_Days": assignment_delay_days,

        "Travel_Time_Minutes": travel_time_minutes,

        "Stress_Index": stress_index,

        "GPA": gpa,

        "Semester_GPA": semester_gpa,

        "CGPA": cgpa,

        "Total_Daily_Commitment_Mins":
            total_daily_commitment,

        "Gender_Male":
            1 if gender == "Male" else 0,

        "Internet_Access_Yes":
            1 if internet_access == "Yes" else 0,

        "Part_Time_Job_Yes":
            1 if part_time_job == "Yes" else 0,

        "Scholarship_Yes":
            1 if scholarship == "Yes" else 0,

        "Semester_Year 2":
            1 if semester_year == 2 else 0,

        "Semester_Year 3":
            1 if semester_year == 3 else 0,

        "Semester_Year 4":
            1 if semester_year == 4 else 0,

        "Department_BUSINESS":
            1 if department == "BUSINESS" else 0,

        "Department_CS":
            1 if department == "CS" else 0,

        "Department_ENGINEERING":
            1 if department == "ENGINEERING" else 0,

        "Department_SCIENCE":
            1 if department == "SCIENCE" else 0,

        "Parental_Education_High School":
            1 if parental_education == "High School" else 0,

        "Parental_Education_Master":
            1 if parental_education == "Master" else 0,

        "Parental_Education_PhD":
            1 if parental_education == "PhD" else 0,

        "Performance_Category_Excellent":
            1 if performance_category == "Excellent" else 0,

        "Performance_Category_Needs Improvement":
            1 if performance_category == "Needs Improvement"
            else 0
    }])

    # EXACT NOTEBOOK FEATURE ORDER
    input_data = input_data[feature_names]

    # SCALING
    scaled_data = scaler.transform(input_data)

    scaled_data = pd.DataFrame(
        scaled_data,
        columns=feature_names
    )

    # FEATURE SELECTION
    selected_data = selector.transform(
        scaled_data
    )

    # PROBABILITY
    dropout_probability = (
        model.predict_proba(selected_data)[0][1]
    )

    not_dropout_probability = (
        1 - dropout_probability
    )

    # EXACT NOTEBOOK THRESHOLD
    prediction = (
        1
        if dropout_probability >= threshold
        else 0
    )

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error(
            "⚠️ High Risk: Student may Drop Out"
        )

    else:

        st.success(
            "✅ Low Risk: Student is Not Predicted to Drop Out"
        )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Dropout Probability",
            f"{dropout_probability * 100:.2f}%"
        )

    with col2:

        st.metric(
            "Not Dropout Probability",
            f"{not_dropout_probability * 100:.2f}%"
        )

    with col3:

        st.metric(
            "Decision Threshold",
            f"{threshold:.2f}"
        )

    st.subheader("Prediction Probability")

    probability_data = pd.DataFrame({

        "Category": [
            "Not Dropout",
            "Dropout"
        ],

        "Probability (%)": [
            not_dropout_probability * 100,
            dropout_probability * 100
        ]
    })

    st.bar_chart(
        probability_data.set_index("Category")
    )
