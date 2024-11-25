use algonauts_db;
-- Drop tables in the correct order to handle foreign key dependencies
DROP TABLE IF EXISTS UserCodingSubmissions;
DROP TABLE IF EXISTS CodingAssessments;
DROP TABLE IF EXISTS UserSkills;
DROP TABLE IF EXISTS UserCourseProgress;
DROP TABLE IF EXISTS CourseTechSkills;
DROP TABLE IF EXISTS CoursePrerequisites;
DROP TABLE IF EXISTS UserCareerProgress;
DROP TABLE IF EXISTS CareerPathSkills;
DROP TABLE IF EXISTS CareerPaths;
DROP TABLE IF EXISTS TechSkills;
DROP TABLE IF EXISTS AcademicCourses;
DROP TABLE IF EXISTS Users;




-- Create Users Table
CREATE TABLE Users (
  user_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  year INT DEFAULT 0
);

-- Create Academic Courses Table with Composite Primary Key
CREATE TABLE AcademicCourses (
  department VARCHAR(10) NOT NULL,
  course_number VARCHAR(10) NOT NULL,
  course_name VARCHAR(200) NOT NULL,
  course_description TEXT,
  credits INT,
  PRIMARY KEY (department, course_number)
);

-- Create Tech Skills Table
CREATE TABLE TechSkills (
  tech_skill_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  skill_name VARCHAR(100) UNIQUE NOT NULL,
  complexity ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL
);

-- Create User Course Progress Table
CREATE TABLE UserCourseProgress (
  progress_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED NOT NULL,
  department VARCHAR(10) NOT NULL,
  course_number VARCHAR(10) NOT NULL,
  progress_status VARCHAR(20) DEFAULT 'in-progress',
  FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
  FOREIGN KEY (department, course_number) REFERENCES AcademicCourses(department, course_number) ON DELETE CASCADE
);

-- Mapping Academic Courses to Tech Skills
CREATE TABLE CourseTechSkills (
  mapping_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  department VARCHAR(10) NOT NULL,
  course_number VARCHAR(10) NOT NULL,
  tech_skill_id INT UNSIGNED NOT NULL,
  FOREIGN KEY (department, course_number) REFERENCES AcademicCourses(department, course_number) ON DELETE CASCADE,
  FOREIGN KEY (tech_skill_id) REFERENCES TechSkills(tech_skill_id) ON DELETE CASCADE
);

-- Create Course Prerequisites Table with Self-Referential Foreign Keys
CREATE TABLE CoursePrerequisites (
    department VARCHAR(10) NOT NULL,
    course_number VARCHAR(10) NOT NULL,
    prerequisite_department VARCHAR(10) NOT NULL,
    prerequisite_number VARCHAR(10) NOT NULL,
    PRIMARY KEY (department, course_number, prerequisite_department, prerequisite_number),
    FOREIGN KEY (department, course_number) REFERENCES AcademicCourses(department, course_number) ON DELETE CASCADE,
    FOREIGN KEY (prerequisite_department, prerequisite_number) REFERENCES AcademicCourses(department, course_number) ON DELETE CASCADE
);

-- Create Career Paths Table
CREATE TABLE CareerPaths (
  career_path_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  career_name VARCHAR(100) NOT NULL,
  description TEXT,
  required_skills TEXT
);

-- Create User Skills Table
CREATE TABLE UserSkills (
  user_skill_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED NOT NULL,
  tech_skill_id INT UNSIGNED NOT NULL,
  acquired_date DATE DEFAULT NULL,
  FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
  FOREIGN KEY (tech_skill_id) REFERENCES TechSkills(tech_skill_id) ON DELETE CASCADE
);

-- Create User Career Progress Table
CREATE TABLE UserCareerProgress (
  progress_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED NOT NULL,
  career_path_id INT UNSIGNED NOT NULL,
  progress_percentage DECIMAL(5,2) DEFAULT 0.00,
  FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
  FOREIGN KEY (career_path_id) REFERENCES CareerPaths(career_path_id) ON DELETE CASCADE
);

CREATE TABLE CareerPathSkills (
    career_path_id INT UNSIGNED NOT NULL,
    tech_skill_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (career_path_id, tech_skill_id),
    FOREIGN KEY (career_path_id) REFERENCES CareerPaths(career_path_id) ON DELETE CASCADE,
    FOREIGN KEY (tech_skill_id) REFERENCES TechSkills(tech_skill_id) ON DELETE CASCADE
);

CREATE TABLE CodingAssessments (
    assessment_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    skill_id INT UNSIGNED,
    problem_statement TEXT,
    expected_output TEXT,
    FOREIGN KEY (skill_id) REFERENCES TechSkills(tech_skill_id)
);

CREATE TABLE UserCodingSubmissions (
    submission_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT UNSIGNED,
    assessment_id INT UNSIGNED,
    career_path_id INT UNSIGNED,
    submitted_code TEXT,
    execution_result TEXT,
    score DECIMAL(5,2),
    status ENUM('correct', 'incorrect') DEFAULT 'incorrect',
    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (assessment_id) REFERENCES CodingAssessments(assessment_id),
    FOREIGN KEY (career_path_id) REFERENCES CareerPaths(career_path_id)
);
CREATE TABLE JobMarketInsights (
    insight_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    job_title VARCHAR(100) NOT NULL,
    required_skills TEXT,
    industry_trends TEXT,
    data_source VARCHAR(100)
);

INSERT INTO AcademicCourses (department, course_number, course_name, course_description, credits) VALUES
('CS', '1100', 'Computer Science and Its Applications', 'Introduces students to the field of computer science and the patterns of thinking that enable them to become intelligent users of software tools in a problem-solving setting.', 4),
('CS', '1800', 'Discrete Structures', 'Introduces the mathematical structures and methods that form the foundation of computer science.', 4),
('CS', '2500', 'Fundamentals of Computer Science 1', 'Introduces the fundamental ideas of computing and the principles of programming.', 4),
('CS', '2510', 'Fundamentals of Computer Science 2', 'Continues CS 2500. Examines object-oriented programming and associated algorithms using more complex data structures as the focus.', 4),
('CS', '2800', 'Logic and Computation', 'Introduces formal logic and its connections to computer and information science.', 4),
('CS', '3000', 'Algorithms and Data', 'Introduces the fundamental concepts of algorithms and data structures.', 4),
('CS', '3500', 'Object-Oriented Design', 'Covers the principles of object-oriented design and programming.', 4),
('CS', '3650', 'Computer Systems', 'Introduces the fundamental concepts of computer systems.', 4),
('CS', '3700', 'Networks and Distributed Systems', 'Introduces the fundamental concepts of computer networks and distributed systems.', 4),
('CS', '3800', 'Theory of Computation', 'Introduces the fundamental concepts of theoretical computer science.', 4);



