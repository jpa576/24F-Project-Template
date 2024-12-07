import streamlit as st
import pandas as pd
import requests

# Set the page configuration
st.set_page_config(page_title="Manage Courses", layout="wide")

st.title("📚 Manage Courses")
st.write("View, add, or update courses in the system.")

# API endpoint to fetch and add courses
FETCH_COURSES_API_URL = "http://api:4000/c/all_courses"  # Endpoint to fetch all courses
ADD_COURSE_API_URL = "http://api:4000/c/add_course"  # Endpoint to add a new course

def fetch_courses():
    """Fetch all courses from the backend."""
    try:
        response = requests.get(FETCH_COURSES_API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching courses: {e}")
        return []

def add_course(course_data):
    """Send a request to the backend to add a course."""
    try:
        response = requests.post(ADD_COURSE_API_URL, json=course_data)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return True, None  # Success
    except requests.exceptions.RequestException as e:
        if e.response is not None:
            # Return error message from the backend response
            return False, e.response.json().get("error", "Unknown error occurred")
        # Return general error if no response is available
        return False, str(e)


# Fetch courses
courses = fetch_courses()

# Display courses in a table
st.markdown("### Current Courses")
if courses:
    df_courses = pd.DataFrame(courses)
    st.dataframe(df_courses)
else:
    st.info("No courses found.")

# Add a new course
st.markdown("### Add a New Course")
dept = st.text_input("Department (e.g., CS, DS):", key="dept_input")
course_number = st.text_input("Course Number (e.g., 2500):", key="course_number_input")
course_name = st.text_input("Course Name:", key="course_name_input")
description = st.text_area("Course Description:", key="description_input")
credits = st.number_input("Credits:", min_value=1, max_value=5, key="credits_input")
if st.button("Add Course"):
    if dept and course_number and course_name and description and credits:
        course_data = {
            "department": dept,
            "course_number": course_number,
            "course_name": course_name,
            "description": description,
            "credits": credits
        }
        success, error_message = add_course(course_data)
        if success:
            st.success("Course added successfully!")
        else:
            st.error(f"Failed to add course. Error: {error_message}")
    else:
        st.warning("Please fill in all fields before submitting.")
