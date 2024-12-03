import logging
import streamlit as st
from modules.nav import SideBarLinks

# Configure logger
logger = logging.getLogger(__name__)

# Set page configuration
st.set_page_config(page_title="User Dashboard", layout="wide")

# Show appropriate sidebar links for the current user's role
SideBarLinks()

# Main header
st.markdown(f"""
# 👋 Welcome back, {st.session_state.get('first_name', 'User')}!
""")
st.write("### Your personalized dashboard to track progress and explore opportunities.")

# Divider for clarity
st.markdown("---")

# Layout for the action buttons
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏆 View Career Progress")
    st.write("Track your career development and see the skills you've mastered.")
    if st.button('Launch Career Progress Tracker', type='primary'):
        st.switch_page('pages/11_Career_Progress.py')

with col2:
    st.markdown("### 📚 View Academic Progress")
    st.write("Monitor your academic growth and assess your learning journey.")
    if st.button('Launch Academic Progress Tracker', type='primary'):
        st.switch_page('pages/12_Academic_Progress.py')

# Add an interactive section for user guidance
st.markdown("---")
st.markdown("## 💡 Explore More")
st.write("Choose from the following options to enhance your experience:")

# Columns for additional resources or actions
col3, col4 = st.columns(2)

with col3:
    st.markdown("### 🔗 Useful Links")
    st.write("- [Explore Career Resources](#)")
    st.write("- [Skill Development Tools](#)")
    st.write("- [Professional Networking Tips](#)")

with col4:
    st.markdown("### 📞 Get Support")
    st.write("- [Contact Academic Advisors](#)")
    st.write("- [Frequently Asked Questions (FAQ)](#)")
    st.write("- [Join the Community Forum](#)")

# Footer for branding and user support
st.markdown("---")
st.markdown("""
<small>
    Built with ❤️ using Streamlit | [Privacy Policy](#) | [Terms of Use](#)
</small>
""", unsafe_allow_html=True)
