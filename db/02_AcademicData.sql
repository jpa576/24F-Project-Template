use algonauts_db;
##----------------------------------insert statements for cs academic courses------------------------------------
INSERT INTO AcademicCourses (department, course_number, course_name, course_description, credits) VALUES
('CS', '1100', 'Computer Science and Its Applications', 'Introduces students to the field of computer science and the patterns of thinking that enable them to become intelligent users of software tools in a problem-solving setting.', 4),
('CS', '1200', 'First Year Seminar', 'An introductory seminar for first-year computer science students.', 1),
('CS', '1210', 'Professional Development for Khoury Co-op', 'Preparation for cooperative education experiences in computer science.', 1),
('CS', '1800', 'Discrete Structures', 'Introduces the mathematical structures and methods that form the foundation of computer science.', 4),
('CS', '1802', 'Seminar for CS 1800', 'Supplementary seminar accompanying CS 1800.', 1),
('CS', '2500', 'Fundamentals of Computer Science 1', 'Introduces the fundamental ideas of computing and the principles of programming.', 4),
('CS', '2501', 'Lab for CS 2500', 'Laboratory component for CS 2500.', 1),
('CS', '2510', 'Fundamentals of Computer Science 2', 'Continues CS 2500. Examines object-oriented programming and associated algorithms using more complex data structures as the focus.', 4),
('CS', '2511', 'Lab for CS 2510', 'Laboratory component for CS 2510.', 1),
('CS', '2800', 'Logic and Computation', 'Introduces formal logic and its connections to computer and information science.', 4),
('CS', '2810', 'Mathematics of Data Models', 'Studies methods and ideas in linear algebra, multivariable calculus, and statistics relevant for data modeling.', 4),
('CS', '3000', 'Algorithms and Data', 'Introduces the fundamental concepts of algorithms and data structures.', 4),
('CS', '3500', 'Object-Oriented Design', 'Covers the principles of object-oriented design and programming.', 4),
('CS', '3501', 'Lab for CS 3500', 'Laboratory component for CS 3500.', 1),
('CS', '3650', 'Computer Systems', 'Introduces the fundamental concepts of computer systems.', 4),
('CS', '3700', 'Networks and Distributed Systems', 'Introduces the fundamental concepts of computer networks and distributed systems.', 4),
('CS', '3800', 'Theory of Computation', 'Introduces the fundamental concepts of theoretical computer science.', 4),
('CS', '4500', 'Software Development', 'Principles and practices of software development.', 4),
('CS', '4530', 'Fundamentals of Software Engineering', 'Introduction to software engineering concepts and methodologies.', 4),
('CY', '2550', 'Foundations of Cybersecurity', 'Fundamental concepts in cybersecurity.', 4),
('CY', '3740', 'Systems Security', 'Study of security in computer systems.', 4),
('CY', '4740', 'Network Security', 'Principles and practices of network security.', 4);
-- Concentration in Artificial Intelligence
INSERT INTO AcademicCourses (department, course_number, course_name, course_description, credits) VALUES
('CS', '4100', 'Artificial Intelligence', 'Introduction to the principles and techniques of artificial intelligence.', 4),
('DS', '4400', 'Machine Learning and Data Mining 1', 'Fundamentals of machine learning and data mining techniques.', 4),
('CS', '4120', 'Natural Language Processing', 'Study of computational techniques for processing natural languages.', 4),
('CS', '4150', 'Game Artificial Intelligence', 'Application of AI techniques in game development.', 4),
('CS', '4610', 'Robotic Science and Systems', 'Exploration of robotic systems and their underlying science.', 4),
('DS', '4420', 'Machine Learning and Data Mining 2', 'Advanced topics in machine learning and data mining.', 4),
('IS', '4200', 'Information Retrieval', 'Techniques and models for retrieving information from large datasets.', 4);
-- Concentration in Foundations
INSERT INTO AcademicCourses (department, course_number, course_name, course_description, credits) VALUES
('CS', '4820', 'Computer-Aided Reasoning', 'Study of tools and techniques for automated reasoning.', 4),
('CS', '4805', 'Fundamentals of Complexity Theory', 'Analysis of computational complexity and related theories.', 4),
('CS', '4810', 'Advanced Algorithms', 'In-depth exploration of advanced algorithmic techniques.', 4),
('CS', '3950', 'Introduction to Computer Science Research', 'Preparation for research in computer science.', 4),
('CS', '4950', 'Computer Science Research Seminar', 'Seminar on current research topics in computer science.', 4),
('CS', '4830', 'System Specification, Verification, and Synthesis', 'Methods for specifying, verifying, and synthesizing systems.', 4),
('CY', '4770', 'Cryptography', 'Study of cryptographic techniques and their applications.', 4);
-- Concentration in Human-Centered Computing
INSERT INTO AcademicCourses (department, course_number, course_name, course_description, credits) VALUES
('IS', '4300', 'Human Computer Interaction', 'Design and evaluation of user interfaces.', 4),
('IS', '4800', 'Empirical Research Methods', 'Methods for conducting empirical research in information science.', 4),
('CS', '4520', 'Mobile Application Development', 'Techniques for developing applications on mobile platforms.', 4),
('CS', '4550', 'Web Development', 'Principles and practices of web application development.', 4),
('DS', '4200', 'Information Presentation and Visualization', 'Methods for presenting and visualizing information.', 4),
('IS', '2000', 'Principles of Information Science', 'Introduction to the field of information science.', 4);
-- Concentration in Software
INSERT INTO AcademicCourses (department, course_number, course_name, course_description, credits) VALUES
('CS', '4400', 'Programming Languages', 'Study of programming language concepts and paradigms.', 4),
('CS', '4700', 'Network Fundamentals', 'Introduction to computer networking principles.', 4),
('CS', '4730', 'Distributed Systems', 'Study of distributed computing systems and their design.', 4),
('CS', '3520', 'Programming in C++', 'Course on programming using the C++ language.', 4),
('CS', '4410', 'Compilers', 'Design and implementation of compilers.', 4);
-- Concentration in Systems
INSERT INTO AcademicCourses (department, course_number, course_name, course_description, credits) VALUES
#('CY', '4740', 'Network Security', 'Studies topics related to Internet architecture and cryptographic schemes in the context of security. Provides advanced coverage of major Internet protocols including IP and DNS. Examines denial of service, viruses, and worms, and discusses techniques for protection.', 4),
('CS', '4300', 'Computer Graphics', 'Charts a path through every major aspect of computer graphics with varying degrees of emphasis. Discusses hardware issues: size and speed; lines, polygons, and regions; modeling, or objects and their relations; viewing, or what can be seen (visibility and perspective); rendering, or how it looks (properties of surfaces, light, and color); transformations, or moving, placing, distorting, and animating; and interaction, or drawing, selecting, and transforming.', 4),
('CS', '4710', 'Mobile and Wireless Systems', 'Introduces the fundamental concepts of mobile and wireless computing systems, including architecture, protocols, and applications.', 4),
('CY', '4760', 'Security of Wireless and Mobile Systems', 'Explores security issues specific to wireless and mobile systems, including vulnerabilities, threats, and mitigation strategies.', 4);

