##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Import the main Streamlit library as well as
# SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# Streamlit supports regular and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout='wide')

# If a user is at this page, we assume they are not 
# authenticated. So we change the 'authenticated' value
# in the Streamlit session_state to False. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# Set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('CS 3200 Sample Semester Project App: Algonauts Edition')
st.write('\n\n')
st.write('### Welcome! Please select a user persona to log in:')

# Create buttons for each persona and redirect to respective landing pages.

if st.button("Persona 1: Ambitious Student - Jamie Chen", 
             type='primary', 
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'ambitious_student'
    st.session_state['first_name'] = 'Jamie'
    logger.info("Logging in as Ambitious Student Persona")
    st.switch_page('pages/01a_ambitious_student_home.py')

if st.button("Persona 2: Career Shifter - Mark Davis", 
             type='primary', 
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'career_shifter'
    st.session_state['first_name'] = 'Mark'
    logger.info("Logging in as Career Shifter Persona")
    st.switch_page('pages/02_career_shifter_home.py')

if st.button("Persona 3: Job Seeker - Priya Patel", 
             type='primary', 
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'job_seeker'
    st.session_state['first_name'] = 'Priya'
    logger.info("Logging in as Job Seeker Persona")
    st.switch_page('pages/03_job_seeker_home.py')

if st.button("Persona 4: Goal-Oriented User - Alex Reyes", 
             type='primary', 
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'goal_oriented_user'
    st.session_state['first_name'] = 'Alex'
    logger.info("Logging in as Goal-Oriented User Persona")
    st.switch_page('pages/04_goal_oriented_user_home.py')

# Add any additional personas or functionality here as necessary.
