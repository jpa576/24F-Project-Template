-- Create the CareerPaths table
CREATE TABLE IF NOT EXISTS CareerPaths (
    path_id INT AUTO_INCREMENT PRIMARY KEY,
    path_name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);

-- Create the CareerPathCourses table to link career paths to courses
CREATE TABLE IF NOT EXISTS CareerPathCourses (
    path_id INT NOT NULL,
    course_id INT NOT NULL,
    PRIMARY KEY (path_id, course_id),
    FOREIGN KEY (path_id) REFERENCES CareerPaths(path_id),
    FOREIGN KEY (course_id) REFERENCES AcademicCourses(course_id)
);

-- Create the CareerPathSkills table to link career paths to skills
CREATE TABLE IF NOT EXISTS CareerPathSkills (
    path_id INT NOT NULL,
    skill_id INT NOT NULL,
    PRIMARY KEY (path_id, skill_id),
    FOREIGN KEY (path_id) REFERENCES CareerPaths(path_id),
    FOREIGN KEY (skill_id) REFERENCES TechSkills(skill_id)
);

-- Insert Career Paths
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

-- Map Career Paths to Courses
INSERT INTO CareerPathCourses (path_id, course_id) VALUES
-- Artificial Intelligence Developer
(1, 101), -- Introduction to Artificial Intelligence
(1, 102), -- Machine Learning
(1, 103), -- Data Structures and Algorithms
(1, 104), -- Probability and Statistics

-- Data Scientist
(2, 201), -- Data Mining
(2, 202), -- Database Management Systems
(2, 203), -- Statistical Methods in Data Science
(2, 204), -- Big Data Analytics

-- Software Engineer
(3, 301), -- Object-Oriented Programming
(3, 302), -- Software Development Methodologies
(3, 303), -- Operating Systems
(3, 304), -- Computer Networks

-- Cybersecurity Analyst
(4, 401), -- Introduction to Cybersecurity
(4, 402), -- Network Security
(4, 403), -- Cryptography
(4, 404), -- Ethical Hacking

-- Cloud Computing Specialist
(5, 501), -- Cloud Computing Architecture
(5, 502), -- Distributed Systems
(5, 503), -- Web Services and APIs
(5, 504), -- Virtualization Technologies

-- Full-Stack Developer
(6, 601), -- Web Development
(6, 602), -- Database Systems
(6, 603), -- User Interface Design
(6, 604), -- Server-Side Programming

-- DevOps Engineer
(7, 701), -- Systems Administration
(7, 702), -- Continuous Integration and Deployment
(7, 703), -- Infrastructure as Code
(7, 704), -- Monitoring and Logging

-- Mobile Application Developer
(8, 801), -- Mobile App Development
(8, 802), -- Human-Computer Interaction
(8, 803), -- Software Engineering
(8, 804), -- Embedded Systems

-- Game Developer
(9, 901), -- Game Design and Development
(9, 902), -- Computer Graphics
(9, 903), -- Artificial Intelligence for Games
(9, 904), -- Physics Simulation

-- Robotics Engineer
(10, 1001), -- Introduction to Robotics
(10, 1002), -- Control Systems
(10, 1003), -- Embedded Systems
(10, 1004); -- Machine Learning

-- Map Career Paths to Skills
INSERT INTO CareerPathSkills (path_id, skill_id) VALUES
-- Artificial Intelligence Developer
(1, 1), -- Python
(1, 2), -- R
(1, 3), -- TensorFlow
(1, 4), -- PyTorch

-- Data Scientist
(2, 1), -- Python
(2, 5), -- SQL
(2, 6), -- Data Visualization
(2, 7), -- Statistical Analysis

-- Software Engineer
(3, 8), -- Java
(3, 9), -- C++
(3, 10), -- SDLC
(3, 11), -- Git

-- Cybersecurity Analyst
(4, 12), -- Network Security
(4, 13), -- Threat Assessment
(4, 14), -- Ethical Hacking Tools
(4, 15), -- Regulatory Compliance

-- Cloud Computing Specialist
(5, 16), -- AWS
(5, 17), -- Azure
(5, 18), -- Docker
(5, 19), -- Kubernetes

-- Full-Stack Developer
(6, 20), -- HTML
(6, 21), -- CSS
(6, 22), -- JavaScript
(6, 23), -- Node.js

-- DevOps Engineer
(7, 24), -- Jenkins
(7, 25), -- Ansible
(7, 26), -- CI/CD Pipelines
(7, 27), -- Bash Scripting

-- Mobile Application Developer
(8, 28), -- Swift
(8, 29), -- Kotlin
(8, 30), -- React Native
(8, 31), -- Mobile UI/UX Design

-- Game Developer
(9, 32), -- Unity
(9, 33), -- Unreal Engine
(9, 34), -- Game Mechanics
(9, 35), -- 3D Modeling

-- Robotics Engineer
(10, 36), -- C++
(10, 37), -- Python
(10, 38), -- Robotics Operating Systems
(10, 39); -- Sensor Integration
