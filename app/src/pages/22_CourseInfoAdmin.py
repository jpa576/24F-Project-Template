import streamlit as st
import pandas as pd
import requests

# Set the page configuration
st.set_page_config(page_title="Manage Courses", layout="wide")

st.title("📚 Manage Courses")
st.write("View, add, or update courses in the system.")

# API endpoint to fetch and add courses
COURSE_API_URL = "http://api:4000/cs"  # Update with your actual endpoint

def fetch_courses():
    try:
        response = requests.get(COURSE_API_URL)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching courses: {e}")
        return []

# Fetch courses
courses = fetch_courses()

# Display courses in a table
if courses:
    df_courses = pd.DataFrame(courses)
    st.dataframe(df_courses)
else:
    st.info("No courses found.")

# Add a new course
st.markdown("### Add a New Course")
dept = st.text_input("Department (e.g., CS, DS):")
course_number = st.text_input("Course Number (e.g., 2500):")
course_name = st.text_input("Course Name:")
description = st.text_area("Course Description:")
credits = st.number_input("Credits:", min_value=1, max_value=5)

if st.button("Add Course"):
    try:
        response = requests.post(COURSE_API_URL, json={
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
