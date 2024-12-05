import requests
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks


# Set page configuration
st.set_page_config(page_title="Career Skills Explorer", layout="wide", initial_sidebar_state="expanded")

# Initialize the sidebar navigation
SideBarLinks()

# Set the page header
st.markdown("""
    <style>
        .header {
            text-align: center;
            font-family: Arial, sans-serif;
            color: #4CAF50;
        }
        .subheader {
            text-align: center;
            font-family: Arial, sans-serif;
            color: #555555;
        }
        .dropdown-label {
            font-weight: bold;
            margin-bottom: 10px;
        }
    </style>
    <h1 class="header">🎓 Career Skills Explorer</h1>
    <p class="subheader">Discover skills associated with specific careers.</p>
    <hr>
""", unsafe_allow_html=True)

# API URLs
CAREERS_API_URL = "http://api:4000/careers/all_careers"
CAREER_SKILLS_API_URL = "http://api:4000/careers/career_skills"

# Function to fetch all careers from the API
def fetch_all_careers():
    try:
        with st.spinner("Fetching careers..."):
            response = requests.get(CAREERS_API_URL, timeout=10)
            response.raise_for_status()
            return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Unable to fetch careers: {e}")
        return []

# Function to fetch career skills based on career_path_id
def fetch_career_skills(career_path_id):
    try:
        with st.spinner("Fetching career skills..."):
            response = requests.get(f"{CAREER_SKILLS_API_URL}?career_path_id={career_path_id}", timeout=10)
            response.raise_for_status()
            return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Unable to fetch skills: {e}")
        return []

# Fetch all careers
careers = fetch_all_careers()

if careers:
    # Convert careers into a DataFrame for better manipulation
    careers_df = pd.DataFrame(careers)
    careers_df = careers_df.rename(
        columns={
            "career_name": "Career Name",
            "career_path_id": "Career Path ID",
            "description": "Description",
            "salary": "Salary",
            "demand": "Demand"
        }
    )

    # Dropdown to select a career
    st.markdown("### Select a Career to Explore Skills")
    selected_career_name = st.selectbox(
        "Choose a Career",
        options=["Select a Career"] + list(careers_df["Career Name"])
    )

    if selected_career_name != "Select a Career":
        # Extract the career_path_id for the selected career
        career_path_id = careers_df.loc[
            careers_df["Career Name"] == selected_career_name, "Career Path ID"
        ].values[0]

        # Fetch career skills for the selected career
        skills = fetch_career_skills(career_path_id)

        if skills:
            st.markdown(f"## Skills for {selected_career_name}")
            # Convert the skills data to a DataFrame
            skills_df = pd.DataFrame(skills)
            # Display the DataFrame
            st.dataframe(
                skills_df.rename(
                    columns={
                        "skill_name": "Skill Name",
                        "complexity": "Complexity Level",
                        "relevance": "Relevance (%)",
                    }
                ),
                use_container_width=True,
            )

            # Add download button for skills data
            csv = skills_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Skills Data",
                data=csv,
                file_name=f"{selected_career_name.lower().replace(' ', '_')}_skills.csv",
                mime="text/csv",
            )
        else:
            st.warning(f"No skills available for {selected_career_name}.")
    else:
        st.info(f"Select a career from the dropdown above to view associated skills.")
else:
    st.warning("No careers data available. Please try again later.")

# Footer for better user experience
st.markdown("---")
st.markdown("💡 **Tip:** Use the dropdown to explore skills for different careers.")
st.caption("Powered by Career Skills API | Designed with ❤️ using Streamlit.")
