import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Configure logger
logger = logging.getLogger(__name__)


# Set page configuration
st.set_page_config(page_title="Coding Challenges", layout="wide")

# Initialize sidebar navigation
SideBarLinks()

# Page Header
st.markdown(
    """
    # 🧑‍💻 Explore Coding Challenges
    ### Choose a problem to solve and enhance your skills with real-time feedback.
    """
)

# Divider for clarity
st.markdown("---")

# Function to fetch coding assessments
def fetch_coding_assessments():
    api_url = "http://api:4000/ass/all_assessments"
    try:
        with st.spinner("Fetching coding challenges..."):
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            data = response.json()  # Assume API returns a list
            return data  # Directly return the list of problems
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Unable to fetch coding challenges: {e}")
        return []

# Fetch coding assessments
coding_problems = fetch_coding_assessments()

# Display coding problems dynamically
if coding_problems:
    st.markdown("## 🛠️ Available Coding Challenges")
    for problem in coding_problems:
        # Extract problem details
        assessment_id = problem.get("assessment_id")
        problem_title = problem.get("problem_statement", "Untitled Problem")

        # Display as an interactive button
        if st.button(problem_title, key=f"problem_{assessment_id}"):
            # Store problem details in session state for the IDE page
            st.session_state["selected_problem_id"] = assessment_id
            st.session_state["selected_problem_title"] = problem_title
            st.session_state["selected_input_example"] = problem.get("input_example")
            st.session_state["selected_expected_output"] = problem.get("expected_output")

            # Redirect to the IDE page
            st.switch_page("pages/12_python_coding.py")
else:
    st.info("🚧 No coding challenges available. Please check back later.", icon="⚙️")

# Footer for branding
st.markdown("---")
st.markdown(
    """
    <small>
    Powered by <b>Algonauts</b> | [Privacy Policy](#) | [Terms of Use](#)
    </small>
    """,
    unsafe_allow_html=True,
)
