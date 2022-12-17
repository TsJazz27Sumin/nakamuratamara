Nakamuratamara
====

## Overview

- This web application made for a close university professor. To sharing reports with one's fellow students.

## Description
### Functional Configuration

- Administrator Features
    - Authentication
        - Login URL Request
        - Login
        - Logout
    - Report Maintenance
        - Search
        - Sort
        - Paging
        - Report Create
        - Report Delete
        - Report Download
    - User Maintenance
        - Search
        - Sort
        - Paging
        - User Create
        - User Update
        - User Delete
    - Access Log Browsing
        - List
        - CSV download
- Student Features
    - Login
    - List
    - Change list
    - Report Download

### Technical Elements
 - Front End
   - JavaScript
   - jQuery
   - Ajax
   - Stylus
   - HTML
 - Server Side
   - Python
   - Python Web Framework : Django
   - SQL
   - PostgreSQL
   - Google Drive API
   - Sendgrid API

### Using API Features
 - Authentication for Administrator.  
 - Report file management.

>Authentication for Administrator.

In Japan of recent date, Security incidents are occurring. Some cases, There was a leak of id and password. For example Home file service. So I design authentication feature without id and password.
Everytime administrator request onetime loginurl with his or her email input. Then email includes onetime loginurl is sent by Sendgrid API.

>Report file management.

Nowadays we can choose storage. AWS, Azure, GCP. But that costs money. Even if insignificant. So I design report file management with Google Drive API.
Report files are uploaded to individual google drive. For example, mine or professor storage.

### Architecture
 - Layerd Architecture x CQRS like I usually do. I am usually developing web applications with Java or C#.

## Directory Structure Sumary

[Abour this directory.](https://github.com/TsJazz27Sumin/nakamuratamara/tree/master/songcycle/apps/student)

- decorators
  - Decorator for logging and authorization process.
- forms
  - Classes for forms in html.
- functions
  - Commonly used logic is called from mutiple class.
- models
  - Models corresponds to tables in database.
- queries
  - Second Layer : Search process. That corresponds to Query of CQRS. To take charge of select database access.
- repositories
  - Third Layer : To take charge of insert, update, delete database access. 
- services
  - Second Layer : To take charge of business logic about insert, update, delete procss. That corresponds to Command of CQRS.
- templates
  - HTML Templates.
- templatetags
  - Functions for view process in html templates.
- views
  - First Layer : That corresponds to Controller of MVC. In django, that is called View.

## Requirement
 - Please use Linux OS. [Because Windows OS has issue about python.](https://github.com/django-helpdesk/django-helpdesk/issues/621) I tried to use ajax in django. But don't work except JsonResponse. 
 - My development environment is Mac OS : Mojave.

## Author

[TsJazz27Sumin](https://github.com/TsJazz27Sumin)
