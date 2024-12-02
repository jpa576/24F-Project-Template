import requests
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Careers')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

# API URL
API_URL = "http://api:4000/careers/all_careers"


def fetch_courses():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Expect the data as JSON
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching courses: {e}")
        return []

# Fetch courses from the API
courses = fetch_courses()

# Display the courses
if courses:
    st.write("### Available Careers")
    # Convert to DataFrame for better tabular display
    df = pd.DataFrame(courses)
    st.dataframe(df)  # Use Streamlit's dataframe viewer
else:
    st.warning("No careers available.")
