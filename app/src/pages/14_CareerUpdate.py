import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Streamlit Page Configuration
st.set_page_config(page_title="Manage Career Paths", layout="wide", initial_sidebar_state="expanded")

# Initialize sidebar links
SideBarLinks()

# Styled Header
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-family: 'Arial Black', sans-serif;
            color: #4CAF50;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-family: 'Arial', sans-serif;
            color: #333333;
            margin-top: 0;
        }
        .table-header {
            background-color: #4CAF50 !important;
            color: white !important;
        }
    </style>
    <h1 class="title">🌟 Manage Career Paths</h1>
    <p class="subtitle">Easily add or remove careers from your list.</p>
    <hr style="border: 1px solid #ddd;">
""", unsafe_allow_html=True)

# API Base URLs
USER_API_BASE_URL = "http://api:4000/u/1"
CAREERS_API_BASE_URL = "http://api:4000/careers"
MAX_CAREERS = 3  # Maximum number of careers a user can follow

# Fetch all careers
def fetch_all_careers():
    try:
        response = requests.get(f"{CAREERS_API_BASE_URL}/all_careers")
        response.raise_for_status()
        return response.json()["data"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching all careers: {e}")
        return []

# Fetch user's current careers
def fetch_user_careers():
    try:
        response = requests.get(f"{USER_API_BASE_URL}/careers")
        response.raise_for_status()
        return response.json()["data"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching user careers: {e}")
        return []

# Add a career path
def add_career_path(career_path_id, progress_percentage=0.00):
    try:
        payload = {"career_path_id": career_path_id, "progress_percentage": progress_percentage}
        response = requests.post(f"{USER_API_BASE_URL}/add_careers", json=payload)
        response.raise_for_status()
        st.success("🎉 Career path added successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error adding career path: {e}")

# Remove a career path
def delete_career_path(career_path_id):
    try:
        response = requests.delete(f"{USER_API_BASE_URL}/pop_career/{career_path_id}")
        response.raise_for_status()
        st.success("🗑️ Career path removed successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error removing career path: {e}")

# Fetch careers data
user_careers = fetch_user_careers()
all_careers = fetch_all_careers()

# Layout
st.markdown("### Careers Following")
if user_careers:
    # Display table of careers being followed
    user_careers_df = pd.DataFrame(user_careers)
    st.table(user_careers_df)
else:
    st.info("You are not following any careers yet.")

# Interactive Section: Two Columns
col1, col2 = st.columns(2)

# Left Column: Add Career
with col1:
    st.markdown("#### ➕ Add Career")
    if len(user_careers) >= MAX_CAREERS:
        st.warning(f"You can only follow a maximum of {MAX_CAREERS} careers.")
    elif all_careers:
        career_names = [career["career_name"] for career in all_careers]
        selected_career_to_add = st.selectbox("Select a career to add:", options=["Select a career"] + career_names)

        if selected_career_to_add and selected_career_to_add != "Select a career":
            career_path_id = next(
                (career["career_path_id"] for career in all_careers if career["career_name"] == selected_career_to_add),
                None
            )
            progress_percentage = st.number_input(
                "Initial Progress Percentage", min_value=0.00, max_value=100.00, step=0.01, value=0.00
            )
            if st.button("Add Career"):
                add_career_path(career_path_id, progress_percentage)
    else:
        st.warning("No careers available to add at the moment.")

# Right Column: Remove Career
with col2:
    st.markdown("#### 🗑️ Remove Career")
    if user_careers:
        career_names = [career["career_name"] for career in user_careers]
        selected_career_to_remove = st.selectbox("Select a career to remove:", options=["Select a career"] + career_names)

        if selected_career_to_remove != "Select a career":
            career_path_id = next(
                (career["career_path_id"] for career in user_careers if career["career_name"] == selected_career_to_remove),
                None
            )
            if st.button("Remove Career"):
                delete_career_path(career_path_id)
    else:
        st.info("You are not following any careers to remove.")
