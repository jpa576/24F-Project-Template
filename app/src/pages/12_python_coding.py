import streamlit as st
import sys
from io import StringIO
import sqlite3

# Database connection setup (update connection details if necessary)
DB_FILE = "path_to_your_database.db"  # Update this with the actual database path

def fetch_random_python_question():
    try:
        # Connect to the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Fetch a random Python-related interview question
        query = """
        SELECT question, difficulty
        FROM InterviewQuestions
        WHERE skill LIKE '%Python%'
        ORDER BY RANDOM()
        LIMIT 1;
        """
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()

        return result if result else ("No Python-related questions found.", "N/A")
    except Exception as e:
        return (f"Error fetching question: {e}", "Error")

# Set page configuration
st.set_page_config(page_title="Python IDE", layout="wide")

# Header
st.markdown("# 🐍 Python IDE")
st.write("Write your Python script below, click Run, and see the results in real-time!")

# Display a random Python-related question
st.markdown("### 🧠 Interview Question")
question, difficulty = fetch_random_python_question()
if difficulty != "Error":
    st.write(f"**Difficulty**: {difficulty}")
    st.write(f"**Question**: {question}")
else:
    st.error(question)

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
