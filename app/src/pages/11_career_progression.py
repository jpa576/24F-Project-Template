import logging
import streamlit as st
from modules.nav import SideBarLinks

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

# Main layout: Career Progress and Insights
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("## 📊 Your Career Progress")
    st.write("""
    Visualize your journey to success. Track mastered skills, progress milestones, 
    and future steps for achieving your career goals.
    """)
    st.empty()  # Placeholder for future dynamic career progress charts
    st.info("🚧 **Career Progress Visuals Coming Soon!**", icon="🚀")

with col2:
    st.markdown("## 🎯 Insights for Your Career Path")
    st.write("""
    Gain insights into demand, salaries, and key benchmarks for your chosen career path. 
    Use this data to stay ahead of the curve.
    """)
    st.empty()  # Placeholder for career path insights
    st.info("🔍 **Career Insights Will Appear Here Soon!**", icon="📊")

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

with col4:
    if st.button('📈 View Skill Recommendations', use_container_width=True):
        st.success("Redirecting to Skill Recommendations Page... (Integration Pending)", icon="📈")

# Footer for branding and navigation
st.markdown("---")
st.markdown("""
<small>
    Built with ❤️ using Streamlit | [Privacy Policy](#) | [Terms of Use](#)
</small>
""", unsafe_allow_html=True)
