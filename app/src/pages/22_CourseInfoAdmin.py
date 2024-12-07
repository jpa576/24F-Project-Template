import streamlit as st
import pandas as pd
import requests

# Set the page configuration
st.set_page_config(page_title="Manage Courses", layout="wide")

st.title("📚 Manage Courses")
st.write("View, add, or remove courses in the system.")

# API endpoint to fetch, add, and remove courses
BASE_COURSE_API_URL = "http://api:4000/c"  # Base URL for course-related API endpoints

def fetch_courses():
    """Fetch all courses from the backend."""
    try:
        response = requests.get(f"{BASE_COURSE_API_URL}/all_courses")
        response.raise_for_status()
        return response.json().get("data", [])  # Assuming the response has a "data" field
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching courses: {e}")
        return []

def add_course(course_data):
    """Send a request to the backend to add a course."""
    try:
        response = requests.post(f"{BASE_COURSE_API_URL}/add_course", json=course_data)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return True, None  # Success
    except requests.exceptions.RequestException as e:
        if e.response is not None:
            return False, e.response.json().get("error", "Unknown error occurred")
        return False, str(e)

def remove_course(department, course_number):
    """Send a request to the backend to remove a course based on department and course number."""
    try:
        response = requests.delete(f"{BASE_COURSE_API_URL}/remove_course", json={
            "department": department,
            "course_number": course_number
        })
        response.raise_for_status()
        return True, None
    except requests.exceptions.RequestException as e:
        if e.response is not None:
            return False, e.response.json().get("error", "Unknown error occurred")
        return False, str(e)

# Fetch and display courses
courses = fetch_courses()

if courses:
    df_courses = pd.DataFrame(courses)
    st.markdown("### Existing Courses")
    st.dataframe(df_courses, use_container_width=True)

    # Remove a Course Section
    st.markdown("### Remove a Course")
    selected_course = st.selectbox(
        "Select a Course to Remove:",
        df_courses.apply(lambda x: f"{x['department']} {x['course_number']} - {x['course_name']}", axis=1)
    )

    if st.button("Remove Course"):
        # Extract department and course_number from the selected course
        selected_index = df_courses.apply(
            lambda x: f"{x['department']} {x['course_number']} - {x['course_name']}", axis=1
        ).tolist().index(selected_course)
        department = df_courses.iloc[selected_index]["department"]
        course_number = df_courses.iloc[selected_index]["course_number"]

        success, error_message = remove_course(department, course_number)
        if success:
            st.success("Course removed successfully!")
            st.experimental_rerun()  # Refresh the page to reflect changes
        else:
            st.error(f"Failed to remove course. Error: {error_message}")
else:
    st.info("No courses found.")

# Add a New Course Section
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
