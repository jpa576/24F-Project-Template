import logging
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from modules.nav import SideBarLinks

# Set the current page context
if "current_page" not in st.session_state:
    st.session_state["current_page"] = None
st.session_state["current_page"] = "Career Progress Dashboard"

# Configure logger
logger = logging.getLogger(__name__)

# Set page configuration
st.set_page_config(
    page_title="Career Progress Dashboard",
    layout="wide",
    page_icon="🚀"
)

# Initialize sidebar navigation
SideBarLinks()

# Page header
st.markdown(f"""
# 🚀 Career Progress Dashboard
Welcome back, **{st.session_state.get('first_name', 'User')}**!
""")
st.write("### Visualize your career progress and track your skills in one place.")

# Divider for clarity
st.markdown("---")

# API Endpoints
USER_PROGRESS_API = "http://api:4000/u/1/progress"
USER_SKILLS_API = "http://api:4000/u/1/skills"


# Fetch User Progress
def fetch_user_progress():
    try:
        response = requests.get(USER_PROGRESS_API)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Unable to fetch progress data: {e}")
        return []


# Fetch User Skills
def fetch_user_skills():
    try:
        response = requests.get(USER_SKILLS_API)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Unable to fetch user skills: {e}")
        return []


# Fetch data
user_progress = fetch_user_progress()
user_skills = fetch_user_skills()

# Layout: Skills and Career Progress
col1, col2 = st.columns(2)

# Career Progress Section
with col1:
    st.markdown("### 🛤️ Career Progress Tracker")
    st.write("Monitor your journey and stay on track with your career goals.")

    if user_progress:
        df = pd.DataFrame(user_progress)

        # Visualize Progress with Pie Chart (Circular Display)
        fig_progress = px.pie(
            df,
            names="career_name",
            values="progress_percentage",
            title="Career Progress Overview",
            hole=0.4
        )
        fig_progress.update_traces(textinfo="percent+label")
        st.plotly_chart(fig_progress, use_container_width=True)
    else:
        st.info("🚧 **No progress data available. Start your career journey today!**", icon="🚀")

# User Skills Section
with col2:
    st.markdown("### 🛠️ Skills Inventory")
    st.write("Track the skills you've acquired and identify areas for growth.")

    if user_skills:
        skills_df = pd.DataFrame(user_skills)

        # Visualize Skills with Pie Chart (Circular Display)
        fig_skills = px.pie(
            skills_df,
            names="skill_name",
            title="Skill Distribution",
            hole=0.4
        )
        fig_skills.update_traces(textinfo="percent+label")
        st.plotly_chart(fig_skills, use_container_width=True)
    else:
        st.info("🚧 **No skills data available. Start building your skills today!**", icon="🎓")

# Divider for navigation buttons
st.markdown("---")

# Navigation Buttons
st.markdown("### 🎯 Take Action")
st.write("Ready to advance your career? Choose an action below to get started.")

col3, col4 = st.columns(2)

with col3:
    if st.button("📝 Update Career Goals"):
        st.success("Redirecting to Career Goals Update Page...", icon="✅")
        st.switch_page('pages/14_CareerUpdate.py')

with col4:
    if st.button("📈 Practice Relevant Skills"):
        st.success("Redirecting to Skill Recommendations Page...", icon="📈")
        st.switch_page('pages/12_CodingQuestions.py')

# Footer Section
st.markdown("---")
st.markdown("""
<small>
    Built with ❤️ using Streamlit | [Privacy Policy](#) | [Contact Us](mailto:support@algonauts.com)
</small>
""", unsafe_allow_html=True)
