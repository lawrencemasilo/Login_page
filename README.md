# Django Login Page

This Django web application provides a user authentication system that allows users to log in and create new accounts if they don't exist.

## Features

- User authentication (login and registration).
- Secure password storage.
- User-friendly interface.
- Successful login redirection.

## Screenshots

### Login Page

![Login Page](images/Screenshot%20(16).png)
![Login Page](images/Screenshot%20(14).png)
![Login Page](images/Screenshot%20(15).png)

### Create User Page

![Create User Page](images/Screenshot%20(19).png)
![Create User Page](images/Screenshot%20(24).png)
![Create User Page](images/Screenshot%20(23).png)

### Successful Login

![Successful Login](images/Screenshot%20(25).png)
![Successful Login](images/Screenshot%20(26).png)

## Installation

   1. Navigate to a directory of your choice/create new directory:

      ```bash
      cd your-empty-directory

   2. Install a Virtual Environment:

      ```bash
      pip install virtualenv

   3. Create the virtual environment:

      ```bash
      python -m venv venv

   4. Navigate to the venv:

      ```bash
      cd your-directory/venv

   5. Activate the virtual environment:

      On Windows:
      ```bash
      Scripts\activate


   6. Clone the repository into venv directory:

      ```bash
      git clone https://github.com/lawrencemasilo/Login_page.git

   7. Navigate to the project directory:

      ```bash
      cd Login_page/login_page
   
   8. Install dependencies:
      ```bash
      pip install -r requirements.txt

   9. Apply Database Migrations:

      ```bash
      python manage.py migrate

   10. Start the Development Server:
    
      python manage.py runserver

## Usage
Access the application in your web browser at http://127.0.0.1:8000/login/

1. Login: Use existing credentials to log in.

2. Create User: Click the "Sign up" link on the login page to create a new user account.

3. Successful Login: Upon successful login, you will be redirected to a welcome page with your username.
