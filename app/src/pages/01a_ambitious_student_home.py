import streamlit as st

# Set up page configuration
st.set_page_config(layout="wide")

# Header Section
st.title("Welcome, Jamie Chen!")
st.subheader("Career Path: AI Development")

# Sidebar Navigation
st.sidebar.title("Navigation")
st.sidebar.button("About")
st.sidebar.button("Career Roadmap")
st.sidebar.button("Coding Practice")
st.sidebar.button("Skills")
st.sidebar.button("Interview Questions")
st.sidebar.button("Academic Progress")
st.sidebar.button("Courses")
st.sidebar.button("Logout")

# Main Content
st.write("Select an option to proceed:")

# Buttons for Skill Progression and Course Progression
col1, col2 = st.columns(2)

with col1:
    if st.button("View Skill Progression", type="primary", use_container_width=True):
        st.session_state["current_career"] = "AI Development"
        st.session_state["user"] = "Jamie Chen"
        st.session_state["page"] = "Skill Progression"
        st.session_state["authenticated"] = True
        st.experimental_set_query_params(page="skill_progression")
        st.success("Redirecting to Skill Progression...")
        st.stop()

with col2:
    if st.button("View Course Progression", type="primary", use_container_width=True):
        st.session_state["current_career"] = "AI Development"
        st.session_state["user"] = "Jamie Chen"
        st.session_state["page"] = "Course Progression"
        st.session_state["authenticated"] = True
        st.experimental_set_query_params(page="course_progression")
        st.success("Redirecting to Course Progression...")
        st.stop()
