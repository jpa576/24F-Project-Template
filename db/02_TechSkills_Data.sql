use algonauts_db;
-- Inserting top technical skills into the TechSkills table
INSERT INTO TechSkills (skill_name, complexity, description) VALUES
    ('Python', 'Beginner', 'A versatile high-level programming language known for its readability and broad applicability.'),
    ('JavaScript', 'Beginner', 'A core technology of the World Wide Web, enabling interactive web pages.'),
    ('Java', 'Intermediate', 'A class-based, object-oriented programming language designed for portability across platforms.'),
    ('C++', 'Advanced', 'An extension of C programming language with object-oriented features, widely used in system/software development.'),
    ('C#', 'Intermediate', 'A language developed by Microsoft, primarily for the .NET framework, combining principles from C and C++.'),
    ('Ruby', 'Beginner', 'A dynamic, open-source programming language with a focus on simplicity and productivity.'),
    ('PHP', 'Beginner', 'A server-side scripting language designed for web development but also used as a general-purpose language.'),
    ('Swift', 'Intermediate', 'A powerful and intuitive programming language for macOS, iOS, watchOS, and tvOS app development.'),
    ('Kotlin', 'Intermediate', 'A statically typed programming language for modern multiplatform applications, fully interoperable with Java.'),
    ('Go', 'Intermediate', 'An open-source programming language that makes it easy to build simple, reliable, and efficient software.'),
    ('R', 'Intermediate', 'A language and environment for statistical computing and graphics, widely used among statisticians and data miners.'),
    ('SQL', 'Beginner', 'A standard language for managing and manipulating relational databases.'),
    ('HTML', 'Beginner', 'The standard markup language for documents designed to be displayed in a web browser.'),
    ('CSS', 'Beginner', 'A style sheet language used for describing the presentation of a document written in HTML or XML.'),
    ('TypeScript', 'Intermediate', 'A strict syntactical superset of JavaScript that adds optional static typing.'),
    ('Scala', 'Advanced', 'A strong static type language that combines object-oriented and functional programming.'),
    ('Perl', 'Intermediate', 'A family of two high-level, general-purpose, interpreted, dynamic programming languages.'),
    ('Rust', 'Advanced', 'A language empowering everyone to build reliable and efficient software, focusing on safety and performance.'),
    ('Dart', 'Intermediate', 'A client-optimized language for fast apps on any platform, developed by Google.'),
    ('Shell Scripting', 'Beginner', 'Writing scripts for command-line interpreters to automate tasks in Unix/Linux environments.'),
    ('MATLAB', 'Intermediate', 'A programming platform designed specifically for engineers and scientists.'),
    ('Objective-C', 'Intermediate', 'A general-purpose, object-oriented programming language that adds Smalltalk-style messaging to C.'),
    ('Assembly Language', 'Advanced', 'A low-level programming language for a computer or other programmable device specific to a particular computer architecture.'),
    ('VHDL', 'Advanced', 'A hardware description language used in electronic design automation to describe digital and mixed-signal systems.'),
    ('Verilog', 'Advanced', 'A hardware description language used to model electronic systems.'),
    ('SAS', 'Intermediate', 'A software suite developed by SAS Institute for advanced analytics, multivariate analysis, business intelligence, and data management.'),
    ('COBOL', 'Intermediate', 'A compiled English-like computer programming language designed for business use.'),
    ('Fortran', 'Intermediate', 'A general-purpose, compiled imperative programming language that is especially suited to numeric computation and scientific computing.'),
    ('Haskell', 'Advanced', 'A standardized, general-purpose purely functional programming language, with non-strict semantics and strong static typing.'),
    ('Lua', 'Beginner', 'A lightweight, high-level, multi-paradigm programming language designed primarily for embedded use in applications.'),
    ('Ada', 'Advanced', 'A structured, statically typed, imperative, and object-oriented high-level computer programming language, extended from Pascal and other languages.'),
    ('Prolog', 'Advanced', 'A logic programming language associated with artificial intelligence and computational linguistics.'),
    ('Lisp', 'Advanced', 'A family of programming languages with a long history and a distinctive, fully parenthesized prefix notation.'),
    ('Scheme', 'Advanced', 'A minimalist dialect of the Lisp family of programming languages.'),
    ('Erlang', 'Advanced', 'A general-purpose, concurrent, functional programming language, and a garbage-collected runtime system.'),
    ('F#', 'Intermediate', 'A functional-first programming language that runs on the .NET runtime, known for its concise syntax and type inference.'),
    ('Elixir', 'Advanced', 'A dynamic, functional language designed for building scalable and maintainable applications.'),
    ('Clojure', 'Advanced', 'A modern, dynamic, and functional dialect of the Lisp programming language on the Java platform.'),
    ('Groovy', 'Intermediate', 'An object-oriented programming language for the Java platform; it is a dynamic language with features similar to those of Python, Ruby, and Smalltalk.'),
    ('Pascal', 'Beginner', 'An imperative and procedural programming language, designed as a small, efficient language intended to encourage good programming practices.'),
    ('Problem Solving', 'Intermediate', 'The process of finding solutions to complex or difficult issues.'),
    ('Software Tools Proficiency', 'Beginner', 'Ability to effectively use software tools for various applications.'),
    ('Academic Orientation', 'Beginner', 'Familiarity with academic environments and expectations.'),
    ('Professional Development', 'Intermediate', 'Skills aimed at improving professional capabilities and career advancement.'),
    ('Career Preparation', 'Intermediate', 'Readiness for entering and succeeding in a chosen career path.'),
    ('Co-op Readiness', 'Intermediate', 'Preparedness for cooperative education experiences.'),
    ('Discrete Mathematics', 'Intermediate', 'Study of mathematical structures that are fundamentally discrete rather than continuous.'),
    ('Logical Reasoning', 'Intermediate', 'Ability to analyze and evaluate arguments and reasoning.'),
    ('Applied Discrete Mathematics', 'Intermediate', 'Practical application of discrete mathematics concepts.'),
    ('Programming Fundamentals', 'Beginner', 'Basic concepts and techniques of programming.'),
    ('Algorithmic Thinking', 'Intermediate', 'Ability to solve problems using algorithms.'),
    ('Practical Programming', 'Beginner', 'Hands-on experience in writing and testing code.'),
    ('Debugging', 'Intermediate', 'Identifying and fixing errors in software code.'),
    ('Object-Oriented Programming', 'Intermediate', 'Programming paradigm based on the concept of objects.'),
    ('Data Structures', 'Intermediate', 'Organizing and storing data efficiently.'),
    ('Advanced Programming Techniques', 'Advanced', 'Complex programming methods and practices.'),
    ('Formal Logic', 'Intermediate', 'Study of reasoning and argumentation.'),
    ('Computational Theory', 'Advanced', 'Study of the capabilities and limitations of computing machines.'),
    ('Linear Algebra', 'Intermediate', 'Branch of mathematics concerning linear equations and their representations.'),
    ('Multivariable Calculus', 'Advanced', 'Extension of calculus to functions of multiple variables.'),
    ('Statistics', 'Intermediate', 'Science of collecting, analyzing, and interpreting data.'),
    ('Algorithm Design', 'Advanced', 'Creating efficient algorithms to solve problems.'),
    ('Data Analysis', 'Intermediate', 'Inspecting and modeling data to discover useful information.'),
    ('Software Design Patterns', 'Advanced', 'General repeatable solutions to common software design problems.'),
    ('Object-Oriented Principles', 'Intermediate', 'Fundamental concepts of object-oriented programming.'),
    ('Software Implementation', 'Intermediate', 'Process of executing a plan or design in software development.'),
    ('Design Application', 'Intermediate', 'Applying design principles in practical scenarios.'),
    ('System Architecture', 'Advanced', 'Conceptual model defining the structure and behavior of a system.'),
    ('Operating Systems', 'Intermediate', 'Software that manages computer hardware and software resources.'),
    ('Networking Protocols', 'Intermediate', 'Rules and conventions for communication between network devices.'),
    ('Distributed Computing', 'Advanced', 'Computing processes distributed across multiple systems.'),
    ('Automata Theory', 'Advanced', 'Study of abstract machines and problems they can solve.'),
    ('Complexity Theory', 'Advanced', 'Study of the complexity of solving problems.'),
    ('Software Engineering', 'Intermediate', 'Application of engineering principles to software development.'),
    ('Project Management', 'Intermediate', 'Planning and executing projects efficiently.'),
    ('Software Development Life Cycle', 'Intermediate', 'Process of planning, creating, testing, and deploying software.'),
    ('Quality Assurance', 'Intermediate', 'Ensuring that products meet specified quality standards.'),
    ('Cybersecurity Principles', 'Intermediate', 'Fundamental concepts of protecting systems and data.'),
    ('Threat Analysis', 'Advanced', 'Identifying and evaluating potential security threats.'),
    ('System Vulnerability Assessment', 'Advanced', 'Identifying weaknesses in systems that could be exploited.'),
    ('Security Protocols', 'Advanced', 'Procedures and measures to protect data and systems.'),
    ('Network Defense', 'Advanced', 'Protecting computer networks from intrusions and attacks.'),
    ('Cryptography', 'Advanced', 'Practice of secure communication in the presence of adversaries.'),
    ('AI Algorithms', 'Advanced', 'Algorithms designed to perform tasks that typically require human intelligence.'),
    ('Machine Learning', 'Advanced', 'Study of computer algorithms that improve automatically through experience.'),
    ('Data Mining Techniques', 'Advanced', 'Extracting patterns from large data sets.'),
    ('Predictive Modeling', 'Advanced', 'Using statistics to predict future outcomes.'),
    ('NLP Techniques', 'Advanced', 'Methods for processing and analyzing natural language data.'),
    ('Text Analysis', 'Advanced', 'Deriving meaningful information from text.'),
    ('Game AI Development', 'Advanced', 'Creating intelligent behaviors in games.'),
    ('Simulation', 'Advanced', 'Imitating the operation of real-world processes or systems.'),
    ('Robotics Engineering', 'Advanced', 'Design and construction of robots.'),
    ('Control Systems', 'Advanced', 'Systems that manage, command, direct, or regulate behaviors.'),
    ('Advanced Machine Learning', 'Advanced', 'Complex machine learning techniques and models.'),
    ('Big Data Analytics', 'Advanced', 'Analyzing large and complex data sets.'),
    ('Search Algorithms', 'Intermediate', 'Algorithms for retrieving information from data structures.'),
    ('Data Retrieval Systems', 'Intermediate', 'Systems designed to retrieve data efficiently.'),
    ('Cognitive Processes', 'Intermediate', 'Mental processes involved in gaining knowledge and comprehension.'),
    ('Human-Computer Interaction', 'Intermediate', 'Study of how people interact with computers.'),
    ('Automated Reasoning', 'Advanced', 'Use of computers to emulate human reasoning.'),
    ('Formal Verification', 'Advanced', 'Mathematical proof of the correctness of systems.'),
    ('Computational Complexity', 'Advanced', 'Study of the resources required for algorithms to solve problems.'),
    ('Algorithm Optimization', 'Advanced', 'Improving the efficiency of algorithms.'),
    ('Computational Efficiency', 'Advanced', 'Measure of the resource usage of algorithms.'),
    ('Research Methodologies', 'Intermediate', 'Systematic methods used in research.'),
    ('Technical Writing', 'Intermediate', 'Writing technical documents and manuals.'),
    ('Research Presentation', 'Intermediate', 'Presenting research findings effectively.'),
    ('Critical Analysis', 'Intermediate', 'Evaluating arguments and evidence systematically.'),
    ('System Design', 'Advanced', 'Process of defining the architecture of systems.'),
    ('Verification Techniques', 'Advanced', 'Methods to ensure systems meet specifications.'),
    ('Encryption Methods', 'Advanced', 'Techniques for securing information.');




