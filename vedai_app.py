import streamlit as st

st.title("VedAI Mathematics Intelligence")

st.write("Student Performance Analysis")

student_name = st.text_input("Enter Student Name")

if student_name:

    maths_data = {
        "Topic": ["Fractions", "Algebra", "Urdhva"],
        "Questions": [10, 10, 10],
        "Correct": [9, 6, 4]
    }

    scores = []

    for questions, correct in zip(
        maths_data["Questions"],
        maths_data["Correct"]
    ):
        score = (correct / questions) * 100
        scores.append(score)

    weakest_score = scores[0]

    for score in scores:
        if score < weakest_score:
            weakest_score = score
    st.write("### Student Performance")

    for topic, score in zip(maths_data["Topic"], scores):
        st.write(topic, ":", score, "%")

    for topic, score in zip(maths_data["Topic"], scores):
        if score == weakest_score:
            st.write("### Weak Topic:", topic)
            st.write("Score:", score)