use algonauts_db;

-- Insert User Data
INSERT INTO Users (user_id, name, email, year, plan_id) VALUES
(1, 'Jack Smith', 'jack.smith@example.com', 2024, 1),
(2, 'Mark Johnson', 'mark.johnson@example.com', 2024, 2);

-- Insert User Course Progress
INSERT INTO UserCourseProgress (progress_id, user_id, department, course_number, progress_status) VALUES
(1, 1, 'CS', '5001', 'completed'),
(2, 1, 'CS', '5010', 'in-progress'),
(3, 2, 'CS', '4500', 'completed'),
(4, 2, 'CS', '4800', 'in-progress');

-- Insert User Skills
INSERT INTO UserSkills (user_skill_id, user_id, tech_skill_id, acquired_date) VALUES
(1, 1, 1, '2023-09-01'),
(2, 1, 2, '2023-10-01'),
(3, 2, 3, '2023-09-15'),
(4, 2, 4, '2023-10-10');

-- Insert User Career Progress
INSERT INTO UserCareerProgress (progress_id, user_id, career_path_id, progress_percentage) VALUES
(1, 1, 1, 50.00),
(2, 2, 2, 75.00);
