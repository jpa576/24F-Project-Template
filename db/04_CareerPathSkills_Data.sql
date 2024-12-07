use algonauts_db;
describe CareerPathSkills;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance) VALUES
(1, 1, 95.00),  -- Software Engineer - Programming Fundamentals
(1, 2, 90.00),  -- Software Engineer - Data Structures
(1, 3, 88.00),  -- Software Engineer - Algorithmic Thinking
(1, 4, 85.00),  -- Software Engineer - Object-Oriented Programming
(1, 5, 80.00),  -- Software Engineer - Software Design Patterns

(2, 6, 95.00),  -- Data Scientist - Data Analysis
(2, 7, 90.00),  -- Data Scientist - Machine Learning
(2, 8, 88.00),  -- Data Scientist - Statistics
(2, 1, 85.00),  -- Data Scientist - Programming Fundamentals
(2, 3, 80.00),  -- Data Scientist - Algorithmic Thinking

(3, 9, 95.00),  -- Cybersecurity Analyst - Cybersecurity Principles
(3, 10, 90.00), -- Cybersecurity Analyst - Threat Analysis
(3, 11, 88.00), -- Cybersecurity Analyst - Network Defense
(3, 12, 85.00), -- Cybersecurity Analyst - System Vulnerability Assessment
(3, 13, 80.00), -- Cybersecurity Analyst - Cryptography

(4, 7, 95.00),  -- AI/ML Engineer - Machine Learning
(4, 14, 90.00), -- AI/ML Engineer - AI Algorithms
(4, 1, 88.00),  -- AI/ML Engineer - Programming Fundamentals
(4, 6, 85.00),  -- AI/ML Engineer - Data Analysis
(4, 3, 80.00),  -- AI/ML Engineer - Algorithmic Thinking

(5, 15, 95.00), -- Web Developer - HTML
(5, 16, 90.00), -- Web Developer - CSS
(5, 17, 88.00), -- Web Developer - JavaScript
(5, 1, 85.00),  -- Web Developer - Programming Fundamentals
(5, 4, 80.00),  -- Web Developer - Object-Oriented Programming

(6, 18, 95.00), -- Mobile App Developer - Java
(6, 19, 90.00), -- Mobile App Developer - Swift
(6, 20, 88.00), -- Mobile App Developer - Kotlin
(6, 1, 85.00),  -- Mobile App Developer - Programming Fundamentals
(6, 4, 80.00),  -- Mobile App Developer - Object-Oriented Programming

(7, 21, 90.00), -- Cloud Engineer - Networking Protocols
(7, 22, 88.00), -- Cloud Engineer - System Architecture
(7, 9, 85.00),  -- Cloud Engineer - Cybersecurity Principles
(7, 1, 80.00),  -- Cloud Engineer - Programming Fundamentals
(7, 23, 75.00), -- Cloud Engineer - Operating Systems

(8, 24, 95.00), -- DevOps Engineer - Software Development Life Cycle
(8, 21, 90.00), -- DevOps Engineer - Networking Protocols
(8, 22, 88.00), -- DevOps Engineer - System Architecture
(8, 1, 85.00),  -- DevOps Engineer - Programming Fundamentals
(8, 23, 80.00) -- DevOps Engineer - Operating Systems
ON DUPLICATE KEY UPDATE relevance = VALUES(relevance);;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance) VALUES
    (9, 20, 95.00), -- Network Administrator - Networking Protocols
    (9, 22, 90.00), -- Network Administrator - Network Defense
    (9, 24, 88.00), -- Network Administrator - System Vulnerability Assessment
    (9, 23, 85.00), -- Network Administrator - Operating Systems
    (9, 1, 80.00),  -- Network Administrator - Problem Solving
    (10, 12, 95.00),-- Database Administrator - SQL
    (10, 6, 90.00), -- Database Administrator - Data Structures
    (10, 9, 88.00), -- Database Administrator - Data Analysis
    (10, 1, 85.00), -- Database Administrator - Problem Solving
    (10, 2, 80.00) -- Database Administrator - Programming Fundamentals
    ON DUPLICATE KEY UPDATE relevance = VALUES(relevance);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance) VALUES
-- 3D Printing Specialist
((SELECT career_path_id FROM CareerPaths WHERE career_name = '3D Printing Specialist'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python'), 95.00),
((SELECT career_path_id FROM CareerPaths WHERE career_name = '3D Printing Specialist'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'), 85.00),
((SELECT career_path_id FROM CareerPaths WHERE career_name = '3D Printing Specialist'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = '3D Modeling'), 85.00),

-- AR/VR Developer
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'AR/VR Developer'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'C++'), 80.00),
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'AR/VR Developer'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Unity/Unreal Engine Basics'), 80.00),
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'AR/VR Developer'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Object-Oriented Programming'), 84.00),

-- Audio Engineer
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'Audio Engineer'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'MATLAB'), 50.00),
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'Audio Engineer'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'), 85.00),
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'Audio Engineer'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Debugging'), 82.00),