##----------------------------------insert statements for BSCS AcademicProgram ------------------------------------
INSERT INTO AcademicPrograms (program_name, degree_type, department, description) VALUES
('Computer Science', 'BS', 'Khoury College', 'Bachelor of Science in Computer Science');

##----------------------------------insert statements for BSCS Concentrations ------------------------------------
-- Assuming program_id 1 corresponds to 'BSCS'
INSERT INTO AcademicConcentrations (program_id, concentration_name, description) VALUES
(1, 'Artificial Intelligence', 'Focuses on AI principles and applications.'),
(1, 'Foundations', 'Emphasizes theoretical aspects of computer science.'),
(1, 'Human-Centered Computing', 'Centers on the design and evaluation of interactive systems.'),
(1, 'Software', 'Concentrates on software development methodologies and practices.'),
(1, 'Systems', 'Deals with computer systems and networks.');



##----------------------------------insert statements for BSCS ConcentrationCourses ------------------------------------
-- Artificial Intelligence Concentration
-- Assuming concentration_id 1 corresponds to 'Artificial Intelligence'
INSERT INTO ConcentrationCourses (concentration_id, department, course_number) VALUES
(1, 'CS', '4100'),  -- Artificial Intelligence
(1, 'DS', '4400'),  -- Machine Learning and Data Mining 1
(1, 'CS', '4120'),  -- Natural Language Processing
(1, 'CS', '4150'),  -- Game Artificial Intelligence
(1, 'CS', '4610'),  -- Robotic Science and Systems
(1, 'DS', '4420'),  -- Machine Learning and Data Mining 2
(1, 'IS', '4200');  -- Information Retrieval

-- Foundations Concentration
-- Assuming concentration_id 2 corresponds to 'Foundations'
INSERT INTO ConcentrationCourses (concentration_id, department, course_number) VALUES
(2, 'CS', '2800'),  -- Logic and Computation
(2, 'CS', '4820'),  -- Computer-Aided Reasoning
(2, 'CS', '4805'),  -- Fundamentals of Complexity Theory
(2, 'CS', '4810'),  -- Advanced Algorithms
(2, 'CS', '3950'),  -- Introduction to Computer Science Research
(2, 'CS', '4950'),  -- Computer Science Research Seminar
(2, 'CS', '4830'),  -- System Specification, Verification, and Synthesis
(2, 'CY', '4770');  -- Cryptography

-- Human-Centered Computing Concentration
-- Assuming concentration_id 3 corresponds to 'Human-Centered Computing'
INSERT INTO ConcentrationCourses (concentration_id, department, course_number) VALUES
(3, 'IS', '4300'),  -- Human Computer Interaction
(3, 'IS', '4800'),  -- Empirical Research Methods
(3, 'CS', '4120'),  -- Natural Language Processing
(3, 'CS', '4520'),  -- Mobile Application Development
(3, 'CS', '4550'),  -- Web Development
(3, 'DS', '4200'),  -- Information Presentation and Visualization
(3, 'IS', '2000');  -- Principles of Information Science

