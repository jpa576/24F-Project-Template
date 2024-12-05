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
st.set_page_config(page_title="Career Progress Dashboard", layout="wide")

# Initialize sidebar navigation
SideBarLinks()

# Page header
st.markdown(f"""
# 🚀 Career Progress Dashboard
Welcome back, **{st.session_state.get('first_name', 'User')}**!
""")
st.write("### Track your progress and uncover opportunities tailored to your goals.")

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

# Main layout: Career Progress and Skills
col1, col2 = st.columns([1, 1])

# Career Progress Section
with col1:
    st.markdown("## 📊 Your Career Progress")
    st.write("""
    Visualize your journey to success. Track mastered skills, progress milestones, 
    and future steps for achieving your career goals.
    """)

    if user_progress:
        df = pd.DataFrame(user_progress)
        st.markdown("### 📈 Progress Overview")
        st.table(df.rename(columns={"career_name": "Career Name", "progress_percentage": "Progress (%)"}))

        # Visualize Progress with Bar Chart
        fig = px.bar(
            df,
            x="career_name",
            y="progress_percentage",
            color="career_name",
            title="Career Progress by Percentage",
            labels={"career_name": "Career Name", "progress_percentage": "Progress (%)"},
            height=400
        )
        fig.update_layout(
            showlegend=False,
            xaxis_title="Career Path",
            yaxis_title="Progress Percentage",
            font=dict(size=14)
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("🚧 **No progress data available. Start your career journey today!**", icon="🚀")

# User Skills Section
with col2:
    st.markdown("## 🛠️ Your Acquired Skills")
    st.write("""
    Explore the skills you've acquired and their acquisition dates. Keep learning to achieve your goals.
    """)

    if user_skills:
        skills_df = pd.DataFrame(user_skills)
        st.markdown("### 🗂️ Skills Overview")
        st.table(
            skills_df.rename(columns={"skill_name": "Skill Name", "acquired_date": "Acquired Date"})
        )
    else:
        st.info("🚧 **No skills data available. Start acquiring new skills today!**", icon="🎓")

# Divider for additional sections
st.markdown("---")

# Interactive section: Explore Career Options
st.markdown("## 🔍 Explore Career Options")
st.write("""
Discover new roles or refine your career focus. This section will provide tailored 
recommendations based on your interests and progress.
""")
st.empty()  # Placeholder for future recommendations
st.info("🚧 **Career Suggestions Coming Soon!**", icon="💡")

# Call-to-action buttons for additional actions
st.markdown("---")
col3, col4 = st.columns([1, 1])

with col3:
    if st.button('📝 Update Career Goals', use_container_width=True):
        st.success("Redirecting to Career Goals Update Page... (Integration Pending)", icon="✅")
        st.switch_page('pages/14_CareerUpdate.py')

with col4:
    if st.button('📈 Practice relevant skills', use_container_width=True):
        st.success("Redirecting to Skill Recommendations Page...", icon="📈")
        st.switch_page('pages/12_CodingQuestions.py')

# Footer
st.markdown("---")
st.markdown("""
<small>
    Built with ❤️ using Streamlit | [Privacy Policy](#) | [Terms of Use](#)
</small>
""", unsafe_allow_html=True)