-- Autonomous Vehicle Engineer
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'Autonomous Vehicle Engineer'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Machine Learning'), 90.00),
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'Autonomous Vehicle Engineer'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'C++'), 80.00),
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'Autonomous Vehicle Engineer'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Algorithm Design'), 75.00),

-- Big Data Analyst
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'Big Data Analyst'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'SQL'), 95.00),
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'Big Data Analyst'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'), 80.00),
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'Big Data Analyst'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Statistics'), 81.00),

-- Bioinformatics Specialist
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'Bioinformatics Specialist'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'R'), 45.00),
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'Bioinformatics Specialist'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python'), 95.00),
((SELECT career_path_id FROM CareerPaths WHERE career_name = 'Bioinformatics Specialist'),
 (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'), 80.00)
ON DUPLICATE KEY UPDATE relevance = VALUES(relevance);;

-- Bioinformatics Specialist
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Bioinformatics Specialist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'R'),
    45.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Bioinformatics Specialist')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'R')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Bioinformatics Specialist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Bioinformatics Specialist')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Bioinformatics Specialist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'),
    80.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Bioinformatics Specialist')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis')
);

-- Blockchain Developer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Blockchain Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Rust'),
    65.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Blockchain Developer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Rust')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Blockchain Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cryptography'),
    59.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Blockchain Developer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cryptography')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Blockchain Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Blockchain Developer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving')
);

-- Business Intelligence Analyst
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Business Intelligence Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'SQL'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Business Intelligence Analyst')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'SQL')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Business Intelligence Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'),
    80.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Business Intelligence Analyst')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Business Intelligence Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Business Intelligence Analyst')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving')
);

-- Cloud Security Engineer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Cloud Security Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cybersecurity Principles'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Cloud Security Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cybersecurity Principles')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Cloud Security Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Networking Protocols'),
    90.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Cloud Security Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Networking Protocols')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Cloud Security Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cloud-Specific Security Concepts'),
    85.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Cloud Security Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cloud-Specific Security Concepts')
);

-- Cryptographer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Cryptographer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cryptography'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Cryptographer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cryptography')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Cryptographer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Discrete Mathematics'),
    90.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Cryptographer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Discrete Mathematics')
);

-- Data Engineer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Data Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'SQL'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Data Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'SQL')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Data Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Structures'),
    90.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Data Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Structures')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Data Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python'),
    85.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Data Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python')
);

-- Digital Forensics Analyst
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Forensics Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Vulnerability Assessment'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Forensics Analyst')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Vulnerability Assessment')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Forensics Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cryptography'),
    90.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Forensics Analyst')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cryptography')
);

-- Digital Marketing Analyst
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Marketing Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Marketing Analyst')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Marketing Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Statistics'),
    90.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Marketing Analyst')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Statistics')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Marketing Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Marketing Analyst')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving')
);

-- Digital Twin Engineer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Twin Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Architecture'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Twin Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Architecture')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Twin Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python'),
    90.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Twin Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Twin Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Digital Twin Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving')
);

-- E-commerce Developer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'E-commerce Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'HTML'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'E-commerce Developer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'HTML')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'E-commerce Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'CSS'),
    90.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'E-commerce Developer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'CSS')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'E-commerce Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'JavaScript'),
    85.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'E-commerce Developer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'JavaScript')
);

-- Embedded Systems Engineer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Embedded Systems Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'C++'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Embedded Systems Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'C++')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Embedded Systems Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Architecture'),
    90.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Embedded Systems Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Architecture')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Embedded Systems Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Embedded Systems Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving')
);

-- Energy Systems Engineer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Energy Systems Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Energy Systems Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Energy Systems Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Architecture'),
    90.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Energy Systems Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Architecture')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Energy Systems Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'),
    85.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Energy Systems Engineer')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis')
);

-- Environmental Data Scientist
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Environmental Data Scientist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Statistics'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Environmental Data Scientist')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Statistics')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Environmental Data Scientist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'),
    90.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Environmental Data Scientist')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Environmental Data Scientist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Environmental Data Scientist')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving')
);

-- Ethical Hacker
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Ethical Hacker'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cybersecurity Principles'),
    95.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Ethical Hacker')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cybersecurity Principles')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Ethical Hacker'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Threat Analysis'),
    90.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Ethical Hacker')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Threat Analysis')
);

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Ethical Hacker'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Network Defense'),
    85.00
