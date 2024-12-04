import streamlit as st
import pandas as pd
import requests

# Set the page configuration
st.set_page_config(page_title="Academic Progression", layout="wide")

# Header
st.markdown("# 📚 Academic Progression")
st.write("Track your academic growth and assess your learning journey.")

# API URL for Marcus's academic progress
API_URL = "http://api:4000/user/academic_progress?user_id=1"

# Fetch academic progress data from the API
def fetch_academic_progress():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        # Ensure keys exist in response
        for key in ["current", "completed", "required"]:
            if key not in data:
                data[key] = []

        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching academic progression: {e}")
        return {"current": [], "completed": [], "required": []}

# Fetch data
academic_progress = fetch_academic_progress()

# Debugging: Display the raw API response
st.json(academic_progress)

# Display tables with error handling
st.markdown("### 📘 Courses Currently Taking")
try:
    current_courses = pd.DataFrame(academic_progress["current"], columns=["Department", "Course Number", "Course Name", "Description", "Credits"])
    st.dataframe(current_courses)
except Exception as e:
    st.warning(f"Error displaying current courses: {e}")

st.markdown("### ✅ Completed Courses")
try:
    completed_courses = pd.DataFrame(academic_progress["completed"], columns=["Department", "Course Number", "Course Name", "Description", "Credits"])
    st.dataframe(completed_courses)
except Exception as e:
    st.warning(f"Error displaying completed courses: {e}")

st.markdown("### 📌 Required Courses")
try:
    required_courses = pd.DataFrame(academic_progress["required"], columns=["Department", "Course Number", "Course Name", "Description", "Credits"])
    st.dataframe(required_courses)
except Exception as e:
    st.warning(f"Error displaying required courses: {e}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Algonauts")
