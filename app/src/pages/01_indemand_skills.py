import requests
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header('In-Demand Skills')

# Access the session state to make a more customized/personalized app experience
if "first_name" in st.session_state:
    st.write(f"### Hi, {st.session_state['first_name']}.")
else:
    st.warning("Please log in to personalize your experience.")

# API URL
API_URL = "http://api:4000/ts/skills/by_demand"

# Fetch skills from the API
def fetch_skills():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad status codes
        skills = response.json()

        # Validate the response data structure
        if isinstance(skills, list) and len(skills) > 0:
            if isinstance(skills[0], dict):
                # If response is a list of dictionaries
                df = pd.DataFrame(skills)
            elif isinstance(skills[0], list):
                # If response is a list of lists, map it to a DataFrame
                df = pd.DataFrame(skills, columns=["skill_name", "complexity", "description", "popularity_score"])
            else:
                st.warning("Unexpected data format from the API.")
                return pd.DataFrame()  # Return an empty DataFrame in case of mismatch
        else:
            st.warning("No data received from the API.")
            return pd.DataFrame()

        return df
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching skills: {e}")
        return pd.DataFrame()

# Fetch skills from the API
skills_df = fetch_skills()

# Display the skills
if not skills_df.empty:
    st.write("### Top 10 In-Demand Skills")

    # Map columns manually
    column_mapping = {
        'skill_name': 'Skill Name',
        'complexity': 'Complexity',
        'description': 'Description',
        'popularity_score': 'Popularity Score'
    }
    skills_df = skills_df.rename(columns=column_mapping)

    # Ensure popularity_score is numeric and sort by it (highest first)
    if 'Popularity Score' in skills_df.columns:
        skills_df['Popularity Score'] = pd.to_numeric(skills_df['Popularity Score'], errors='coerce')  # Convert to numeric
        skills_df = skills_df.sort_values(by='Popularity Score', ascending=False)

    # Top 10 entries
    top_10_skills = skills_df.head(10).reset_index(drop=True)

    # Initialize session state index
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0

    # Navigation logic
    def next_item():
        if st.session_state.current_index < len(top_10_skills) - 1:
            st.session_state.current_index += 1

    def prev_item():
        if st.session_state.current_index > 0:
            st.session_state.current_index -= 1

    # Layout: Horizontal navigation with arrows
    col1, col2, col3 = st.columns([1, 8, 1])

    with col1:
        if st.button("⬅️", key="prev"):
            prev_item()

    with col2:
        # Current Skill Data
        current_skill = top_10_skills.iloc[st.session_state.current_index]

        # Display Rank and Skill Information
        rank = st.session_state.current_index + 1  # Rank from 1 to 10
        st.markdown(f"<h1 style='font-size: 72px; text-align: center;'>#{rank}</h1>", unsafe_allow_html=True)
        st.write(f"**{current_skill['Skill Name']}**")
        st.write(f"*{current_skill['Description']}*")
        st.write(f"⚡ **Complexity**: {current_skill['Complexity']}")
        st.write(f"🔥 **Popularity Score**: {current_skill['Popularity Score']}")

    with col3:
        if st.button("➡️", key="next"):
            next_item()

    # Show the complete DataFrame below for reference
    st.write("### All Skills Ranked by Demand")
    st.dataframe(skills_df)
else:
    st.warning("No skills available.")
