# Algonauts 🚀
# CS 3200 Semester Project | Fall 2024
# Demo Link: https://www.dropbox.com/scl/fi/3icrrthkafg9ftjaeplwp/cs3200-algonauts_demo-Made-with-Clipchamp.mp4?rlkey=gi7wxm9aoj036qwv2g3cw9m9p&st=b4newnn5&dl=0
# Overview
Algonauts is a career exploration and skill development platform designed to empower users by:

Tracking academic and career progress.
Gaining insights into job market trends.
Developing in-demand technical skills.
The project combines:

A Streamlit-based frontend for a user-friendly experience.
A Flask REST API backend to manage resources and operations.
A Dockerized environment for easy deployment and scalability.
Features
For Students
Personalized Dashboard: Track your academic achievements and career progress.
Career Pathway Management: Add, remove, and update career goals.
Skill Development Resources: Gain insights into in-demand skills.
For Job Market Enthusiasts
In-Demand Skills Insights: Explore top skills ranked by demand.
Salary Trends & Role Insights: Analyze job roles and salary data.
For System Administrators
Administrative Tools:
Manage users, roles, and permissions.
Maintain course and skill data integrity.
Setup Instructions
Secrets Configuration
Add a .env file in the root directory with the following secrets and configuration values:

# Security Keys
SECRET_KEY=someCrazyS3cR3T!Key.!


# MySQL Database Configuration
MYSQL_USER=algonauts_user
MYSQL_PASSWORD=algonauts_password
MYSQL_HOST=algonauts_mysql
MYSQL_PORT=3306
MYSQL_DATABASE=algonauts_db
MYSQL_ROOT_PASSWORD=root_password