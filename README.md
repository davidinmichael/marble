# Blog Web Application

A simple blog web application built with Django.

## Features
- User authentication (register, login, logout)
- Create, read, update, and delete blog posts
- Filter blog posts by categories or tags
- Pagination of blog posts
- Search functionality

## Getting Started
To get a copy of this project up and running on your local machine, follow these steps:

### Prerequisites
- Python (3.6 or higher)
- pip

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/davidinmichael/marble.git
   ```
2. Change into the project directory:
   ```
   cd marble
   ```
3. Create a virtual environment:
   ```
   python -m venv env
   ```
4. Activate the virtual environment:
   ```
   source env/bin/activate
   ```
5. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Run the migrations:
   ```
   python manage.py migrate
   ```
7. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
8. Start the development server:
   ```
   python manage.py runserver
   ```
9. Access the application at `http://localhost:8000`

## Usage
- Register a new account by clicking on the "Register" button on the home page.
- Login to your account to create, edit, or delete blog posts.
- Browse existing blog posts by category, tag, or search.
- Logout by clicking on the "Logout" button on the navigation bar.

## Built With
- Python - The programming language
- Django - The web framework used
- HTML - The web structure language
- Bootstrap - The front-end library used for styling

## Acknowledgments
- This project was inspired by [Django Girls Tutorial](https://tutorial.djangogirls.org)
- Thanks to all open source contributors for their great work!