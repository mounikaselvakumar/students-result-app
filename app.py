import streamlit as st

st.title("🎓 Student Result & Feedback App")

name = st.text_input("Student Name")

language = st.selectbox(
    "Select Medium",
    ["English", "Tamil", "Telugu", "Hindi"]
)

st.subheader("Enter Marks (out of 100)")

marks = []
for i in range(1, 6):
    marks.append(st.number_input(f"Subject {i}", 0, 100))

if st.button("Calculate Result"):
    total = sum(marks)
    percentage = total / 5

    if min(marks) >= 40:
        result = "PASS ✅"
        feedback = "Well done! Keep learning and improving 👍"
        tips = "Revise daily and practice more problems."
    else:
        result = "FAIL ❌"
        feedback = "Don’t give up. Improvement is possible 💪"
        tips = "Focus on weak subjects and ask doubts."

    st.success(f"Name: {name}")
    st.info(f"Medium: {language}")
    st.write(f"Total Marks: {total}")
    st.write(f"Percentage: {percentage}%")
    st.write(f"Result: {result}")
    st.write(f"Feedback: {feedback}")
    st.write(f"Tips: {tips}")