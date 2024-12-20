use algonauts_db;
-- Disable foreign key checks to allow dropping tables without constraint issues
SET FOREIGN_KEY_CHECKS = 0;

-- Drop child tables first
DROP TABLE IF EXISTS CareerPathAssessments;
DROP TABLE IF EXISTS UserCodingSubmissions;
DROP TABLE IF EXISTS CodingAssessments;
DROP TABLE IF EXISTS UserSkills;
DROP TABLE IF EXISTS UserCourseProgress;
DROP TABLE IF EXISTS CourseTechSkills;
DROP TABLE IF EXISTS CoursePrerequisites;
DROP TABLE IF EXISTS UserCareerProgress;

DROP TABLE IF EXISTS CareerPathSkills;
DROP TABLE IF EXISTS RequiredCourses;
DROP TABLE IF EXISTS ConcentrationCourses;
DROP TABLE IF EXISTS SemesterCourses;
DROP TABLE IF EXISTS Semesters;

-- Drop intermediate tables
DROP TABLE IF EXISTS AcademicPlans;
DROP TABLE IF EXISTS AcademicConcentrations;
DROP TABLE IF EXISTS AcademicPrograms;

-- Drop parent tables
DROP TABLE IF EXISTS CareerPaths;
DROP TABLE IF EXISTS CareerPathCourses;
DROP TABLE IF EXISTS TechSkills;
DROP TABLE IF EXISTS InterviewQuestions;
DROP TABLE IF EXISTS AcademicCourses;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS JobMarketInsights;

-- Re-enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;


-- Create Interview Questions Table
CREATE TABLE InterviewQuestions (
    question_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    skill VARCHAR(100) NOT NULL,
    difficulty ENUM('Easy', 'Medium', 'Hard') NOT NULL
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
    complexity ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL,
    category VARCHAR(50) DEFAULT 'General',
    popularity_score DECIMAL(4, 2) DEFAULT 0.00,
    description TEXT
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
  career_path_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each career path
  career_name VARCHAR(100) NOT NULL,                      -- Name of the career
  description TEXT,                                       -- Detailed description of the career
  salary INT UNSIGNED,                                    -- Expected average salary in USD
  demand DECIMAL(2, 1)                                    -- Demand rating (e.g., 4.7 out of 5.0)
);

-- Create a table to map courses to career paths
CREATE TABLE CareerPathCourses (
    career_path_id INT UNSIGNED NOT NULL,
    department VARCHAR(10) NOT NULL,
    course_number VARCHAR(10) NOT NULL,
    PRIMARY KEY (career_path_id, department, course_number),
    FOREIGN KEY (career_path_id) REFERENCES CareerPaths(career_path_id) ON DELETE CASCADE,
    FOREIGN KEY (department, course_number) REFERENCES AcademicCourses(department, course_number) ON DELETE CASCADE
);


CREATE TABLE CareerPathSkills (
    career_path_id INT UNSIGNED NOT NULL,
    tech_skill_id INT UNSIGNED NOT NULL,
    relevance DECIMAL (4,2),
    PRIMARY KEY (career_path_id, tech_skill_id),
    FOREIGN KEY (career_path_id) REFERENCES CareerPaths(career_path_id) ON DELETE CASCADE,
    FOREIGN KEY (tech_skill_id) REFERENCES TechSkills(tech_skill_id) ON DELETE CASCADE
);

CREATE TABLE CodingAssessments (
    assessment_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    skill_id INT UNSIGNED,
    problem_statement TEXT,
    input_example TEXT, -- New column for input example
    expected_output TEXT, -- Output expected for the given input
    FOREIGN KEY (skill_id) REFERENCES TechSkills(tech_skill_id)
);


CREATE TABLE JobMarketInsights (
    insight_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    job_title VARCHAR(100) NOT NULL,
    required_skills TEXT,
    industry_trends TEXT,
    data_source VARCHAR(100)
);

