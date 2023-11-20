A group-project from the subject DAT310 Webprogramming while pursuing a bachelors degree at University of Stavanger. Main goal of the project was to make a website. This website is for adding tasks/ToDo's, setting reminders for when they need to be done etc.

Grade: A

# How To Run:

## Installation Guide for new Virtual Env
### 1: Create virtual environment:
```python3 -m venv venv```

### 2: Activate venv (MAC):
```source venv/bin/activate```

### 3: Install packages in the venv:

#### Flask
```pip install Flask Flask_SQLAlchemy Flask-Bcrypt Flask-JWT-Extended Flask-Cors python-dateutil```


#### Vue (```cd frontend``` before running!)
```npm install```


## Running the application:

### Terminals
Open two terminals:
One for frontend &
One for running run.py

#### Frontend terminal run (frontend directory):
```cd frontend```

```npm run serve```

#### Backend terminal run (root directory):
```python run.py```

### Now the application should run on: ```http://localhost:8080/```
<br>

# Instructions For Testing:

## User Details:
Username: TestUser <br>
Password: Testuser1

## Navigating the website:
Login with user details to view dashboard.<br>
Create categories or todo's on dashboard.<br>
Edit/Update or Delete categories or todo's.<br>
Sort todo's after your desired criteria.<br>
Enter profile page to add/change profile picture.


# List of functionalities:

## Main Technologies:
Vue <br>
Vuex<br>
Vue-router<br>
Axios: To allow communication between frontend and backend.<br>
Flask<br>
Flask-JWT: Authentication tokens <br>
Bootstrap

## Shortened list of functionalities:
- Register user
- Login user
- Create Todo's
    - Sort, Edit, and Delete Todo's
- Create Categories
    - Edit, and Delete Categories
- View Todo's and Categories
- View Profile page
    - Upload profile picture

## Functionalities & Criterias met

### Register
Register a user with username and password. Password has certain restrictions for protection.
Bcrypt used to generate password hashes to be stored in the database.

### Login
Login with the registered user details. Data requested from frontend login form.
Checks input against database details, then creates an access token using flask JWT.
This token is used to authenticate the user and give access to restricted pages.

### JS Form Validation
Frontend form validation by using the "required" attribute on forms.
Error message displays if a forms input field is missing or contains wrong format.

### Sorting
User can sort by many criterias: Date added, Alphabetical A-Z, Priority, Due Date, all of these reversed, and by Category

### Sorting Preferences Saved/Stored
Sorting preferences are saved using Web Storage API (localStorage). Vuex is
used to store different states in our program, for example "sortOrder" (store.js).

### Update and Delete
Users can update their Todo's, as well as delete them. The changes are stored in the database.

### AJAX Request used
AJAX requests are used. This is by using Axios, which allows frontend to communicate with backend.
For example when logging in, axios.post(/login) is used to post the form inputs "username" and "password" to backend for storing in the database.

### Components
Vue Components are used to create the fundamentals for the different pages in our app.
Some of these components are imported and used in the corresponding views files.

### Layout
 Used semantic tags where we think it fits.
 Used mainly bootstrap for layout, and a bit of css for extra customazation.
 Used d-flex from Bootstrap. (flex)
 Fluid layout - website is responsive to phone sized displays.
 Used absolute positioning on the logo in the header.

### Data stored, updated, and deleted
Data such as user details, todo details, and categories are stored in the database.
Todo's can be edited, updated, and deleted.

### Rest API
We have defined routes for the API, such as /login and /todos/<"int:todo_id">. Used POST, GET, DELETE,and PUT HTTP methods. Stateless API with the use of JWT (token needed to identify and authorize user).

### Server-side Validation
Validation for required fields. Validation for reasonable restrictions for passwords. User access token validation required to access certain pages.

### Errors displayed
Errors get displayed if an error occurs, both server and client side.

### Authentication
JWT authentication is used to authorize users. The created user access token must be valid for the user to be able to access certain features/pages. The token is created when logging in, and removed when logging out. The token is stored in localStorage.

### Access Control
Routes are protected based on JWT authentication. Users can only view, modify, and delete their own todos and categories.

### Extra Features
- Vue components
- Vue Router
- VueX
- Storage and display of dates
- Storage and handling of user uploaded images
- Due date and countdown until this date and time
- Hashed passwords

### General application functionality:
- Users are stored in the database with a hashed password for security.
    - When logging in, a JWT access token is connected to the logged in user to authenticate them for restricted routes.
- Preferences for sorting todos are stored in localStorage and remembered when revisiting the site
    - Stored with the use of VueX
- New Todo's can be added on the Dashboard page
    - Todo attributes:
        - ID
        - user_id
        - task
        - completed
        - createdAt
        - updatedAt
        - priority
        - due_date
        - category_id
- New categories can be created on the Dashboard page
    - Category attributes:
        - ID
        - name
        - user_id
- Password restrictions on registration:
    - If password does not apply to the following restrictions, an error will occur and be displayed:
        - At least 8 characters
        - At least 1 upper case letter
        - At least 1 number
- The application is a SPA (Single Page Application), and uses AJAX calls
    - AJAX calls for POST, GET, PUT, and DELETE are used, such as registration of users, displaying todo's, and uploading a profile picture.
- Validation:
    - Both server and client side validation is done.
    - If a form is missing required input, JS Form validation will display an error message
    - If user details do not meet specific restrictions, a meaningful error message will be displayed
