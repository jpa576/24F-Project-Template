import requests
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header('Careers Ranked by Salary')

# Access the session state to make a more customized/personalized app experience
if "first_name" in st.session_state:
    st.write(f"### Hi, {st.session_state['first_name']}.")
else:
    st.warning("Please log in to personalize your experience.")

# API URL
API_URL = "http://api:4000/careers/by_salary"

# Fetch careers from the API
def fetch_careers():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad status codes
        response_json = response.json()

        # Extract the "data" field if it exists
        if "data" in response_json and isinstance(response_json["data"], list):
            careers = response_json["data"]
        else:
            st.warning("Unexpected data format from the API.")
            return pd.DataFrame()  # Return an empty DataFrame if data is invalid

        if not careers:
            st.warning("No data received from the API.")
            return pd.DataFrame()

        # Create DataFrame from the extracted data
        return pd.DataFrame(careers, columns=["career_name", "description", "salary", "demand"])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching careers: {e}")
        return pd.DataFrame()

# Fetch careers from the API
careers_df = fetch_careers()

# Display the careers
if not careers_df.empty:
    st.write("### Top 10 Careers Ranked by Salary")

    # Map columns manually
    column_mapping = {
        'career_name': 'Career Name',
        'description': 'Description',
        'salary': 'Salary',
        'demand': 'Demand'
    }
    careers_df = careers_df.rename(columns=column_mapping)

    # Ensure salary is numeric and sort by it (highest first)
    if 'Salary' in careers_df.columns:
        careers_df['Salary'] = pd.to_numeric(careers_df['Salary'], errors='coerce')  # Convert salary to numeric
        careers_df = careers_df.sort_values(by='Salary', ascending=False)

    # Top 10 entries
    top_10_careers = careers_df.head(10).reset_index(drop=True)

    # Initialize session state index
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0

    # Navigation logic
    def next_item():
        if st.session_state.current_index < len(top_10_careers) - 1:
            st.session_state.current_index += 1

    def prev_item():
        if st.session_state.current_index > 0:
            st.session_state.current_index -= 1

    # Layout: Horizontal navigation with arrows
    col1, col2, col3 = st.columns([1, 8, 1])

    with col1:
        if st.button("⬅️", key="prev"):
            prev_item()

    with col2:
        # Current Career Data
        current_career = top_10_careers.iloc[st.session_state.current_index]

        # Display Rank and Career Information
        rank = st.session_state.current_index + 1  # Rank from 1 to 10
        st.markdown(f"<h1 style='font-size: 72px; text-align: center;'>#{rank}</h1>", unsafe_allow_html=True)
        st.write(f"**{current_career['Career Name']}**")
        st.write(f"*{current_career['Description']}*")
        st.write(f"💰 **Salary**: ${current_career['Salary']:,}")
        st.write(f"🔥 **Demand**: {current_career['Demand']}/5")

    with col3:
        if st.button("➡️", key="next"):
            next_item()

    # Show the complete DataFrame below for reference
    st.write("### All Careers Ranked by Salary")
    st.dataframe(careers_df)
else:
    st.warning("No careers available.")
