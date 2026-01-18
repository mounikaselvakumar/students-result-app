import streamlit as st

st.title("📊 Smart Student Performance Analyzer")

name = st.text_input("Enter Student Name")

medium = st.selectbox("Select Language / Medium", ["English Medium", "Tamil Medium"])

num_subjects = st.selectbox("Number of Subjects", [5, 6])

subjects = []
if medium == "English Medium":
    subjects = ["Math", "Science", "English", "Computer", "Social"]
else:
    subjects = ["Tamil", "English", "Math", "Science", "Social"]

if num_subjects == 6:
    subjects.append("Optional Subject")

marks = []
for sub in subjects:
    mark = st.number_input(f"Enter marks for {sub}", min_value=0, max_value=100)
    marks.append(mark)

if st.button("Analyze Performance"):
    total = sum(marks)
    max_marks = len(subjects) * 100
    percentage = (total / max_marks) * 100
    average = total / len(subjects)

    # Pass / Fail
    if average >= 40:
        status = "PASS ✅"
    else:
        status = "FAIL ❌"

    # Grade, Feedback & Tips
    if average >= 90:
        grade = "A"
        feedback = "Outstanding performance 🌟"
        tips = "Keep challenging yourself with advanced topics."
    elif average >= 75:
        grade = "B"
        feedback = "Very good 👍"
        tips = "Be consistent to reach excellence."
    elif average >= 60:
        grade = "C"
        feedback = "Good effort 📘"
        tips = "Practice weak subjects regularly."
    elif average >= 40:
        grade = "D"
        feedback = "Needs improvement ⚠️"
        tips = "Revise basics and manage time better."
    else:
        grade = "F"
        feedback = "Poor performance ❌"
        tips = "Seek help and focus on fundamentals."

    st.subheader("📄 Result")
    st.write("**Student Name:**", name)
    st.write("**Subjects:**", subjects)
    st.write("**Total Marks:**", total, "/", max_marks)
    st.write("**Percentage:**", round(percentage, 2), "%")
    st.write("**Grade:**", grade)
    st.write("**Status:**", status)
    st.write("**Feedback:**", feedback)
    st.write("**Tips:**", tips)