-- CS 1100: Computer Science and Its Applications
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '1100', 1),  -- Problem Solving
('CS', '1100', 2);  -- Software Tools Proficiency

-- CS 1200: First Year Seminar
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '1200', 3),  -- Academic Orientation
('CS', '1200', 4);  -- Professional Development

-- CS 1210: Professional Development for Khoury Co-op
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '1210', 5),  -- Career Preparation
('CS', '1210', 6);  -- Co-op Readiness

-- CS 1800: Discrete Structures
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '1800', 7),  -- Discrete Mathematics
('CS', '1800', 8);  -- Logical Reasoning

-- CS 1802: Seminar for CS 1800
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '1802', 9);  -- Applied Discrete Mathematics

-- CS 2500: Fundamentals of Computer Science 1
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '2500', 10),  -- Programming Fundamentals
('CS', '2500', 11);  -- Algorithmic Thinking

-- CS 2501: Lab for CS 2500
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '2501', 12),  -- Practical Programming
('CS', '2501', 13);  -- Debugging

-- CS 2510: Fundamentals of Computer Science 2
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '2510', 14),  -- Object-Oriented Programming
('CS', '2510', 15);  -- Data Structures

-- CS 2511: Lab for CS 2510
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '2511', 16);  -- Advanced Programming Techniques