CREATE TABLE AcademicPrograms (
    program_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    degree_type ENUM('BS', 'BA', 'MS', 'PhD') NOT NULL,
    department VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE RequiredCourses (
    program_id INT UNSIGNED NOT NULL,
    department VARCHAR(10) NOT NULL,
    course_number VARCHAR(10) NOT NULL,
    requirement_type ENUM('Required', 'Elective') DEFAULT 'Required',
    requirement_category ENUM('Overview', 'Fundamental', 'Required', 'Security', 'Presentation', 'Elective') NOT NULL,
    PRIMARY KEY (program_id, department, course_number),
    FOREIGN KEY (program_id) REFERENCES AcademicPrograms(program_id) ON DELETE CASCADE,
    FOREIGN KEY (department, course_number) REFERENCES AcademicCourses(department, course_number) ON DELETE CASCADE
);

CREATE TABLE AcademicConcentrations (
    concentration_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    program_id INT UNSIGNED NOT NULL,
    concentration_name VARCHAR(100) NOT NULL,
    description TEXT,
    FOREIGN KEY (program_id) REFERENCES AcademicPrograms(program_id) ON DELETE CASCADE
);

CREATE TABLE ConcentrationCourses (
    concentration_id INT UNSIGNED NOT NULL,
    department VARCHAR(10) NOT NULL,
    course_number VARCHAR(10) NOT NULL,
    PRIMARY KEY (concentration_id, department, course_number),
    FOREIGN KEY (concentration_id) REFERENCES AcademicConcentrations(concentration_id) ON DELETE CASCADE,
    FOREIGN KEY (department, course_number) REFERENCES AcademicCourses(department, course_number) ON DELETE CASCADE
);

-- Create Users Table
CREATE TABLE Users (
  user_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  year INT DEFAULT 0,
  plan_id INT UNSIGNED
);

CREATE TABLE UserCodingSubmissions (
    submission_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT UNSIGNED,
    assessment_id INT UNSIGNED,
    career_path_id INT UNSIGNED,
    submitted_code TEXT,
    execution_result TEXT,
    status ENUM('correct', 'incorrect') DEFAULT 'incorrect',
    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (assessment_id) REFERENCES CodingAssessments(assessment_id),
    FOREIGN KEY (career_path_id) REFERENCES CareerPaths(career_path_id)
        );

CREATE TABLE UserCourseProgress (
  progress_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the record
  user_id INT UNSIGNED NOT NULL,                      -- Reference to the Users table
  department VARCHAR(10) NOT NULL,                    -- Department of the course (e.g., CS, DS)
  course_number VARCHAR(10) NOT NULL,                 -- Course number (e.g., 2500, 4400)
  progress_status ENUM('in-progress', 'completed', 'not-started') DEFAULT 'in-progress', -- Default is 'in-progress'

  FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
  FOREIGN KEY (department, course_number) REFERENCES AcademicCourses(department, course_number) ON DELETE CASCADE
);

-- Updated User Skills Table
CREATE TABLE UserSkills (
  user_skill_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED NOT NULL,
  tech_skill_id INT UNSIGNED NOT NULL,
  acquired_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Use TIMESTAMP for default current date
  skill_level ENUM('Beginner', 'Intermediate', 'Advanced', 'Expert') DEFAULT 'Beginner', -- Skill proficiency level
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for creation
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
  FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
  FOREIGN KEY (tech_skill_id) REFERENCES TechSkills(tech_skill_id) ON DELETE CASCADE,
  UNIQUE (user_id, tech_skill_id) -- Ensure unique user-skill combination
) ENGINE=InnoDB;



CREATE TABLE CareerPathAssessments (
    mapping_id INT AUTO_INCREMENT PRIMARY KEY,
    career_path_id INT UNSIGNED NOT NULL,
    assessment_id  INT UNSIGNED NOT NULL,
    FOREIGN KEY (career_path_id) REFERENCES CareerPaths(career_path_id) ON DELETE CASCADE,
    FOREIGN KEY (assessment_id) REFERENCES CodingAssessments(assessment_id) ON DELETE CASCADE
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





