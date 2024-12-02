import requests
import streamlit as st
import pandas as pd
import plotly.express as px
from modules.nav import SideBarLinks

# Set page configuration for a wide layout
st.set_page_config(page_title="Skill Marketplace", layout="wide")

# Call the SideBarLinks from the nav module
SideBarLinks()

# Header with branding and user name
st.markdown(
    f"<h1 style='text-align: center; color: #4CAF50;'>Welcome to the Skill Marketplace, {st.session_state.get('first_name', 'User')}! 🚀</h1>",
    unsafe_allow_html=True
)
st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line separator

# Motivational tagline
st.markdown(
    """
    <h3 style='text-align: center; color: #555555;'>
    Discover in-demand technical skills, track your progress, and get closer to your dream career.
    </h3>
    """,
    unsafe_allow_html=True
)

# Define the API URL
API_URL = "http://api:4000/ts/all_skills"

# Fetch skills from the API
@st.cache_data
def fetch_skills():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad status codes
        skills = response.json()

        # Validate the response data structure
        if isinstance(skills, list) and len(skills) > 0:
            if isinstance(skills[0], list):
                # If response is a list of lists, map it to a DataFrame
                df = pd.DataFrame(skills, columns=["tech_skill_id", "skill_name", "complexity", "category", "popularity_score", "description"])
            elif isinstance(skills[0], dict):
                # If response is a list of dictionaries
                df = pd.DataFrame(skills)
            else:
                st.warning("Unexpected data format from the API.")
                return pd.DataFrame()  # Return an empty DataFrame in case of mismatch
            return df
        else:
            st.warning("No skills data received from the API.")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching skills: {e}")
        return pd.DataFrame()

# Fetch and display skills
df = fetch_skills()

if not df.empty:
    # Skill Overview Section
    st.subheader("🛠️ Skill Overview")
    st.write(f"Total Skills Available: **{len(df)}**")

    # Visualization: Skill Distribution by Complexity
    if "complexity" in df.columns:
        skill_counts = df["complexity"].value_counts().reset_index()
        skill_counts.columns = ["Complexity Level", "Number of Skills"]

        # Create an interactive bar chart using Plotly
        fig = px.bar(
            skill_counts,
            x="Complexity Level",
            y="Number of Skills",
            color="Complexity Level",
            title="Skill Distribution by Complexity",
            labels={"Complexity Level": "Complexity Level", "Number of Skills": "Number of Skills"},
            color_discrete_map={
                "Beginner": "#1f77b4",
                "Intermediate": "#ff7f0e",
                "Advanced": "#2ca02c"
            }
        )
        fig.update_layout(
            title_font_size=20,
            xaxis_title="Complexity Level",
            yaxis_title="Number of Skills",
            bargap=0.2,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#333333")
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No complexity data available for visualization.")

    # Full Skill List Section
    st.subheader("📋 Full Skill List")
    # Configure DataFrame display
    st.dataframe(
        df,
        use_container_width=True,
        column_config={
            "tech_skill_id": None,  # Hide this column
            "skill_name": "Skill Name",
            "complexity": st.column_config.Column(
                "Complexity Level",
                help="The difficulty level of the skill",
                width="medium"
            ),
            "category": "Category",
            "popularity_score": st.column_config.NumberColumn(
                "Popularity Score",
                format="%.2f",
                help="Popularity score ranging from 0 to 100"
            ),
            "description": st.column_config.Column(
                "Description",
                width="large"
            )
        }
    )

    # Export option for users
    st.download_button(
        label="📥 Download Skill List as CSV",
        data=df.to_csv(index=False),
        file_name="skills.csv",
        mime="text/csv"
    )
else:
    st.warning("⚠️ No skills available. Check back later or contact support!")

# Footer branding
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; color: #888888;">
        <small>Powered by <b>Algonauts</b> | Bringing Data to Life 🌟</small>
    </div>
    """,
    unsafe_allow_html=True
)
