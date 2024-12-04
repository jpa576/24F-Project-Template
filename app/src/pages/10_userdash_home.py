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

# Career Progress Button
with col1:
    st.markdown("### 🏆 View Career Progress")
    st.write("Track your career development and see the skills you've mastered.")
    if st.button('Launch Career Progress Tracker', type='primary'):
        # Correct file name/path for Career Progression Page
        st.switch_page('11_career_progression')

# Academic Progress Button
with col2:
    st.markdown("### 📚 View Academic Progress")
    st.write("Monitor your academic growth and assess your learning journey.")
    if st.button('Launch Academic Progress Tracker', type='primary'):
        # Correct file name/path for Academic Progression Page
        st.switch_page('12_Academic_Progress')

# Add an interactive section for user guidance
st.markdown("---")
st.markdown("## 💡 Explore More")
st.write("Choose from the following options to enhance your experience:")

# Columns for additional resources or actions
col3, col4 = st.columns(2)

# Useful Links
with col3:
    st.markdown("### 🔗 Useful Links")
    st.markdown(
        '<a href="https://careers.northeastern.edu" target="_blank" style="text-decoration:none;">'
        '<button style="background-color:#4CAF50; color:white; border:none; padding:10px 20px; '
        'text-align:center; text-decoration:none; display:inline-block; font-size:16px; margin:4px 2px; '
        'cursor:pointer; border-radius:4px;">Explore Career Resources</button></a>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<a href="https://www.kaggle.com/learn" target="_blank" style="text-decoration:none;">'
        '<button style="background-color:#4CAF50; color:white; border:none; padding:10px 20px; '
        'text-align:center; text-decoration:none; display:inline-block; font-size:16px; margin:4px 2px; '
        'cursor:pointer; border-radius:4px;">Skill Development Tools</button></a>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<a href="https://blog.linkedin.com/professional-networking-tips" target="_blank" style="text-decoration:none;">'
        '<button style="background-color:#4CAF50; color:white; border:none; padding:10px 20px; '
        'text-align:center; text-decoration:none; display:inline-block; font-size:16px; margin:4px 2px; '
        'cursor:pointer; border-radius:4px;">Professional Networking Tips</button></a>',
        unsafe_allow_html=True
    )

# Get Support Links
with col4:
    st.markdown("### 📞 Get Support")
    st.markdown(
        '<a href="https://www.northeastern.edu/cs/advising/" target="_blank" style="text-decoration:none;">'
        '<button style="background-color:#4CAF50; color:white; border:none; padding:10px 20px; '
        'text-align:center; text-decoration:none; display:inline-block; font-size:16px; margin:4px 2px; '
        'cursor:pointer; border-radius:4px;">Contact Academic Advisors</button></a>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<a href="https://www.reddit.com/r/learnprogramming" target="_blank" style="text-decoration:none;">'
        '<button style="background-color:#4CAF50; color:white; border:none; padding:10px 20px; '
        'text-align:center; text-decoration:none; display:inline-block; font-size:16px; margin:4px 2px; '
        'cursor:pointer; border-radius:4px;">Join the Community Forum</button></a>',
        unsafe_allow_html=True
    )

# Footer for branding and user support
st.markdown("---")
st.markdown("""
<small>
    Built with ❤️ using Streamlit | [Privacy Policy](#) | [Terms of Use](#)
</small>
""", unsafe_allow_html=True)
