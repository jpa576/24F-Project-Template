import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="Mark's Academic Status", page_icon="🎓", layout="wide")

# Page Title
st.title("Mark's Academic Status")

# Fetch Data from API (using similar logic to Jack's code)
try:
    response = requests.get("http://localhost:5000/api/mark/academic_status")
    if response.status_code == 200:
        academic_data = response.json()
    else:
        academic_data = {}
        st.error("Failed to fetch Mark's academic data.")
except Exception as e:
    academic_data = {}
    st.error(f"An error occurred: {e}")

# Display Academic Data
if academic_data:
    st.subheader("Personal Information")
    st.markdown(f"""
    - **Name:** {academic_data.get('name', 'N/A')}
    - **Major:** {academic_data.get('major', 'N/A')}
    - **GPA:** {academic_data.get('gpa', 'N/A')}
    - **Credits Completed:** {academic_data.get('credits_completed', 'N/A')}
    """)

    st.subheader("Current Courses")
    current_courses = academic_data.get('current_courses', [])
    if current_courses:
        st.write(current_courses)
    else:
        st.info("No current courses available.")

# Sidebar Navigation (matching Jack's logic)
st.sidebar.title("Mark's Navigation")
selected_page = st.sidebar.radio(
    "Go to:",
    options=["Academic Status", "Academic Roadmap", "Career-Oriented Courses"]
)

if selected_page == "Academic Status":
    st.experimental_set_query_params(page="10_MarkAcademicHome")
elif selected_page == "Academic Roadmap":
    st.experimental_set_query_params(page="11_MarkRoadmap")
elif selected_page == "Career-Oriented Courses":
    st.experimental_set_query_params(page="12_MarkCareerCourses")
