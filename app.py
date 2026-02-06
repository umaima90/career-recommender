import streamlit as st

st.title("Career Recommender 🎓")
st.write("Select your skills and interests to get a career suggestion.")

skills = st.multiselect(
    "Select your skills:",
    ["coding", "math", "design", "communication", "writing", "research", "leadership", "marketing"]
)

interests = st.multiselect(
    "Select your interests:",
    ["data", "creativity", "problem-solving", "management", "teaching", "science", "business", "social impact"]
)

if st.button("Recommend Career"):
    career = None

    # Rule-based recommendations
    if "coding" in skills and "problem-solving" in interests:
        career = "Software Engineer 💻"
    elif "math" in skills and "data" in interests:
        career = "Data Scientist 📊"
    elif "design" in skills and "creativity" in interests:
        career = "UI/UX Designer 🎨"
    elif "communication" in skills and "management" in interests:
        career = "Project Manager 📂"
    elif "writing" in skills and "creativity" in interests:
        career = "Content Creator ✍️"
    elif "research" in skills and "science" in interests:
        career = "Research Scientist 🔬"
    elif "leadership" in skills and "business" in interests:
        career = "Entrepreneur 🚀"
    elif "marketing" in skills and "social impact" in interests:
        career = "Marketing Specialist 📢"
    elif "teaching" in interests and "communication" in skills:
        career = "Educator 👩‍🏫"

    # Default recommendation if no exact match
    if not career:
        if "coding" in skills:
            career = "Software Engineer 💻"
        elif "math" in skills:
            career = "Data Analyst 📈"
        elif "design" in skills:
            career = "Graphic Designer 🎨"
        elif "communication" in skills:
            career = "Public Relations Specialist 🗣️"
        elif "research" in skills:
            career = "Academic Researcher 📚"
        elif "leadership" in skills:
            career = "Team Lead 👥"
        elif "marketing" in skills:
            career = "Digital Marketer 📢"
        elif "writing" in skills:
            career = "Journalist 📰"
        else:
            career = "Generalist Explorer 🌍"

    st.success(f"Recommended Career: {career}")

