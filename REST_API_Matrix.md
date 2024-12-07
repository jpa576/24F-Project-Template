# REST API Matrix

This matrix documents all available endpoints in the application, along with their methods, descriptions, and associated user stories or personas.

| **Resource**       | **HTTP Method** | **Endpoint**                                        | **Description**                                                            | **User Story/Persona**             |
|---------------------|-----------------|----------------------------------------------------|----------------------------------------------------------------------------|-------------------------------------|
| **Static Files**    | GET             | `/static/<filename>`                               | Serve static files (e.g., images, stylesheets).                            | General                            |
| **Home**            | GET             | `/`                                               | Welcome route for the application.                                        | General                            |
| **Playlists**       | GET             | `/playlist`                                       | Fetch playlist data.                                                       | General User                       |
| **Messages**        | GET             | `/niceMesage`                                     | Fetch a positive affirmation.                                             | General User                       |
|                     | GET             | `/message`                                        | Fetch a message.                                                           | General User                       |
| **Products**        | GET             | `/p/products`                                     | Fetch all products.                                                        | Users browsing products            |
|                     | GET             | `/p/product/<id>`                                 | Fetch a specific product by ID.                                            | Users viewing product details      |
|                     | GET             | `/p/mostExpensive`                                | Fetch the most expensive product.                                          | Users interested in luxury items   |
|                     | GET             | `/p/tenMostExpensive`                             | Fetch the top 10 most expensive products.                                  | Users interested in top-tier items |
|                     | GET             | `/p/topOrderedProducts`                           | Fetch the top ordered products.                                            | Admin reviewing trends             |
|                     | POST            | `/p/product`                                      | Add a new product.                                                         | Admin adding products              |
|                     | PUT             | `/p/product`                                      | Update an existing product.                                                | Admin updating products            |
|                     | GET             | `/p/categories`                                   | Fetch all product categories.                                              | Users browsing by category         |
| **Courses**         | GET             | `/c/all_courses`                                  | Fetch all available courses.                                               | Users exploring courses            |
|                     | DELETE          | `/c/remove_course`                                | Remove a course.                                                           | Admin removing courses             |
|                     | GET             | `/c/concentration_courses`                        | Fetch courses by concentration.                                            | Users filtering by focus           |
|                     | GET             | `/c/courses_without_skills`                       | Fetch courses without associated skills.                                   | Admin improving course data        |
|                     | POST            | `/c/add_course`                                   | Add a new course.                                                          | Admin adding courses               |
| **Tech Skills**     | GET             | `/ts/all_skills`                                  | Fetch all technical skills.                                                | Users exploring skills             |
|                     | GET             | `/ts/skills/by_demand`                            | Fetch skills by demand level.                                              | Admin reviewing skill trends       |
|                     | POST            | `/ts/add_skill`                                   | Add a new skill.                                                           | Admin adding skills                |
| **Careers**         | GET             | `/careers/all_careers`                            | Fetch all careers.                                                         | Users exploring career paths       |
|                     | GET             | `/careers/career_skills`                          | Fetch skills required for careers.                                         | Users planning career growth       |
|                     | GET             | `/careers/career_skills2`                         | Fetch careers with no skill prerequisites.                                 | Admin improving career data        |
|                     | GET             | `/careers/by_salary`                              | Fetch careers by salary range.                                             | Users seeking high-paying careers  |
|                     | PUT             | `/careers/<user_id>/update_progress/<career_path_id>` | Update career progress for a user.                                     | Users tracking their career path   |
|                     | POST            | `/careers/add_career`                             | Add a new career path.                                                     | Admin adding careers               |
| **Users**           | GET             | `/u/<user_id>/info`                               | Fetch information about a specific user.                                   | Admin or user viewing details      |
|                     | GET             | `/u/<user_id>/skills`                             | Fetch skills associated with a user.                                       | Users tracking their skills        |
|                     | GET             | `/u/<user_id>/progress`                           | Fetch progress of a specific user.                                         | Users tracking progress            |
|                     | GET             | `/u/<user_id>/careers`                            | Fetch careers associated with a user.                                      | Users managing careers             |
|                     | PUT             | `/u/<user_id>/update_careers/<career_id>`         | Update career details for a user.                                          | Admin managing user careers        |
|                     | GET             | `/u/all_users`                                    | Fetch all users.                                                           | Admin viewing user database        |
|                     | POST            | `/u/add_user`                                     | Add a new user.                                                            | Admin onboarding users             |
|                     | DELETE          | `/u/<user_id>/remove_user`                        | Remove a user.                                                             | Admin removing users               |
|                     | PUT             | `/u/<user_id>/update_progress1`                  | Update user progress.                                                      | Admin managing user data           |
|                     | DELETE          | `/u/<user_id>/pop_career/<career_id>`            | Remove a career from a user.                                               | Users editing their career paths   |
|                     | POST            | `/u/<user_id>/add_careers`                       | Add a career to a user.                                                    | Users adding career paths          |
|                     | PUT             | `/u/<user_id>/update_progress`                   | Update progress for a user.                                                | Admin updating progress            |
|                     | GET             | `/u/<user_id>/academic_progress`                 | Fetch academic progress of a user.                                         | Users tracking academics           |
| **Assessments**     | GET             | `/ass/all_assessments`                           | Fetch all coding assessments.                                              | Users preparing for assessments    |
|                     | POST            | `/ass/save_submission`                           | Save an assessment submission.                                             | Users submitting assessments       |
|                     | GET             | `/ass/career_assessments/<career_path_id>`       | Fetch assessments for a specific career path.                              | Users planning career assessments  |

---

