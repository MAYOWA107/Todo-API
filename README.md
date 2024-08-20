A simple and efficient Todo application built using Django Rest Framework, allowing users to manage their tasks effectively. The app provides functionality to create, update, delete, and filter tasks by status. It features user authentication, ensuring that tasks are securely managed per user. Ideal for personal task management or as a backend for a more extensive productivity application.

Features
User Authentication: Secure login and registration for users.
Task Management: Create, update, and delete tasks.
Status Filtering: Filter tasks by their status (e.g., in progress, completed, pending).
RESTful API: Fully functional API built with Django Rest Framework.
Installation

Clone the repository:
git clone https://github.com/MAYOWA107/Todo-API.git

Create a virtual environment and activate it:
python -m venv venv

venv\Scripts\activate #on windows

Install the required dependencie
pip install -r requirements.txt

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Create a superuser:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Usage
Access the API at http://127.0.0.1:8000/.
Use the Django admin to manage users and tasks: http://127.0.0.1:8000/admin/.
API Endpoints
GET /todos/: List all tasks.
POST /todos/: Create a new task.
GET /todo/<id>/: Retrieve a task by its ID.
PUT /todo/<id>/: Update a task by its ID.
DELETE /todo/<id>/: Delete a task by its ID.
Contributing
Feel free to submit issues, fork the repository, and send pull requests. For major changes, please open an issue first to discuss what you would like to change.
