# STaff Education Platform
## About Project
```text
    Our project has been conceive a couple of years before it's date of birth,
    but a lot of time we didn't have enough time to start working on it.
    But at last time has come...
```
## Project info
```text
Current version: 0.10
    Version info:
    Project decomposition completed!
        Added:
            - new application "courses";
                - previous functionality for model "Course" has migrate to this app;
            - new application "employees";
                - custom model instead built-in model "User";
                - previous functionality for model "User" has migrate to this app;
                - join to course controller/template/form;
            - description;
        Changed:
            - completely reworked models and migrations;
            - most of forms and templates for all applications;
            - role model;
            - tests;
        Deleted:
            - unused functionality;
            
Previous versions:
    Version 0.07 info:
        Added:
            - GitHub Actions;
        Changed:
            - code refactoring dur to PEP8 standard;
    Version 0.05 info:
        Added:
            - all needed forms and views to use CRUD-operations with main models (User, Course);
            - confirmation forms for deleting courses and students;
            - privileges control to get access to different URLs and options on site;
            - base data generation script;
            - tests for models and views;
        Changed:
            - models and migrations;
            - all forms and templates to display necessary information about users and courses;
            - role model for feature access;
            - views permissions;
        Deleted:
            - unused functionality;
    Version 0.02 info:
        Added:
            - controllers/templates/forms for Course model;
            - additional controllers for controllers/templates/forms for list of users and user detail info;
        Changed:
            - Course model and migrations;
            - forms and templates for users;
            - base template;
    Version 0.01 info:
        Added:
            - Course/Result models and migrations;
            - base controllers/templates/forms for user registration/login/logout;
    Date of birth: 2023.02.06
```