-- Software Concentration
-- Assuming concentration_id 4 corresponds to 'Software'
INSERT INTO ConcentrationCourses (concentration_id, department, course_number) VALUES
(4, 'CS', '2800'),  -- Logic and Computation
(4, 'CS', '4400'),  -- Programming Languages
(4, 'CS', '4700'),  -- Network Fundamentals
(4, 'CS', '4730'),  -- Distributed Systems
(4, 'CS', '3520'),  -- Programming in C++
(4, 'CS', '4410'),  -- Compilers
(4, 'CS', '4550'),  -- Web Development
(4, 'CS', '4820'),  -- Computer-Aided Reasoning
(4, 'CS', '4830');  -- System Specification, Verification, and Synthesis

-- Systems Concentration
-- Assuming concentration_id 5 corresponds to 'Systems'
INSERT INTO ConcentrationCourses (concentration_id, department, course_number) VALUES
(5, 'CS', '4700'),  -- Network Fundamentals
(5, 'CS', '4730'),  -- Distributed Systems
(5, 'CY', '3740'),  -- Systems Security
(5, 'CY', '4740'),  -- Network Security
(5, 'CS', '3520'),  -- Programming in C++
(5, 'CS', '4300'),  -- Computer Graphics
(5, 'CS', '4610'),  -- Robotic Science and Systems
(5, 'CS', '4710'),  -- Mobile and Wireless Systems
(5, 'CY', '4760');  -- Security of Wireless and Mobile Systems
-- ---------INSERT FOR COURSE PREREQS
INSERT INTO CoursePrerequisites (department, course_number, prerequisite_department, prerequisite_number) VALUES
('CS', '1802', 'CS', '1800'),  -- Seminar for CS 1800 requires Discrete Structures
('CS', '2500', 'CS', '1800'),  -- Fundamentals of Computer Science 1 requires Discrete Structures
('CS', '2501', 'CS', '2500'),  -- Lab for CS 2500 requires Fundamentals of Computer Science 1
('CS', '2510', 'CS', '2500'),  -- Fundamentals of Computer Science 2 requires Fundamentals of Computer Science 1
('CS', '2511', 'CS', '2510'),  -- Lab for CS 2510 requires Fundamentals of Computer Science 2
('CS', '2800', 'CS', '1800'),  -- Logic and Computation requires Discrete Structures
('CS', '3000', 'CS', '2510'),  -- Algorithms and Data requires Fundamentals of Computer Science 2
('CS', '3500', 'CS', '2510'),  -- Object-Oriented Design requires Fundamentals of Computer Science 2
('CS', '3501', 'CS', '3500'),  -- Lab for CS 3500 requires Object-Oriented Design
('CS', '3650', 'CS', '2510'),  -- Computer Systems requires Fundamentals of Computer Science 2
('CS', '3700', 'CS', '3650'),  -- Networks and Distributed Systems requires Computer Systems
('CS', '3800', 'CS', '2800'),  -- Theory of Computation requires Logic and Computation
('CS', '4500', 'CS', '3500'),  -- Software Development requires Object-Oriented Design
('CS', '4530', 'CS', '3500'),  -- Fundamentals of Software Engineering requires Object-Oriented Design
('CY', '3740', 'CY', '2550'),  -- Systems Security requires Foundations of Cybersecurity
('CY', '4740', 'CY', '3740');  -- Network Security requires Systems Security


-- Insert mock data for career paths
-- Assuming career_path_id 1 is Software Engineer
INSERT INTO CareerPathCourses (career_path_id, department, course_number)
VALUES
(1, 'CS', '2500'), -- Fundamentals of Computer Science 1
(1, 'CS', '2510'), -- Fundamentals of Computer Science 2
(1, 'CS', '3000'), -- Algorithms and Data
(1, 'CS', '3500'), -- Object-Oriented Design
(1, 'CS', '4500'); -- Software Development

-- Assuming career_path_id 2 is Data Scientist
INSERT INTO CareerPathCourses (career_path_id, department, course_number)
VALUES
(2, 'CS', '1800'), -- Discrete Structures
(2, 'CS', '3000'), -- Algorithms and Data
(2, 'DS', '4400'), -- Machine Learning and Data Mining 1
(2, 'DS', '4420'), -- Machine Learning and Data Mining 2
(2, 'CS', '4100'); -- Artificial Intelligence


-- Add additional required courses for Software Engineer
INSERT INTO CareerPathCourses (career_path_id, department, course_number)
VALUES
(1, 'CS', '3650'), -- Computer Systems (Example additional required course)
(1, 'CS', '3700'); -- Networks and Distributed Systems

-- Add additional required courses for Data Scientist
INSERT INTO CareerPathCourses (career_path_id, department, course_number)
VALUES
(2, 'CS', '2800'), -- Logic and Computation (Example additional required course)
(2, 'CS', '4820'); -- Computer-Aided Reasoning