import logging
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from modules.nav import SideBarLinks

# Configure logger
logger = logging.getLogger(__name__)

# Set page configuration
st.set_page_config(page_title="Career Progress Dashboard", layout="wide")

# Initialize sidebar navigation
SideBarLinks()

# Page header
st.markdown(f"""
# 🚀 Career Progress Dashboard
Welcome back, **{st.session_state.get('first_name', 'User')}**!
""")
st.write("### Track your progress and uncover opportunities tailored to your goals.")

# Divider for clarity
st.markdown("---")


# Function to fetch career progress data
def fetch_career_progress():
    api_url = "http://api:4000/u/1/progress"
    try:
        with st.spinner("Fetching career progress data..."):
            response = requests.get(api_url, timeout=10)  # 10-second timeout
            response.raise_for_status()
            response_data = response.json()
            return response_data.get("data", [])  # Extract the 'data' key
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Unable to fetch progress data: {e}")
        return []


# Fetch progress data
progress_data = fetch_career_progress()

# Main layout: Career Progress and Insights
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("## 📊 Your Career Progress")
    st.write("""
    Visualize your journey to success. Track mastered skills, progress milestones, 
    and future steps for achieving your career goals.
    """)

    if progress_data:
        # Create a DataFrame from the extracted 'data' list
        df = pd.DataFrame(progress_data)

        # Cleanly format the DataFrame for display
        st.markdown("### 📈 Progress Overview")
        st.table(df.rename(columns={"career_name": "Career Name", "progress_percentage": "Progress (%)"}))

        # Visualize Progress
        fig = px.bar(
            df,
            x="career_name",
            y="progress_percentage",
            color="career_name",
            title="Career Progress by Percentage",
            labels={"career_name": "Career Name", "progress_percentage": "Progress (%)"},
            height=400
        )
        fig.update_layout(
            showlegend=False,
            xaxis_title="Career Path",
            yaxis_title="Progress Percentage",
            font=dict(size=14)
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("🚧 **No progress data available. Start your career journey today!**", icon="🚀")

with col2:
    st.markdown("## 🎯 Insights for Your Career Path")
    st.write("""
    Gain insights into demand, salaries, and key benchmarks for your chosen career path. 
    Use this data to stay ahead of the curve.
    """)

    # Ensure progress_data is available
    if progress_data:
        # Initialize session state for current career index
        if "career_index" not in st.session_state:
            st.session_state["career_index"] = 0

        # Get the current career data
        current_career = progress_data[st.session_state["career_index"]]

        # Display Career Insights
        st.markdown("### 📋 Career Overview")
        st.write(f"**Career Name:** {current_career['career_name']}")
        st.write(f"**Progress:** {current_career['progress_percentage']}%")

        # Placeholder for additional career details (e.g., demand, salary, description)
        st.markdown("### 📊 Additional Insights")
        st.write(f"💰 **Average Salary:** ${current_career.get('salary', 'N/A'):,}")
        st.write(f"🔥 **Demand:** {current_career.get('demand', 'N/A')}/5")
        st.write(f"📜 **Description:** {current_career.get('description', 'No description available.')}")

        # Navigation Buttons
        col_prev, col_next = st.columns([1, 1])
        with col_prev:
            if st.button("⬅️ Previous", key="prev"):
                if st.session_state["career_index"] > 0:
                    st.session_state["career_index"] -= 1

        with col_next:
            if st.button("➡️ Next", key="next"):
                if st.session_state["career_index"] < len(progress_data) - 1:
                    st.session_state["career_index"] += 1
    else:
        st.info("🚧 **No insights available. Start tracking your career paths!**", icon="📊")

# Divider for additional sections
st.markdown("---")

# Interactive section: Explore Career Options
st.markdown("## 🔍 Explore Career Options")
st.write("""
Discover new roles or refine your career focus. This section will provide tailored 
recommendations based on your interests and progress.
""")
st.empty()  # Placeholder for future recommendations
st.info("🚧 **Career Suggestions Coming Soon!**", icon="💡")

# Call-to-action buttons for additional actions
st.markdown("---")
col3, col4 = st.columns([1, 1])

with col3:
    if st.button('📝 Update Career Goals', use_container_width=True):
        st.success("Redirecting to Career Goals Update Page... (Integration Pending)", icon="✅")
        st.switch_page('pages/14_CareerUpdate.py')

with col4:
    if st.button('📈 Practice relevant skills', use_container_width=True):
        st.success("Redirecting to Skill Recommendations Page...", icon="📈")
        st.switch_page('pages/12_CodingQuestions.py')

# Footer for branding and navigation
st.markdown("---")
st.markdown("""
<small>
    Built with ❤️ using Streamlit | [Privacy Policy](#) | [Terms of Use](#)
</small>
""", unsafe_allow_html=True)