-- CS 2800: Logic and Computation
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '2800', 17),  -- Formal Logic
('CS', '2800', 18);  -- Computational Theory

-- CS 2810: Mathematics of Data Models
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '2810', 19),  -- Linear Algebra
('CS', '2810', 20),  -- Multivariable Calculus
('CS', '2810', 21);  -- Statistics

-- CS 3000: Algorithms and Data
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '3000', 22),  -- Algorithm Design
('CS', '3000', 23);  -- Data Analysis

-- CS 3500: Object-Oriented Design
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '3500', 24),  -- Software Design Patterns
('CS', '3500', 25);  -- Object-Oriented Principles

-- CS 3501: Lab for CS 3500
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '3501', 26),  -- Software Implementation
('CS', '3501', 27);  -- Design Application

-- CS 3650: Computer Systems
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '3650', 28),  -- System Architecture
('CS', '3650', 29);  -- Operating Systems

-- CS 3700: Networks and Distributed Systems
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '3700', 30),  -- Networking Protocols
('CS', '3700', 31);  -- Distributed Computing

-- CS 3800: Theory of Computation
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '3800', 32),  -- Automata Theory
('CS', '3800', 33);  -- Complexity Theory

-- CS 4500: Software Development
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4500', 34),  -- Software Engineering
('CS', '4500', 35);  -- Project Management

