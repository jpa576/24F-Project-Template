import streamlit as st
import pandas as pd
import requests

# Set the page configuration
st.set_page_config(page_title="Manage Skills and Careers", layout="wide")

st.title("💼 Manage Skills and Careers")
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

# Fetch careers
def fetch_careers():
    try:
        response = requests.get(f"{CAREERS_API_URL}/all_careers")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching careers: {e}")
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

# Add a new career
def add_career(career_data):
    try:
        response = requests.post(f"{CAREERS_API_URL}/add_career", json=career_data)
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

# Display Careers
st.markdown("### Careers")
careers = fetch_careers()
if careers:
    df_careers = pd.DataFrame(careers, columns=["ID", "Career Name", "Description", "Salary", "Demand"])
    st.dataframe(df_careers, use_container_width=True)
else:
    st.info("No careers found.")

# Form to Add a New Career
st.markdown("### Add a New Career")
with st.form("Add Career"):
    career_name = st.text_input("Career Name:")
    career_description = st.text_area("Career Description:")
    salary = st.number_input("Average Salary:", min_value=0, step=1000)
    demand = st.number_input("Demand (1-5):", min_value=1.0, max_value=5.0, step=0.1)
    submit_career = st.form_submit_button("Add Career")

    if submit_career:
        if career_name and career_description and salary > 0 and demand is not None:
            success, error_message = add_career({
                "career_name": career_name,
                "description": career_description,
                "salary": salary,
                "demand": demand,
            })
            if success:
                st.success("Career added successfully!")
                st.experimental_rerun()
            else:
                st.error(f"Failed to add career. Error: {error_message}")
        else:
            st.warning("Please complete all required fields.")
