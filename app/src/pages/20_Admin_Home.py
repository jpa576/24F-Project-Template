import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

# Configure logger
logger = logging.getLogger(__name__)

# Set page configuration
st.set_page_config(page_title="System Admin Home Page", layout='wide')

# Initialize sidebar navigation
SideBarLinks()

# Page Title
st.title("System Admin Home Page")
st.write("Manage all system data, including user information, courses, and skills.")

# Admin Actions
st.markdown("### Admin Actions:")
col1, col2, col3 = st.columns(3)

# Button to navigate to User Info Admin page
with col1:
    if st.button("🔍 Manage User Information", type="primary", use_container_width=True):
        st.switch_page("pages/21_UserInfoAdmin.py")

# Button to navigate to Course Info Admin page
with col2:
    if st.button("📚 Manage Courses", type="primary", use_container_width=True):
        st.switch_page("pages/22_CourseInfoAdmin.py")

# Button to navigate to Skills Info Admin page
with col3:
    if st.button("💼 Manage Skills ", type="primary", use_container_width=True):
        st.switch_page("pages/23_SkillsInfoAdmin.py")