-- CS 4530: Fundamentals of Software Engineering
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4530', 36),  -- Software Development Life Cycle
('CS', '4530', 37);  -- Quality Assurance

-- CY 2550: Foundations of Cybersecurity
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CY', '2550', 38),  -- Cybersecurity Principles
('CY', '2550', 39);  -- Threat Analysis

-- CY 3740: Systems Security
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CY', '3740', 40),  -- System Vulnerability Assessment
('CY', '3740', 41);  -- Security Protocols

-- CY 4740: Network Security
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CY', '4740', 42),  -- Network Defense
('CY', '4740', 43);  -- Cryptography

-- CS 4100: Artificial Intelligence
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4100', 44),  -- AI Algorithms
('CS', '4100', 45);  -- Machine Learning

-- DS 4400: Machine Learning and Data Mining 1
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('DS', '4400', 46),  -- Data Mining Techniques
('DS', '4400', 47);  -- Predictive Modeling

-- CS 4120: Natural Language Processing
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4120', 48),  -- NLP Techniques
('CS', '4120', 49);  -- Text Analysis

-- CS 3520: Programming in C++
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '3520', 4);  -- C++ Programming

-- CS 3950: Introduction to Computer Science Research
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '3950', 50);  -- Research Methodologies

-- CS 4150: Game Artificial Intelligence
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4150', 51);  -- Game AI Development

-- CS 4300: Computer Graphics
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4300', 52);  -- Computer Graphics Programming

-- CS 4400: Programming Languages
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4400', 53);  -- Programming Language Theory

-- CS 4410: Compilers
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4410', 54);  -- Compiler Construction

-- CS 4520: Mobile Application Development
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4520', 55);  -- Mobile App Development

-- CS 4550: Web Development
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4550', 56);  -- Web Development Technologies

-- CS 4610: Robotic Science and Systems
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4610', 57);  -- Robotics Programming

-- CS 4700: Network Fundamentals
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4700', 58);  -- Networking Basics

-- CS 4710: Mobile and Wireless Systems
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4710', 59);  -- Mobile Systems Development

-- CS 4730: Distributed Systems
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4730', 60);  -- Distributed Computing

-- CS 4805: Fundamentals of Complexity Theory
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4805', 61);  -- Complexity Theory

-- CS 4810: Advanced Algorithms
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4810', 62);  -- Advanced Algorithm Design

-- CS 4820: Computer-Aided Reasoning
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4820', 63);  -- Formal Verification

-- CS 4830: System Specification, Verification, and Synthesis
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4830', 64);  -- System Verification

-- CS 4950: Computer Science Research Seminar
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CS', '4950', 65);  -- Research Presentation

-- CY 4760: Security of Wireless and Mobile Systems
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CY', '4760', 66);  -- Wireless Security

-- CY 4770: Cryptography
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('CY', '4770', 67);  -- Cryptographic Techniques

-- DS 4200: Information Presentation and Visualization
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('DS', '4200', 68);  -- Data Visualization

-- DS 4420: Machine Learning and Data Mining 2
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('DS', '4420', 69);  -- Advanced Machine Learning

-- IS 2000: Principles of Information Science
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('IS', '2000', 70);  -- Information Science Fundamentals

-- IS 4200: Information Retrieval
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('IS', '4200', 71);  -- Information Retrieval Techniques

-- IS 4300: Human Computer Interaction
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('IS', '4300', 72);  -- HCI Principles

-- IS 4800: Empirical Research Methods
INSERT INTO CourseTechSkills (department, course_number, tech_skill_id) VALUES
('IS', '4800', 73);  -- Empirical Research Methods



