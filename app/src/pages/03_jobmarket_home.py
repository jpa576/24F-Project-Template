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
    - **Job Growth Trends**: Visualize long-term trends in the tech job market.
    - **Career Path Recommendations**: Find the right roles based on your unique skills.
    - **Regional Opportunities**: Dive into job availability in your preferred locations.
    """
)

# Data Source Acknowledgment
st.write("")
st.markdown("### 📈 **Data Sources**")
st.markdown(
    """
    Our insights are powered by reliable, up-to-date data sources, including:
    - **O*NET Online**: For occupational data and job characteristics.
    - **Bureau of Labor Statistics (BLS)**: For employment projections and salary benchmarks.
    - **Glassdoor & LinkedIn Trends**: For real-world salary reports and hiring trends.
    - **World Bank Data**: For macroeconomic indicators.
    """
)

# Interactive Buttons for Navigation
st.write("")
st.write("---")
st.markdown("### 🎯 **Get Started**")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔎 Explore Roles & Salaries"):
        st.session_state["page"] = "salary_explorer"
        #st.experimental_set_query_params(page="salary_explorer")
        st.success("Redirecting to Salary Explorer...")
        st.stop()

with col2:
    if st.button("📊 View Skills in Demand"):
        st.session_state["page"] = "skills_analysis"
        #st.experimental_set_query_params(page="skills_analysis")
        st.success("Redirecting to Skills Analysis...")
        st.stop()

with col3:
    if st.button("🌍 Explore Regional Trends"):
        st.session_state["page"] = "regional_trends"
        #st.experimental_set_query_params(page="regional_trends")
        st.success("Redirecting to Regional Trends...")
        st.stop()

# Footer with Contact Information and Data Credibility
st.write("")
st.write("---")
st.markdown(
    """
    #### 💡 **Need Personalized Advice?**
    Contact our job market experts or explore tailored insights for your skills and aspirations. 
    """
)
st.write("")

st.markdown(
    """
    ##### 🌟 **Disclaimer**: The data and insights provided here are based on third-party sources (e.g., O*NET, Glassdoor). While we strive for accuracy, always cross-check with official sources before making career decisions.
    """
)
