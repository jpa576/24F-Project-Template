##################################################
# Entry-Point File for the Sample Application
# CS 3200 Semester Project: Algonauts
##################################################

# Import necessary libraries
import logging
import streamlit as st
from modules.nav import SideBarLinks

# Set up logging infrastructure
logging.basicConfig(
    format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configure Streamlit layout
st.set_page_config(
    layout='wide',
    page_icon="🚀",  # Astronaut icon for a professional look
    page_title="Algonauts App"
)

# Initialize session state
st.session_state['authenticated'] = False

# Sidebar navigation setup
# IMPORTANT: Ensure src/.streamlit/config.toml sets `showSidebarNavigation = false` in the `[client]` section
SideBarLinks(show_home=True)

# ***************************************************
# Main Content of the Home Page
# ***************************************************

logger.info("Loading the Home page of the app")

# Page title and introductory text
st.title('CS 3200 Semester Project: Algonauts 🚀')
st.write('### Welcome to Algonauts! \nSelect a user role to log in:')

# User role buttons for different personas
if st.button(
    label="Log in as Jack - Job Market Enthusiast",
    type='primary',
    use_container_width=True
):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'Job Market Enthusiast'
    st.session_state['first_name'] = 'Jack'
    logger.info("Logged in as Jack - Job Market Enthusiast")
    st.switch_page('pages/00_jobmarket_home.py')

if st.button(
    label="Log in as Marcus - CS Student",
    type='primary',
    use_container_width=True
):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'CS Student'
    st.session_state['first_name'] = 'Marcus'
    logger.info("Logged in as Marcus - CS Student")
    st.switch_page('pages/10_userdash_home.py')

if st.button(
    label="Log in as System Administrator",
    type='primary',
    use_container_width=True
):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'Administrator'
    st.session_state['first_name'] = 'SysAdmin'
    logger.info("Logged in as System Administrator")
    st.switch_page('pages/20_Admin_Home.py')
