import streamlit as st
import sys
from io import StringIO

# Set page configuration
st.set_page_config(page_title="Python IDE", layout="wide")

# Header
st.markdown("# 🐍 Python IDE")
st.write("Write your Python script below, click Run, and see the results in real-time!")

# Check if problem details are passed via `st.session_state`
if "selected_problem_id" in st.session_state:
    problem_statement = st.session_state.get("selected_problem_title", "No problem selected.")
    input_example = st.session_state.get("selected_input_example", "No input example.")
    expected_output = st.session_state.get("selected_expected_output", "No expected output.")

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
            output = sys.stdout.getvalue()

            # Display the output
            if output:
                st.text_area("Execution Output:", output, height=200)
            else:
                st.success("Code executed successfully with no output.")

            # Compare the output to the expected output (if available)
            if "selected_expected_output" in st.session_state:
                expected = st.session_state["selected_expected_output"].strip("Output: ")
                if output.strip() == expected:
                    st.success("🎉 Correct solution!")
                else:
                    st.error(f"❌ Incorrect solution. Expected: `{expected}`")
        except Exception as e:
            # Handle errors gracefully
            st.error(f"Error: {e}")
        finally:
            # Restore original stdout
            sys.stdout = old_stdout
