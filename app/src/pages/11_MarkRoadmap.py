import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="Mark's Academic Roadmap", page_icon="🗺️", layout="wide")

# Page Title
st.title("Mark's Academic Roadmap")

# Fetch Data from API
with st.spinner("Loading academic roadmap..."):
    try:
        response = requests.get("http://localhost:5000/api/mark/roadmap")  # Update API URL as needed
        if response.status_code == 200:
            roadmap_data = response.json()
        else:
            st.error("Failed to fetch roadmap data. Please try again later.")
            roadmap_data = []
    except Exception as e:
        st.error(f"An error occurred: {e}")
        roadmap_data = []

# Display Roadmap
if roadmap_data:
    for semester in roadmap_data:
        st.subheader(f"Semester: {semester['semester']}")
        courses = semester.get("courses", [])
        if courses:
            st.markdown(", ".join(courses))
        else:
            st.info("No courses scheduled for this semester.")
else:
    st.info("No academic roadmap data available.")

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
