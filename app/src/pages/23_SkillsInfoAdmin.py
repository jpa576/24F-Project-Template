import streamlit as st
import pandas as pd
import requests

# Set the page configuration
st.set_page_config(page_title="Manage Skills and Careers", layout="wide")

st.title("💼 Manage Skills and Careers")
st.write("View, add, or update skills and career paths in the system.")

# API endpoints to fetch and add skills/careers
SKILLS_API_URL = "http://api:4000/ts"  # 'ts' for tech skills
CAREERS_API_URL = "http://api:4000/careers"  # 'careers' for career paths

# Fetch skills
def fetch_skills():
    try:
        response = requests.get(SKILLS_API_URL)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching skills: {e}")
        return []

# Fetch careers
def fetch_careers():
    try:
        response = requests.get(CAREERS_API_URL + "/all_careers")
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching careers: {e}")
        return []

# Display skills
st.markdown("### Skills")
skills = fetch_skills()
if skills:
    df_skills = pd.DataFrame(skills)
    st.dataframe(df_skills)
else:
    st.info("No skills found.")

# Add a new skill
st.markdown("### Add a New Skill")
skill_name = st.text_input("Skill Name:")
skill_complexity = st.selectbox("Complexity Level:", ["Beginner", "Intermediate", "Advanced"])
skill_category = st.text_input("Skill Category (optional):")
skill_description = st.text_area("Skill Description:")
popularity_score = st.number_input("Popularity Score (0-100):", min_value=0.0, max_value=100.0, step=0.1)

if st.button("Add Skill"):
    try:
        response = requests.post(SKILLS_API_URL, json={
            "skill_name": skill_name,
            "complexity": skill_complexity,
            "category": skill_category,
            "description": skill_description,
            "popularity_score": popularity_score,
        })
        if response.status_code == 201:
            st.success("Skill added successfully!")
        else:
            st.error(f"Failed to add skill. Error: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error adding skill: {e}")

# Display careers
st.markdown("---")
st.markdown("### Careers")
careers = fetch_careers()
if careers:
    df_careers = pd.DataFrame(careers)
    st.dataframe(df_careers)
else:
    st.info("No careers found.")

# Add a new career
st.markdown("### Add a New Career")
career_name = st.text_input("Career Name:")
career_description = st.text_area("Career Description:")
salary = st.number_input("Average Salary:", min_value=0, step=1000)
demand = st.number_input("Demand (1-5):", min_value=1.0, max_value=5.0, step=0.1)

if st.button("Add Career"):
    try:
        response = requests.post(CAREERS_API_URL, json={
            "career_name": career_name,
            "description": career_description,
            "salary": salary,
            "demand": demand,
        })
        if response.status_code == 201:
            st.success("Career added successfully!")
        else:
            st.error(f"Failed to add career. Error: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error adding career: {e}")
