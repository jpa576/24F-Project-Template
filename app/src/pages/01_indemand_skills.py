import logging
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from modules.nav import SideBarLinks

# Configure logger
logger = logging.getLogger(__name__)

# Set page configuration for a wide layout
st.set_page_config(page_title="Career Progress Dashboard", layout="wide")

# Call the SideBarLinks from the nav module
SideBarLinks()

# Header with branding and username
st.markdown(
    f"<h1 style='text-align: center; color: #4CAF50;'>Welcome to the Career Progress Dashboard, {st.session_state.get('first_name', 'User')}! 🚀</h1>",
    unsafe_allow_html=True
)
st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line separator

# Motivational tagline
st.markdown(
    """
    <h3 style='text-align: center; color: #555555;'>
    Track your progress and uncover opportunities tailored to your dream career.
    </h3>
    """,
    unsafe_allow_html=True
)

# Define the API URL for career progress
API_URL = "http://api:4000/u/get_progress"

# Fetch career progress data from the API
@st.cache_data
def fetch_career_progress():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad status codes
        progress_data = response.json()
        if isinstance(progress_data, list) and len(progress_data) > 0:
            return pd.DataFrame(progress_data, columns=["Career Path", "Progress Percentage"])
        else:
            st.warning("No career progress data received from the API.")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching career progress: {e}")
        return pd.DataFrame()

# Fetch and display career progress
df = fetch_career_progress()

if not df.empty:
    # Career Progress Overview Section
    st.subheader("📊 Career Progress Overview")
    st.write(f"Tracking progress for **{len(df)} career paths**. Stay on track to achieve your goals!")

    # Visualization: Career Progress Distribution
    st.markdown("### 📈 Progress Distribution Across Career Paths")
    if "Progress Percentage" in df.columns:
        fig = px.bar(
            df,
            x="Career Path",
            y="Progress Percentage",
            title="Career Progress by Path",
            labels={"Career Path": "Career Path", "Progress Percentage": "Progress (%)"},
            text="Progress Percentage",
            color="Career Path",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_layout(
            title_font_size=20,
            xaxis_title="Career Path",
            yaxis_title="Progress (%)",
            bargap=0.2,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#333333")
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No progress data available for visualization.")

    # Career Progress Table
    st.subheader("📋 Detailed Career Progress")
    st.dataframe(
        df,
        use_container_width=True,
        column_config={
            "Career Path": st.column_config.Column("Career Path", width="medium"),
            "Progress Percentage": st.column_config.NumberColumn(
                "Progress (%)",
                format="%.2f",
                help="Percentage of progress completed for each career path"
            )
        }
    )

    # Export option for users
    st.download_button(
        label="📥 Download Career Progress as CSV",
        data=df.to_csv(index=False),
        file_name="career_progress.csv",
        mime="text/csv"
    )
else:
    st.warning("⚠️ No career progress available. Start tracking your progress today!")

# Footer branding
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; color: #888888;">
        <small>Powered by <b>Algonauts</b> | Empowering Your Career Progress 🌟</small>
    </div>
    """,
    unsafe_allow_html=True
)
