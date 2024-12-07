import requests
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks

# Initialize the sidebar navigation
SideBarLinks()

# Set the page header
st.title('🎓 Career Skills Explorer')

# Display a personalized greeting
user_name = st.session_state.get('first_name', 'Guest')
st.subheader(f"👋 Welcome, {user_name}! Explore skills associated with your dream careers.")

# API URLs
CAREERS_API_URL = "http://api:4000/careers/all_careers"
CAREER_SKILLS_API_URL = "http://api:4000/careers/career_skills"

# Fet ch all careers
@st.cache_data
def fetch_all_careers():
    try:
        response = requests.get(CAREERS_API_URL)
        response.raise_for_status()
        data = response.json().get("data", [])
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Unable to fetch careers: {e}")
        return pd.DataFrame()

# Fetch skills for a specific career
def fetch_career_skills(career_path_id):
    try:
        response = requests.get(CAREER_SKILLS_API_URL, params={"career_path_id": career_path_id})
        response.raise_for_status()
        data = response.json().get("data", [])
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Unable to fetch skills for the selected career: {e}")
        return pd.DataFrame()

# Fetch all careers
careers_df = fetch_all_careers()

if not careers_df.empty:
    # Create a dropdown to select a career
    st.markdown("### 🎯 Select a Career")
    careers_df = careers_df.rename(columns={"career_name": "Career Name", "career_path_id": "Career ID"})
    selected_career = st.selectbox(
        "Choose a Career to View Its Skills",
        options=["Select a Career"] + careers_df["Career Name"].tolist()
    )

    if selected_career != "Select a Career":
        # Get the selected career's ID
        selected_career_id = careers_df[careers_df["Career Name"] == selected_career]["Career ID"].iloc[0]

        # Fetch skills for the selected career
        career_skills_df = fetch_career_skills(selected_career_id)

        if not career_skills_df.empty:
            st.markdown(f"### 📋 Skills for {selected_career}")
            st.write(career_skills_df.style.set_table_styles(
                [
                    {"selector": "thead th", "props": [("background-color", "#4CAF50"), ("color", "white")]},
                    {"selector": "tbody tr:nth-child(even)", "props": [("background-color", "#f2f2f2")]},
                ]
            ))
        else:
            st.warning(f"No skills found for {selected_career}.")
else:
    st.warning("No careers available. Please try again later.")

# Add footer for better user experience
st.markdown("---")
st.markdown("💡 **Tip:** Select a career from the dropdown to view its required skills.")
st.caption("Powered by Career Skills API | Designed with ❤️ using Streamlit.")
