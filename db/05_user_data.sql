-- Insert user into Users table

INSERT IGNORE INTO Users (name, email, year, plan_id)
VALUES ('Marcus', 'mca007@example.com', 2, NULL);

-- Assuming "Marcus" is assigned user_id 1, and using sample data for other tables


-- Insert skills acquired by "Marcus"
INSERT INTO UserSkills (user_id, tech_skill_id, acquired_date)
VALUES
(1, 1, '2023-01-15'), -- Assuming tech_skill_id 1 is Python
(1, 3, '2023-05-20'), -- Assuming tech_skill_id 3 is Algorithmic Thinking
(1, 6, '2023-08-10'); -- Assuming tech_skill_id 6 is Data Analysis

-- Insert career progress for "Marcus"
INSERT INTO UserCareerProgress (user_id, career_path_id, progress_percentage)
VALUES
(1, 1, 45.00), -- Assuming career_path_id 1 is Software Engineer
(1, 2, 25.00); -- Assuming career_path_id 2 is Data Scientist

-- Insert courses Marcus is currently taking
INSERT INTO UserCourseProgress (user_id, department, course_number, progress_status)
VALUES
(1, 'CS', '2500', 'in-progress'), -- Fundamentals of Computer Science 1
(1, 'CS', '2510', 'in-progress'), -- Fundamentals of Computer Science 2
(1, 'DS', '4400', 'in-progress'); -- Machine Learning and Data Mining 1

-- Insert courses Marcus has completed
INSERT INTO UserCourseProgress (user_id, department, course_number, progress_status)
VALUES
(1, 'CS', '1800', 'completed'), -- Discrete Structures
(1, 'CS', '3000', 'completed'); -- Algorithms and Data

-- Insert courses Marcus needs to take
-- These are derived from the CareerPathCourses table
INSERT INTO UserCourseProgress (user_id, department, course_number, progress_status)
VALUES
(1, 'CS', '3500', 'not-started'), -- Object-Oriented Design
(1, 'CS', '4500', 'not-started'), -- Software Development
(1, 'DS', '4420', 'not-started'), -- Machine Learning and Data Mining 2
(1, 'CS', '4100', 'not-started'); -- Artificial Intelligence





