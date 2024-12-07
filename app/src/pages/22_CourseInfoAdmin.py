import streamlit as st
import pandas as pd
import requests

# Set the page configuration
st.set_page_config(page_title="Manage Courses", layout="wide")

st.title("📚 Manage Courses")
st.write("View, add, or remove courses in the system.")

<<<<<<< HEAD
COURSE_API_URL = "http://api:4000/c"
=======
# API endpoint to fetch and add courses
FETCH_COURSES_API_URL = "http://api:4000/c/all_courses"  # Endpoint to fetch all courses
ADD_COURSE_API_URL = "http://api:4000/c/add_course"  # Endpoint to add a new course
>>>>>>> 06a7414cc90379ec136154c20e5da88e1a7dfb9c

def fetch_courses():
    """Fetch all courses from the backend."""
    try:
<<<<<<< HEAD
        response = requests.get(f"{COURSE_API_URL}/all_courses")
=======
        response = requests.get(FETCH_COURSES_API_URL)
>>>>>>> 06a7414cc90379ec136154c20e5da88e1a7dfb9c
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching courses: {e}")
        return []

<<<<<<< HEAD
# Fetch courses and display
courses = fetch_courses()
=======
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
>>>>>>> 06a7414cc90379ec136154c20e5da88e1a7dfb9c
if courses:
    df_courses = pd.DataFrame(courses)
    st.markdown("### Existing Courses")
    st.dataframe(df_courses)

    # Remove a Course Section
    st.markdown("### Remove a Course")
    course_id_to_remove = st.selectbox("Select a Course to Remove:", df_courses["course_id"])

    if st.button("Remove Course"):
        try:
            response = requests.delete(f"{COURSE_API_URL}/remove_course/{course_id_to_remove}")
            if response.status_code == 200:
                st.success("Course removed successfully!")
            else:
                st.error("Failed to remove course.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error removing course: {e}")
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
<<<<<<< HEAD
    try:
        response = requests.post(f"{COURSE_API_URL}/add_course", json={
=======
    if dept and course_number and course_name and description and credits:
        course_data = {
>>>>>>> 06a7414cc90379ec136154c20e5da88e1a7dfb9c
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
<<<<<<< HEAD
            st.error("Failed to add course.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error adding course: {e}")

=======
            st.error(f"Failed to add course. Error: {error_message}")
    else:
        st.warning("Please fill in all fields before submitting.")
>>>>>>> 06a7414cc90379ec136154c20e5da88e1a7dfb9c