WHERE NOT EXISTS (
    SELECT 1 FROM CareerPathSkills
    WHERE career_path_id = (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Ethical Hacker')
      AND tech_skill_id = (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Network Defense')
);
-- Financial Systems Developer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Financial Systems Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Financial Systems Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Financial Systems Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'SQL'),
    85.00;

-- Full-Stack Developer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Full-Stack Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'JavaScript'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Full-Stack Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'HTML'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Full-Stack Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'CSS'),
    85.00;

-- Game Designer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Game Designer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Creative Writing Basics'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Game Designer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Unity/Unreal Engine Basics'),
    85.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Game Designer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    80.00;

-- Game Developer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Game Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'C++'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Game Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Unity/Unreal Engine Basics'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Game Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Algorithmic Thinking'),
    85.00;

-- Game Tester
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Game Tester'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Game Tester'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Debugging'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Game Tester'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Software Development Life Cycle'),
    85.00;

-- Hardware Engineer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Hardware Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Architecture'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Hardware Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'VHDL'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Hardware Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00;

-- Health Informatics Specialist
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Health Informatics Specialist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Health Informatics Specialist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Statistics'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Health Informatics Specialist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00;

-- Information Security Manager
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Information Security Manager'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cybersecurity Principles'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Information Security Manager'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Threat Analysis'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Information Security Manager'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Vulnerability Assessment'),
    85.00;

-- IoT Developer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'IoT Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'C++'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'IoT Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Networking Protocols'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'IoT Developer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Architecture'),
    85.00;

-- IT Consultant
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'IT Consultant'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'IT Consultant'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Project Management'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'IT Consultant'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Software Development Life Cycle'),
    85.00;

-- IT Project Manager
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'IT Project Manager'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Project Management'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'IT Project Manager'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'IT Project Manager'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Architecture'),
    85.00;

-- IT Support Specialist
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'IT Support Specialist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'IT Support Specialist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Networking Protocols'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'IT Support Specialist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Debugging'),
    85.00;

-- Machine Learning Researcher
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Machine Learning Researcher'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Machine Learning'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Machine Learning Researcher'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'AI Algorithms'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Machine Learning Researcher'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python'),
    85.00;

-- Natural Language Processing Specialist
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Natural Language Processing Specialist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Natural Language Processing Specialist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'AI Algorithms'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Natural Language Processing Specialist'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'),
    85.00;

-- Operations Analyst
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Operations Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Operations Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Operations Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Statistics'),
    85.00;

-- Penetration Tester
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Penetration Tester'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Cybersecurity Principles'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Penetration Tester'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Vulnerability Assessment'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Penetration Tester'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Threat Analysis'),
    85.00;

-- Product Manager
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Product Manager'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Project Management'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Product Manager'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Software Development Life Cycle'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Product Manager'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00;

-- Quality Assurance Engineer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Quality Assurance Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Software Development Life Cycle'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Quality Assurance Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Debugging'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Quality Assurance Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00;

-- Quantum Computing Researcher
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Quantum Computing Researcher'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Quantum Theory Basics'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Quantum Computing Researcher'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Quantum Computing Researcher'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00;

-- Robotics Engineer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Robotics Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'C++'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Robotics Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Python'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Robotics Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Architecture'),
    85.00;

-- Site Reliability Engineer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Site Reliability Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Networking Protocols'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Site Reliability Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Architecture'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Site Reliability Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Debugging'),
    85.00;

-- Systems Analyst
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Systems Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Systems Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Systems Analyst'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Statistics'),
    85.00;

-- Systems Architect
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Systems Architect'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'System Architecture'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Systems Architect'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Networking Protocols'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Systems Architect'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00;

-- Technical Program Manager
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Technical Program Manager'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Project Management'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Technical Program Manager'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Technical Program Manager'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Software Development Life Cycle'),
    85.00;

-- Technical Writer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Technical Writer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Creative Writing Basics'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Technical Writer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Technical Writer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Data Analysis'),
    85.00;

-- UX/UI Designer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'UX/UI Designer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Responsive Design'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'UX/UI Designer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Creative Writing Basics'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'UX/UI Designer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    85.00;

-- Video Production Engineer
INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Video Production Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'MATLAB'),
    95.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Video Production Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Problem Solving'),
    90.00;

INSERT INTO CareerPathSkills (career_path_id, tech_skill_id, relevance)
SELECT
    (SELECT career_path_id FROM CareerPaths WHERE career_name = 'Video Production Engineer'),
    (SELECT tech_skill_id FROM TechSkills WHERE skill_name = 'Creative Writing Basics'),
    85.00;

