import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

# Set the page configuration
st.set_page_config(page_title="Manage Skills", layout="wide")
SideBarLinks()

st.title("💼 Manage Skills")
st.write("View, add, or update skills and career paths in the system.")

# API endpoints to fetch and add skills/careers
SKILLS_API_URL = "http://api:4000/ts"
CAREERS_API_URL = "http://api:4000/careers"

# Fetch skills
def fetch_skills():
    try:
        response = requests.get(f"{SKILLS_API_URL}/all_skills")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching skills: {e}")
        return []



# Add a new skill
def add_skill(skill_data):
    try:
        response = requests.post(f"{SKILLS_API_URL}/add_skill", json=skill_data)
        if response.status_code == 201:
            return True, None
        return False, response.json().get("error", response.text)
    except requests.exceptions.RequestException as e:
        return False, str(e)



# Display Skills
st.markdown("### Skills")
skills = fetch_skills()
if skills:
    df_skills = pd.DataFrame(skills, columns=["ID", "Skill Name", "Complexity", "Category", "Popularity Score", "Description"])
    st.dataframe(df_skills, use_container_width=True)
else:
    st.info("No skills found.")

# Form to Add a New Skill
st.markdown("### Add a New Skill")
with st.form("Add Skill"):
    skill_name = st.text_input("Skill Name:")
    skill_complexity = st.selectbox("Complexity Level:", ["Beginner", "Intermediate", "Advanced"])
    skill_category = st.text_input("Skill Category:")
    skill_description = st.text_area("Skill Description:")
    popularity_score = st.number_input("Popularity Score (0-100):", min_value=0.0, max_value=100.0, step=0.1)
    submit_skill = st.form_submit_button("Add Skill")

    if submit_skill:
        if skill_name and skill_complexity and skill_description and popularity_score is not None:
            success, error_message = add_skill({
                "skill_name": skill_name,
                "complexity": skill_complexity,
                "category": skill_category,
                "description": skill_description,
                "popularity_score": popularity_score,
            })
            if success:
                st.success("Skill added successfully!")
            else:
                st.error(f"Failed to add skill. Error: {error_message}")
        else:
            st.warning("Please complete all required fields.")

# Divider
st.markdown("---")
