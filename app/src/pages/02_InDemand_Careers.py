import requests
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks


# Set page configuration
st.set_page_config(page_title="Careers", layout="wide")
# Initialize sidebar navigation
SideBarLinks()

# Page header
st.header("Explore Careers")

# Personalized welcome message
if "first_name" in st.session_state:
    st.write(f"### Hi, {st.session_state['first_name']}!")
else:
    st.warning("Please log in to personalize your experience.")

# API Base URL
API_URL = "http://api:4000/careers/all_careers"

# Function to fetch careers from the API
def fetch_careers():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        # Validate and parse the data structure
        if "data" in data and isinstance(data["data"], list):
            return pd.DataFrame(data["data"])
        else:
            st.warning("Unexpected data format received from the API.")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching careers: {e}")
        return pd.DataFrame()

# Fetch careers
careers_df = fetch_careers()

# Display careers
if not careers_df.empty:
    st.write("### Top 10 Careers")

    # Rename columns for display
    column_mapping = {
        'career_name': 'Career Name',
        'description': 'Description',
        'salary': 'Salary',
        'demand': 'Demand'
    }
    careers_df = careers_df.rename(columns=column_mapping)

    # Convert Salary to numeric and sort by Salary
    if "Salary" in careers_df.columns:
        careers_df["Salary"] = pd.to_numeric(careers_df["Salary"], errors="coerce")
        careers_df = careers_df.sort_values(by="Salary", ascending=False)

    # Top 10 Careers
    top_10_careers = careers_df.head(10).reset_index(drop=True)

    # Initialize session state index
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0

    # Navigation logic
    def next_item():
        if st.session_state.current_index < len(top_10_careers) - 1:
            st.session_state.current_index += 1

    def prev_item():
        if st.session_state.current_index > 0:
            st.session_state.current_index -= 1

    # Layout for navigation and career details
    col1, col2, col3 = st.columns([1, 8, 1])

    with col1:
        if st.button("⬅️ Previous", key="prev"):
            prev_item()

    with col2:
        # Display current career
        current_career = top_10_careers.iloc[st.session_state.current_index]

        rank = st.session_state.current_index + 1  # Rank from 1 to 10
        st.markdown(f"<h1 style='font-size: 72px; text-align: center;'>#{rank}</h1>", unsafe_allow_html=True)
        st.write(f"**Career Name:** {current_career['Career Name']}")
        st.write(f"*{current_career['Description']}*")
        st.write(f"💰 **Salary:** ${current_career['Salary']:,}")
        st.write(f"🔥 **Demand:** {current_career['Demand']}/5")

    with col3:
        if st.button("Next ➡️", key="next"):
            next_item()

    # Display all careers in a table for reference
    st.markdown("### Complete List of Careers")
    st.dataframe(careers_df, use_container_width=True)
else:
    st.warning("No careers available.")
