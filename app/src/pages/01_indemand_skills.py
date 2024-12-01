import requests
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
import matplotlib.pyplot as plt

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header with branding and user name
st.title(f"Welcome to the Skill Marketplace, {st.session_state.get('first_name', 'User')}! 🚀")
st.write("___")  # Separator for a cleaner UI

# Add a motivational tagline
st.markdown(
    """
    **Discover in-demand technical skills, track your progress, and get closer to your dream career.**
    """
)

# Define the API URL
API_URL = "http://api:4000/ts/all_skills"


# Fetch skills from the API
def fetch_skills():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad status codes
        skills = response.json()

        # Validate the response data structure
        if isinstance(skills, list) and len(skills) > 0 and isinstance(skills[0], list):
            # If response is a list of lists, map it to a DataFrame
            df = pd.DataFrame(skills, columns=["tech_skill_id", "skill_name", "complexity", "description"])
            return df
        elif isinstance(skills, list) and isinstance(skills[0], dict):
            # If response is a list of dictionaries
            return pd.DataFrame(skills)
        else:
            st.warning("Unexpected data format from the API.")
            return pd.DataFrame()  # Return an empty DataFrame in case of mismatch
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching skills: {e}")
        return pd.DataFrame()


# Fetch and display skills
df = fetch_skills()

if not df.empty:
    # Display a summary of skills
    st.subheader("🛠️ Skill Overview")
    st.write(f"Total Skills Available: **{len(df)}**")

    # Generate a bar chart showing skill categories (if applicable)
    if "complexity" in df.columns:
        skill_counts = df["complexity"].value_counts()

        # Create a chart
        fig, ax = plt.subplots(figsize=(8, 4))
        skill_counts.plot(kind="bar", color=["#1f77b4", "#ff7f0e", "#2ca02c"], ax=ax)
        ax.set_title("Skill Distribution by Complexity", fontsize=14, weight="bold")
        ax.set_xlabel("Skill Level", fontsize=12)
        ax.set_ylabel("Number of Skills", fontsize=12)
        st.pyplot(fig)
    else:
        st.info("No complexity data available for visualization.")

    # Display the skills in a styled table
    st.subheader("📋 Full Skill List")
    st.dataframe(
        df.style.format(precision=2).set_table_styles([
            {"selector": "thead th", "props": [("font-size", "14px"), ("text-align", "center")]},
            {"selector": "tbody td", "props": [("font-size", "12px"), ("padding", "10px")]}
        ])
    )

    # Add an export option for users
    st.download_button(
        label="📥 Download Skill List as CSV",
        data=df.to_csv(index=False),
        file_name="skills.csv",
        mime="text/csv"
    )
else:
    st.warning("⚠️ No skills available. Check back later or contact support!")

# Add footer branding
st.write("___")
st.markdown(
    """
    <div style="text-align: center; color: #888888;">
        <small>Powered by <b>Algonauts</b> | Bringing Data to Life 🌟</small>
    </div>
    """,
    unsafe_allow_html=True
)
