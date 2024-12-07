import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

# Set the page configuration
st.set_page_config(page_title="Academic Progress Dashboard", layout="wide")
st.session_state["current_page"] = "Academic Progress Dashboard"  # Or "Career Progress Dashboard", etc.

# Initialize sidebar navigation
SideBarLinks()

# Header
st.markdown("# 📚 Academic Progression")
st.write("Track your academic growth and assess your learning journey.")

# API URLs
ACADEMIC_API_URL = "http://api:4000/u/1/academic_progress"  # API for academic progress
USER_INFO_API_URL = "http://api:4000/u/1/info"             # API for user info
USER_CAREERS_API_URL = "http://api:4000/u/1/careers"       # API for user careers

# Fetch academic progress data from the API
def fetch_academic_progress():
    try:
        response = requests.get(ACADEMIC_API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching academic progression: {e}")
        return {"current": [], "completed": [], "required": []}

# Fetch user information
def fetch_user_info():
    try:
        response = requests.get(USER_INFO_API_URL)
        response.raise_for_status()
        return response.json().get("data", {"name": "User"})
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching user info: {e}")
        return {"name": "User"}

# Fetch user careers
def fetch_user_careers():
    try:
        response = requests.get(USER_CAREERS_API_URL)
        response.raise_for_status()
        return [career["career_name"] for career in response.json().get("data", [])]
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching user careers: {e}")
        return []

# Fetch data
academic_progress = fetch_academic_progress()
user_info = fetch_user_info()
user_careers = fetch_user_careers()

# Generate dynamic header for required courses
user_name = user_info.get("name", "User")
if user_careers:
    career_paths_text = ", ".join(user_careers)
    st.markdown(
        f"### Hello {user_name}, here are your required courses based on your career paths: **{career_paths_text}**"
    )
else:
    st.markdown(
        f"### Hello {user_name}, here are your required courses for your academic journey:"
    )

# Styled table display function
def display_table(title, data, color):
    """
    Displays a styled table with a given title, data, and color scheme.
    """
    st.markdown(f"## {title}")
    if data:
        df = pd.DataFrame(data)
        st.dataframe(
            df.style.set_table_styles(
                [
                    {"selector": "thead th", "props": [("background-color", color), ("color", "white")]},
                    {"selector": "tbody tr:nth-child(even)", "props": [("background-color", "#f9f9f9")]},
                ]
            )
        )
    else:
        st.warning(f"No data available for {title.lower()}.")

# Display sections
display_table("📘 Courses Currently Taking", academic_progress.get("current", []), "#3498db")
display_table("✅ Completed Courses", academic_progress.get("completed", []), "#2ecc71")
display_table("📌 Required Courses", academic_progress.get("required", []), "#e74c3c")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Algonauts")
