import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="High-Demand Career Courses", page_icon="💼", layout="wide")

# Page Title
st.title("Courses for High-Demand Careers")

# Fetch Data from API
with st.spinner("Loading career-oriented courses..."):
    try:
        response = requests.get("http://localhost:5000/api/mark/career_courses")  # Update API URL as needed
        if response.status_code == 200:
            career_courses = response.json()
        else:
            st.error("Failed to fetch data. Please try again later.")
            career_courses = []
    except Exception as e:
        st.error(f"An error occurred: {e}")
        career_courses = []

# Display Career-Oriented Courses
if career_courses:
    for job in career_courses:
        st.subheader(f"Job Role: {job['job_role']}")
        courses = job.get("courses", [])
        if courses:
            st.markdown(", ".join(courses))
        else:
            st.info("No courses listed for this role.")
else:
    st.info("No career-oriented course data available.")

# Sidebar Navigation
st.sidebar.title("Mark's Navigation")
selected_page = st.sidebar.radio(
    "Go to:",
    options=["Academic Status", "Academic Roadmap", "Career-Oriented Courses"]
)

# Redirect based on sidebar
if selected_page == "Academic Status":
    st.experimental_set_query_params(page="10_MarkAcademicHome")
elif selected_page == "Academic Roadmap":
    st.experimental_set_query_params(page="11_MarkRoadmap")
elif selected_page == "Career-Oriented Courses":
    st.experimental_set_query_params(page="12_MarkCareerCourses")
