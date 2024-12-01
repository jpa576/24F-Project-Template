import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Q4 2024 job market data please enjoy, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View hot tech skills',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_indemand_skills.py')

if st.button('View in Demand Careers',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_InDemand_Careers.py')

if st.button('View new homepage demo',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/03_jobmarket_home.py')