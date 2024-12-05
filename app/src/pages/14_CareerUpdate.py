import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Page Configuration
st.set_page_config(page_title="Career Path Manager", layout="wide", initial_sidebar_state="expanded")

SideBarLinks()

# Header Styling and Title
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
            color: #555555;
            margin-top: 0;
        }
        .highlight {
            color: #FF5722;
        }
        .st-button {
            margin-top: 20px;
        }
    </style>
    <h1 class="title">🌟 Career Path Manager</h1>
    <p class="subtitle">Seamlessly manage your career paths with just a few clicks.</p>
    <hr style="border: 1px solid #ddd;">
""", unsafe_allow_html=True)

# API Base URLs
USER_API_BASE_URL = "http://api:4000/u/1"
CAREERS_API_BASE_URL = "http://api:4000/careers"
MAX_CAREERS = 3  # Limit for careers a user can follow

# Helper Functions
def fetch_all_careers():
    """Fetch all available careers from the API."""
    try:
        response = requests.get(f"{CAREERS_API_BASE_URL}/all_careers")
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching all careers: {e}")
        return []

def fetch_user_careers():
    """Fetch careers currently being followed by the user."""
    try:
        response = requests.get(f"{USER_API_BASE_URL}/careers")
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching user careers: {e}")
        return []

def add_career_path(career_path_id, progress_percentage=0.00):
    """Add a new career path for the user."""
    try:
        payload = {"career_path_id": career_path_id, "progress_percentage": progress_percentage}
        response = requests.post(f"{USER_API_BASE_URL}/add_careers", json=payload)
        response.raise_for_status()
        st.success("🎉 Career path added successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error adding career path: {e}")

def delete_career_path(career_path_id):
    """Remove a career path for the user."""
    try:
        response = requests.delete(f"{USER_API_BASE_URL}/pop_career/{career_path_id}")
        response.raise_for_status()
        st.success("🗑️ Career path removed successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error removing career path: {e}")

# Fetch Data
user_careers = fetch_user_careers()
all_careers = fetch_all_careers()

# Layout: Display Current Careers
st.markdown("### Careers You’re Following")
if user_careers:
    user_careers_df = pd.DataFrame(user_careers)
    st.table(user_careers_df)
else:
    st.info("You are not currently following any careers. Start by adding one below.")

# Two Columns: Add Career & Remove Career
col1, col2 = st.columns(2)

# Add Career Section
with col1:
    st.markdown("#### ➕ Add a Career Path")
    if len(user_careers) >= MAX_CAREERS:
        st.warning(f"You can only follow up to {MAX_CAREERS} careers.")
    elif all_careers:
        career_names = [career.get("career_name", "Unknown") for career in all_careers]
        selected_career_to_add = st.selectbox("Select a Career to Add:", ["Select a Career"] + career_names)

        if selected_career_to_add and selected_career_to_add != "Select a Career":
            # Get the career_path_id for the selected career
            matching_career = next((career for career in all_careers if career["career_name"] == selected_career_to_add), None)
            career_path_id = matching_career.get("career_path_id") if matching_career else None

            progress_percentage = st.number_input(
                "Initial Progress Percentage", min_value=0.00, max_value=100.00, step=0.01, value=0.00
            )
            if st.button("Add Career"):
                if career_path_id is not None:
                    add_career_path(career_path_id, progress_percentage)
                else:
                    st.error("Unable to find career ID for the selected career.")
    else:
        st.warning("No careers available to add at the moment.")

# Remove Career Section
with col2:
    st.markdown("#### 🗑️ Remove a Career Path")
    if user_careers:
        career_names = [career.get("career_name", "Unknown") for career in user_careers]
        selected_career_to_remove = st.selectbox("Select a Career to Remove:", ["Select a Career"] + career_names)

        if selected_career_to_remove != "Select a Career":
            # Get the career_path_id for the selected career
            matching_career = next((career for career in user_careers if career["career_name"] == selected_career_to_remove), None)
            career_path_id = matching_career.get("career_path_id") if matching_career else None

            if st.button("Remove Career"):
                if career_path_id is not None:
                    delete_career_path(career_path_id)
                else:
                    st.error("Unable to find career ID for the selected career.")
    else:
        st.info("You are not following any careers to remove.")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; font-size: small; color: #888;">
        Managed with ❤️ using Career Path Manager. Stay on track with your goals!
    </div>
""", unsafe_allow_html=True)
