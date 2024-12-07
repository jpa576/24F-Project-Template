import streamlit as st
import pandas as pd
import requests

# Set the page configuration
st.set_page_config(page_title="Manage Courses", layout="wide")

st.title("📚 Manage Courses")
st.write("View, add, or remove courses in the system.")

COURSE_API_URL = "http://api:4000/c"

def fetch_courses():
    try:
        response = requests.get(f"{COURSE_API_URL}/all_courses")
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching courses: {e}")
        return []

# Fetch courses and display
courses = fetch_courses()
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
dept = st.text_input("Department (e.g., CS, DS):")
course_number = st.text_input("Course Number (e.g., 2500):")
course_name = st.text_input("Course Name:")
description = st.text_area("Course Description:")
credits = st.number_input("Credits:", min_value=1, max_value=5)

if st.button("Add Course"):
    try:
        response = requests.post(f"{COURSE_API_URL}/add_course", json={
            "department": dept,
            "course_number": course_number,
            "course_name": course_name,
            "description": description,
            "credits": credits
        })
        if response.status_code == 201:
            st.success("Course added successfully!")
        else:
            st.error("Failed to add course.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error adding course: {e}")

