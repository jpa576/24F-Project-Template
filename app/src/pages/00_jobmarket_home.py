import streamlit as st
from modules.nav import SideBarLinks

# Initialize Sidebar Navigation
SideBarLinks()

# Page Title and Header
st.title(f"🚀 Q4 2024 Job Market Insights for Aspiring Tech Professionals, {st.session_state['first_name']}!")
st.markdown(
    """
    ---
    **Welcome to Your Personal Job Market Dashboard!**  
    Gain data-driven insights into the technology job market tailored to your career aspirations.  
    Explore salary trends, in-demand skills, job availability, and actionable recommendations.  
    Let's bridge the gap between your potential and market demands!
    """,
    unsafe_allow_html=True,
)

# Hero Section: Quick Overview
st.markdown("### 🔍 **Key Features of Your Dashboard**")
st.markdown(
    """
    - 💼 **Salary Explorer**: Analyze salaries by role, location, and industry.
    - 📈 **Skills Demand Analysis**: Identify real-time trends in tech skills employers seek.
    - 🌐 **Career Skills Recommendations**: Discover key skills for careers in computer science and tech fields.
    """
)

# Interactive Section: Navigation Buttons
st.write("")
st.markdown("---")
st.markdown("### 🎯 **Ready to Dive In? Select an Option Below:**")

# Layout for navigation buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 View Skills in Demand"):
        st.switch_page('pages/01_indemand_skills.py')

with col2:
    if st.button("🔎 Explore Roles & Salaries"):
        st.switch_page('pages/02_InDemand_Careers.py')

with col3:
    if st.button("🌐 Explore Careers & Required Skills"):
        st.switch_page('pages/03_career_skills.py')

# Professional Footer with Contact Information
st.markdown("---")
st.markdown(
    """
    #### ⚠️ **Disclaimer**  
    Insights are AI-generated using reliable data sources (e.g., O*NET, Glassdoor).  
    While accurate, these insights should be cross-checked with official resources for critical decisions.  
    Use this tool as a guide to navigate trends and opportunities in the tech industry.
    """
)

# Add Contact Information
st.markdown(
    """
    #### 📬 **Contact Support**  
    Have questions or feedback? Reach out to us at [support@algonauts.com](mailto:support@algonauts.com).  
    Your input helps us improve!
    """
)
