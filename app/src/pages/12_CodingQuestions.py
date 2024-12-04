import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Coding Problems", layout="wide")

# Page header
st.markdown("# 🧩 Interactive Coding Problems")
st.markdown("### Choose a problem to solve and boost your skills!")


# Function to fetch coding problems
def fetch_coding_problems():
    api_url = "http://api:4000/ass/all_assessments"
    try:
        with st.spinner("Fetching coding problems..."):
            response = requests.get(api_url, timeout=10)  # 10-second timeout
            response.raise_for_status()
            data = response.json()
            if "data" in data:
                return data["data"]
            else:
                st.error("Unexpected API response format.")
                return []
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Unable to fetch coding problems: {e}")
        return []


# Fetch coding problems
problems = fetch_coding_problems()

# Display problems as buttons
if problems:
    st.markdown("### 📝 Available Coding Problems")
    for problem in problems:
        problem_id = problem.get("assessment_id", "Unknown ID")
        problem_statement = problem.get("problem_statement", "No description available")

        # Display each problem as a button
        if st.button(problem_statement, key=f"problem_{problem_id}"):
            # Redirect to the IDE page with the selected problem ID as a query parameter
            st.experimental_set_query_params(problem_id=problem_id)
            st.success(f"Redirecting to the IDE for Problem ID: {problem_id}")
            st.experimental_rerun()
else:
    st.info("🚧 **No coding problems available at the moment. Please check back later!**", icon="🛠️")

# Footer for branding
st.markdown("---")
st.markdown("""
<small>
    Built with ❤️ using Streamlit | [Privacy Policy](#) | [Terms of Use](#)
</small>
""", unsafe_allow_html=True)
