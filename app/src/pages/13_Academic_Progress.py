import streamlit as st
import pandas as pd
import requests

# Set the page configuration
st.set_page_config(page_title="Academic Progression", layout="wide")

# Header
st.markdown("# 📚 Academic Progression")
st.write("Track your academic growth and assess your learning journey.")

# API URL for Marcus's academic progress
API_URL = "http://api:4000/u/1/academic_progress"

# Fetch academic progress data from the API
def fetch_academic_progress():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching academic progression: {e}")
        return {"current": [], "completed": [], "required": []}

# Fetch data
academic_progress = fetch_academic_progress()

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
