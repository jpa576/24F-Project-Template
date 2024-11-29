USE algonauts_db;

-- Step 1: Insert Career Paths
INSERT INTO CareerPaths (path_name, description) VALUES
('Artificial Intelligence Developer', 'Focuses on designing and implementing AI systems.'),
('Data Scientist', 'Specializes in analyzing and interpreting complex data.'),
('Software Engineer', 'Develops software solutions and systems.'),
('Cybersecurity Analyst', 'Focuses on securing networks and systems against cyber threats.'),
('Cloud Computing Specialist', 'Works with cloud-based systems and architecture.'),
('Full-Stack Developer', 'Develops both frontend and backend applications.'),
('DevOps Engineer', 'Specializes in CI/CD pipelines and system automation.'),
('Mobile Application Developer', 'Designs and develops applications for mobile platforms.'),
('Game Developer', 'Creates games using engines and graphics libraries.'),
('Robotics Engineer', 'Designs robotic systems with control and automation.');

-- Step 2: Map Career Paths to Courses
-- Ensure course_id values match actual course IDs in AcademicCourses table
INSERT INTO CareerPathCourses (path_id, course_id) VALUES
-- Artificial Intelligence Developer
(1, 1), -- Introduction to Artificial Intelligence
(1, 2), -- Machine Learning
(1, 3), -- Data Structures and Algorithms
(1, 4), -- Probability and Statistics

-- Data Scientist
(2, 5), -- Data Mining
(2, 6), -- Database Management Systems
(2, 7), -- Statistical Methods in Data Science
(2, 8), -- Big Data Analytics

-- Software Engineer
(3, 9), -- Object-Oriented Programming
(3, 10), -- Software Development Methodologies
(3, 11), -- Operating Systems
(3, 12), -- Computer Networks

-- Cybersecurity Analyst
(4, 13), -- Introduction to Cybersecurity
(4, 14), -- Network Security
(4, 15), -- Cryptography
(4, 16), -- Ethical Hacking

-- Cloud Computing Specialist
(5, 17), -- Cloud Computing Architecture
(5, 18), -- Distributed Systems
(5, 19), -- Web Services and APIs
(5, 20), -- Virtualization Technologies

-- Full-Stack Developer
(6, 21), -- Web Development
(6, 22), -- Database Systems
(6, 23), -- User Interface Design
(6, 24), -- Server-Side Programming

-- DevOps Engineer
(7, 25), -- Systems Administration
(7, 26), -- Continuous Integration and Deployment
(7, 27), -- Infrastructure as Code
(7, 28), -- Monitoring and Logging

-- Mobile Application Developer
(8, 29), -- Mobile App Development
(8, 30), -- Human-Computer Interaction
(8, 31), -- Software Engineering
(8, 32), -- Embedded Systems

-- Game Developer
(9, 33), -- Game Design and Development
(9, 34), -- Computer Graphics
(9, 35), -- Artificial Intelligence for Games
(9, 36), -- Physics Simulation

-- Robotics Engineer
(10, 37), -- Introduction to Robotics
(10, 38), -- Control Systems
(10, 39), -- Embedded Systems
(10, 40); -- Machine Learning

-- Step 3: Map Career Paths to Skills
-- Ensure skill_id values match actual skill IDs in TechSkills table
INSERT INTO CareerPathSkills (path_id, skill_id) VALUES
-- Artificial Intelligence Developer
(1, 1), -- Python
(1, 2), -- R
(1, 3), -- TensorFlow
(1, 4), -- PyTorch

-- Data Scientist
(2, 5), -- Python
(2, 6), -- SQL
(2, 7), -- Data Visualization
(2, 8), -- Statistical Analysis

-- Software Engineer
(3, 9), -- Java
(3, 10), -- C++
(3, 11), -- SDLC
(3, 12), -- Git

-- Cybersecurity Analyst
(4, 13), -- Network Security
(4, 14), -- Threat Assessment
(4, 15), -- Ethical Hacking Tools
(4, 16), -- Regulatory Compliance

-- Cloud Computing Specialist
(5, 17), -- AWS
(5, 18), -- Azure
(5, 19), -- Docker
(5, 20), -- Kubernetes

-- Full-Stack Developer
(6, 21), -- HTML
(6, 22), -- CSS
(6, 23), -- JavaScript
(6, 24), -- Node.js

-- DevOps Engineer
(7, 25), -- Jenkins
(7, 26), -- Ansible
(7, 27), -- CI/CD Pipelines
(7, 28), -- Bash Scripting

-- Mobile Application Developer
(8, 29), -- Swift
(8, 30), -- Kotlin
(8, 31), -- React Native
(8, 32), -- Mobile UI/UX Design

-- Game Developer
(9, 33), -- Unity
(9, 34), -- Unreal Engine
(9, 35), -- Game Mechanics
(9, 36), -- 3D Modeling

-- Robotics Engineer
(10, 37), -- C++
(10, 38), -- Python
(10, 39), -- Robotics Operating Systems
(10, 40); -- Sensor Integration
