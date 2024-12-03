import streamlit as st
import sys
from io import StringIO

# Set page configuration
st.set_page_config(page_title="Python IDE", layout="wide")

# Header
st.markdown("# 🐍 Python IDE")
st.write("Write your Python script below, click Run, and see the results in real-time!")

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
            exec(code)
            # Capture and display the output
            output = sys.stdout.getvalue()
            if output:
                st.text_area("Execution Output:", output, height=200)
            else:
                st.success("Code executed successfully with no output.")
        except Exception as e:
            # Handle errors gracefully
            st.error(f"Error: {e}")
        finally:
            # Restore original stdout
            sys.stdout = old_stdout
