import streamlit as st
import networkx as nx
from pyvis.network import Network

# Set up page configuration
st.set_page_config(layout="wide")

# Header
st.title("Course Progression")
st.subheader("Courses for Career Path: AI Development")

# Placeholder Function for Courses Data
# Your partner can replace this with the actual database call
def get_courses_mock():
    return [
        {"course_name": "Intro to AI", "prerequisite": None},
        {"course_name": "ML Basics", "prerequisite": "Intro to AI"},
        {"course_name": "Deep Learning", "prerequisite": "ML Basics"},
        {"course_name": "Algorithms", "prerequisite": "Intro to AI"},
    ]

# Fetch mock data for now
courses = get_courses_mock()

# Build Course Roadmap
graph = nx.DiGraph()
for course in courses:
    if course["prerequisite"]:
        graph.add_edge(course["prerequisite"], course["course_name"])
    else:
        graph.add_node(course["course_name"])

# Render the roadmap using Pyvis
st.write("### Course Roadmap")
net = Network(notebook=True, height="400px", width="100%")
net.from_nx(graph)
net.show("course_roadmap.html")
st.components.v1.html(open("course_roadmap.html", "r").read(), height=500)

# Back Button
if st.button("Back to Home"):
    st.experimental_set_query_params(page="ambitious_student_home")
    st.stop()
