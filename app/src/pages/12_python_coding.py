import logging
import streamlit as st
import requests
import sys
from io import StringIO
from modules.nav import SideBarLinks

# API Endpoints
SAVE_SUBMISSION_API = "http://api:4000/ass/save_submission"
UPDATE_PROGRESS_API = "http://api:4000/u/1/update_progress"

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Set page configuration
st.set_page_config(page_title="Python IDE", layout="wide")
SideBarLinks()

# Header
st.markdown("# 🐍 Python IDE")
st.write("Write your Python script below, click Run, and see the results in real-time!")

# Check if problem details are passed via `st.session_state`
if "selected_problem_id" in st.session_state:
    problem_statement = st.session_state.get("selected_problem_title", "No problem selected.")
    input_example = st.session_state.get("selected_input_example", "No input example.")
    expected_output = st.session_state.get("selected_expected_output", "No expected output.")
    career_path_id = st.session_state.get("career_path_id", 1)  # Default to Software Engineer
    user_id = st.session_state.get("user_id", 1)  # Default user ID

    # Display selected problem details
    st.markdown("### 📝 Problem Details")
    st.markdown(f"**Problem Statement:** {problem_statement}")
    st.markdown(f"**Input Example:** `{input_example}`")
    st.markdown(f"**Expected Output:** `{expected_output}`")
else:
    st.warning("No problem selected. Please choose a problem from the problem list page.")

# Code input area
code = st.text_area("Type your Python code here:", height=300, placeholder="e.g., print('Hello, World!')")

# Output area
st.markdown("### 🖥️ Output")
if st.button("Run"):
    if not code.strip():
        st.warning("Please enter some Python code to execute.")
    else:
        # Redirect stdout to capture the print statements
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            # Execute the code
            exec_globals = {}
            exec(code, exec_globals)

            # Capture the output
            output = sys.stdout.getvalue().strip()

            # Display the output
            if output:
                st.text_area("Execution Output:", output, height=200)
            else:
                st.success("Code executed successfully with no output.")

            # Compare the output to the expected output (if available)
            if "selected_expected_output" in st.session_state:
                expected = st.session_state["selected_expected_output"].strip("Output: ")
                if output == expected:
                    st.success("🎉 Correct solution!")

                    # Save the submission
                    submission_data = {
                        "user_id": user_id,
                        "assessment_id": st.session_state["selected_problem_id"],
                        "career_path_id": career_path_id,
                        "submitted_code": code,
                        "execution_result": output,
                        "status": "correct"
                    }
                    try:
                        response = requests.post(SAVE_SUBMISSION_API, json=submission_data)
                        response.raise_for_status()
                        st.success("✅ Your submission was saved successfully!")
                    except requests.exceptions.RequestException as e:
                        st.error(f"❌ Failed to save submission: {e}")
                        logger.error(f"Error saving submission: {e}, Data: {submission_data}")

                    # Update career progress
                    try:
                        progress_data = {"career_path_id": 1, "progress_increment": 5.0}
                        response = requests.put(UPDATE_PROGRESS_API, json=progress_data)
                        response.raise_for_status()
                        st.success("✅ Career progress updated by 5%!")
                    except requests.exceptions.RequestException as e:
                        st.error(f"❌ Failed to update career progress: {e}")
                        logger.error(f"Error updating career progress: {e}, Data: {progress_data}")
                else:
                    st.error(f"❌ Incorrect solution. Expected: `{expected}`, but got: `{output}`")
                    logger.info(f"Incorrect solution. Expected: {expected}, Got: {output}")
        except Exception as e:
            # Handle errors gracefully
            st.error(f"Error: {e}")
            logger.error(f"Code execution error: {e}")
        finally:
            # Restore original stdout
            sys.stdout = old_stdout

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
