import streamlit as st
from modules.nav import SideBarLinks


SideBarLinks()

# Page Title and Header
st.title(f"🚀 Q4 2024 Job Market Insights for Aspiring Tech Professionals, {st.session_state['first_name']}!")
st.write("")
st.subheader("Welcome to Your Personal Job Market Dashboard")
st.markdown(
    """
    Gain data-driven insights into the technology job market. Explore salary trends, in-demand skills, job availability, and more. 
    Tailored specifically for your career aspirations in computer science and related fields. Let's bridge the gap between your skills and the market demands. 
    """,
    unsafe_allow_html=True,
)

# Hero Section: Quick Overview
st.write("")
st.write("---")
st.markdown("### 🔍 **What’s Available on Your Dashboard?**")
st.markdown(
    """
    - **Salary Explorer**: Compare salaries across roles, locations, and industries.
    - **Skills Demand Analysis**: See which technical skills employers are prioritizing in real time.
    - **Career Skills**: Visualize recommended skills for any career in our database.
    """
)

# Interactive Buttons for Navigation
st.write("")
st.write("---")
st.markdown("### 🎯 **Get Started**")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 View Skills in Demand"):
        st.switch_page('pages/01_indemand_skills.py')

with col2:
    if st.button("🔎 Explore Roles & Salaries"):
        st.switch_page('pages/02_InDemand_Careers.py')

with col3:
    if st.button("🌍 Explore Careers and their Required Skills"):
        st.switch_page('pages/03_career_skills.py')

# Footer with Contact Information and Data Credibility
st.write("")
st.write("---")

st.markdown(
    """
    ##### 🌟 **Disclaimer**: The insights provided are AI-generated and based on publicly available data sources (e.g., O*NET, Glassdoor). 
    While we strive for accuracy, always cross-check with official sources before making career decisions. AI-generated data may not 
    fully capture real-world nuances and trends.
    """
)
