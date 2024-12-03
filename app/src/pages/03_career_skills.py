import requests
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks

# Initialize the sidebar navigation
SideBarLinks()

# Set the page header
st.title('🎓 Career Skills Explorer')

# Display a personalized greeting
user_name = st.session_state.get('first_name', 'Guest')
st.subheader(f"👋 Welcome, {user_name}! Explore skills associated with your dream careers.")

# API URL for fetching career skills
API_URL = "http://api:4000/careers/career_skills1"


# Function to fetch career skills from the API
def fetch_career_skills():
    try:
        with st.spinner("Fetching career skills..."):
            response = requests.get(API_URL, timeout=10)  # 10-second timeout
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Unable to fetch career skills: {e}")
        return []


# Fetch career skills
career_skills = fetch_career_skills()

# Display the career skills table
if career_skills:
    st.markdown("## 📂 Available Careers and Skills")

    # Convert the data into a DataFrame
    df = pd.DataFrame(career_skills, columns=['Career', 'Skill'])

    # Add a dropdown to filter by career
    st.markdown("### 🎯 Filter by Career")
    unique_careers = df['Career'].unique()
    selected_career = st.selectbox("Select a Career", ["All"] + list(unique_careers))

    # Filter data based on the career selection
    filtered_df_career = df if selected_career == "All" else df[df['Career'] == selected_career]

    # Display the filtered data in a styled table
    st.markdown("### 📋 Career Skills Table (Filtered by Career)")
    st.write(filtered_df_career.style.set_table_styles(
        [
            {"selector": "thead th", "props": [("background-color", "#4CAF50"), ("color", "white")]},
            {"selector": "tbody tr:nth-child(even)", "props": [("background-color", "#f2f2f2")]},
        ]
    ))

    # Add a text input with auto-completion to filter by skill
    st.markdown("### 🔍 Search Careers by Skill")
    all_skills = sorted(df['Skill'].unique())  # Get all unique skills
    search_skill = st.text_input(
        "Type a Skill to See Associated Careers (Auto-Complete Enabled)",
        placeholder="Start typing a skill...",
        help="Search for skills like 'Python', 'Machine Learning', etc."
    )

    # Show a dropdown with suggestions as users type
    if search_skill:
        suggestions = [skill for skill in all_skills if search_skill.lower() in skill.lower()]
        if suggestions:
            st.markdown("### 🔍 Suggestions:")
            st.write(", ".join(suggestions))

        # Filter by the entered skill
        filtered_df_skill = df[df['Skill'].str.contains(search_skill, case=False, na=False)]
        if not filtered_df_skill.empty:
            st.markdown("### 📋 Careers Associated with the Skill")
            st.write(filtered_df_skill.style.set_table_styles(
                [
                    {"selector": "thead th", "props": [("background-color", "#FF5722"), ("color", "white")]},
                    {"selector": "tbody tr:nth-child(even)", "props": [("background-color", "#f2f2f2")]},
                ]
            ))
        else:
            st.warning(f"No careers found associated with the skill: {search_skill}")

    # Add a download button for career-skills data
    st.markdown("### 📥 Download Skills Data")
    csv = filtered_df_career.to_csv(index=False)
    st.download_button(
        label="Download as CSV",
        data=csv,
        file_name=f"{selected_career.lower().replace(' ', '_')}_skills.csv" if selected_career != "All" else "all_career_skills.csv",
        mime="text/csv",
    )
else:
    st.warning("No career skills data available at the moment. Please try again later.")

# Add footer for better user experience
st.markdown("---")
st.markdown("💡 **Tip:** Select a career from the dropdown or type a skill in the search bar to filter the data.")
st.caption("Powered by Career Skills API | Designed with ❤️ using Streamlit.")
