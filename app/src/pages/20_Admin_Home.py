import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

# Configure logger
logger = logging.getLogger(__name__)

# Set page configuration
st.set_page_config(
    page_title="System Admin Home Page",
    layout="wide",
    page_icon="🖥️"
)

# Initialize sidebar navigation
SideBarLinks()

# Page Title and Description
st.title("🖥️ System Admin Dashboard")
st.markdown("""
Welcome, **System Administrator**.  
This is your central hub to manage all system resources, including user information, courses, and skills.
""")

# Divider for clarity
st.markdown("---")

# Admin Actions Section
st.markdown("## ⚙️ **Administrative Actions**")
st.write("Select an action below to manage system data efficiently.")

# Action Buttons Layout
col1, col2, col3 = st.columns(3)

# Button to navigate to User Info Admin page
with col1:
    st.markdown("### 👥 Manage Users")
    st.write("Handle user information, roles, and permissions.")
    if st.button("🔍 Manage User Information", use_container_width=True):
        st.switch_page("pages/21_UserInfoAdmin.py")

# Button to navigate to Course Info Admin page
with col2:
    st.markdown("### 📚 Manage Courses")
    st.write("Oversee course data, descriptions, and availability.")
    if st.button("📚 Manage Courses", use_container_width=True):
        st.switch_page("pages/22_CourseInfoAdmin.py")

# Button to navigate to Skills Info Admin page
with col3:
    st.markdown("### 💼 Manage Skills")
    st.write("Maintain the database of skills and their mappings.")
    if st.button("💼 Manage Skills", use_container_width=True):
        st.switch_page("pages/23_SkillsInfoAdmin.py")


# Footer Section
st.markdown("---")
st.markdown("""
<small>
    Built with ❤️ using Streamlit | [Privacy Policy](#) | [Terms of Use](#) | [Contact Us](mailto:support@algonauts.com)
</small>
""", unsafe_allow_html=True)
