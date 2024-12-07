# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")




#--------------- Role of a job market enthusiast-------------
def JobFanHomeNav():
    st.sidebar.page_link("pages/00_jobmarket_home.py", label= "job market homepage", icon="🏠")
def SkillsNav():
    st.sidebar.page_link("pages/01_indemand_skills.py", label="View Skills in Demand", icon="📊")
def CareerNav():
    st.sidebar.page_link("pages/02_InDemand_Careers.py", label="Explore Roles & Salaries", icon="🔍")
def CareerSkillNav():
    st.sidebar.page_link("pages/03_career_skills.py", label="Explore Careers and their Required Skills", icon="🌍")


#### ------------------------ Role of User Dashboard ------------------------

# Links for User Dashboard Page
def UserDashHomeNav():
    st.sidebar.page_link("pages/10_userdash_home.py", label="User Dashboard", icon="🏠")

def CareerProgressNav():
    st.sidebar.page_link("pages/11_career_progression.py", label="Career Progress Dashboard", icon="🚀")

def AcademicProgressNav():
    st.sidebar.page_link("pages/13_Academic_Progress.py", label="Academic Progress Dashboard", icon="📚")

# Links for Career Progress Page
def CodingChallengesNav():
    st.sidebar.page_link("pages/12_CodingQuestions.py", label="Explore Coding Challenges", icon="🧑‍💻")

def UpdateCareerPathNav():
    st.sidebar.page_link("pages/14_CareerUpdate.py", label="Update Careers Goals", icon="🧑‍💻")



##------------------------Role of a System Admin-------------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon="🖥️")


def ManageCoursesNav():
    st.sidebar.page_link("pages/22_CourseInfoAdmin.py", label="Manage Courses", icon="📚")


def ManageUsersNav():
    st.sidebar.page_link("pages/21_UserInfoAdmin.py", label="Manage User Information", icon="👥")


def ManageSkillsNav():
    st.sidebar.page_link("pages/23_SkillsInfoAdmin.py", label="Manage Skills", icon="💼")


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # Display "ALGONAUTS" text above the logo
    st.sidebar.markdown("## ALGONAUTS ")

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:
        #show the page links if user is a job market enthusiast
        if st.session_state["role"]== "Job Market Enthusiast":
            JobFanHomeNav()
            SkillsNav()
            CareerNav()
            CareerSkillNav()

            # Role-specific logic
        if st.session_state["role"] == "CS Student":
            current_page = st.session_state.get("current_page", "User Dashboard")
            if current_page == "User Dashboard":
                UserDashHomeNav()
                CareerProgressNav()
                AcademicProgressNav()
            elif current_page == "Career Progress Dashboard":
                UserDashHomeNav()
                CareerProgressNav()
                CodingChallengesNav()
                UpdateCareerPathNav()
            elif current_page == "Academic Progress Dashboard":
                UserDashHomeNav()
                AcademicProgressNav()

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "administrator":
            AdminPageNav()
            ManageCoursesNav()
            ManageUsersNav()
            ManageSkillsNav()


    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
