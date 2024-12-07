Algonauts Database Schema
Overview
The Algonauts database is a relational database designed to support the application’s core functionalities, including career tracking, academic progress monitoring, and skill mapping. This database uses MySQL with multiple interrelated tables to handle user data, academic courses, career paths, technical skills, assessments, and more.

The schema ensures data integrity and facilitates CRUD operations through foreign key constraints and relationships.

Key Features
Career Path Mapping:

Links career paths to required skills and academic courses.
Tracks user progress in career goals.
Academic Progress Tracking:

Maps courses to technical skills.
Tracks user progress in courses (completed, in-progress, or not-started).
Handles course prerequisites and academic concentrations.
Technical Skills:

Provides insights into skill complexity, categories, and popularity.
Tracks user-acquired skills and proficiency levels.
Coding Assessments:

Includes problems with input-output examples and tracks user submissions.
Maps assessments to specific career paths.
Job Market Insights:

Provides industry trends, required skills, and related job titles.
Schema Overview
The database contains the following main entities:

1. Users
Tracks user information, coding submissions, skills, and career progress.
Key Table: Users.
2. Academic Courses
Stores academic course information, including department, course number, and prerequisites.
Key Tables: AcademicCourses, CoursePrerequisites.
3. Technical Skills
Tracks technical skills and their mapping to courses and career paths.
Key Tables: TechSkills, CourseTechSkills, CareerPathSkills.
4. Career Paths
Tracks career paths, required skills, courses, and user progress.
Key Tables: CareerPaths, CareerPathCourses, CareerPathAssessments, UserCareerProgress.
5. Coding Assessments
Includes coding challenges and user submissions.
Key Tables: CodingAssessments, UserCodingSubmissions.
6. Academic Programs
Tracks academic programs, required courses, and concentrations.
Key Tables: AcademicPrograms, RequiredCourses, AcademicConcentrations.
7. Job Market Insights
Provides insights into job roles, skills, and industry trends.
Key Table: JobMarketInsights.
Schema Details
1. Users
Column	Type	Description
user_id	INT (Primary Key)	Unique user identifier.
name	VARCHAR(100)	User's name.
email	VARCHAR(100) (Unique)	User's email.
year	INT	Year of study (default: 0).
plan_id	INT	Academic plan ID.
2. Academic Courses
Column	Type	Description
department	VARCHAR(10)	Department offering the course (e.g., CS).
course_number	VARCHAR(10)	Course number (e.g., 2500).
course_name	VARCHAR(200)	Name of the course.
credits	INT	Number of credits.
3. Tech Skills
Column	Type	Description
tech_skill_id	INT (Primary Key)	Unique skill identifier.
skill_name	VARCHAR(100)	Name of the skill.
complexity	ENUM	Skill complexity (Beginner, Intermediate, Advanced).
4. Career Paths
Column	Type	Description
career_path_id	INT (Primary Key)	Unique identifier for a career path.
career_name	VARCHAR(100)	Name of the career path.
description	TEXT	Detailed description of the career.
salary	INT	Average salary in USD.
demand	DECIMAL(2, 1)	Demand rating (e.g., 4.5 out of 5).
5. Coding Assessments
Column	Type	Description
assessment_id	INT (Primary Key)	Unique identifier for the assessment.
problem_statement	TEXT	Description of the coding problem.
input_example	TEXT	Example input for the problem.
expected_output	TEXT	Expected output for the problem.
6. Relationships
Table	Relationship	Description
CareerPathCourses	Maps CareerPaths to AcademicCourses.	Courses needed for a career path.
CourseTechSkills	Maps AcademicCourses to TechSkills.	Skills taught in a course.
UserCareerProgress	Tracks user progress in career paths.	Career path tracking.
UserCourseProgress	Tracks user progress in courses.	Academic tracking.
UserSkills	Tracks skills acquired by users.	Skill acquisition tracking.
Setup Instructions
Database Creation:

Use the provided SQL script to create the schema.
Run:
sql
Copy code
CREATE DATABASE algonauts_db;
USE algonauts_db;
Import Schema:

Execute the schema script:
sql
Copy code
SOURCE schema.sql;
Seed Data:

Use tools like Mockaroo or Faker to generate realistic data.
Insert the data using INSERT statements or a seed.sql file.
Connect Application:

Configure the database connection in the .env file used by the Flask backend.
Future Enhancements
Add additional indexes for faster querying.
Implement stored procedures for complex operations.
Include database views for aggregated data (e.g., career demand trends).