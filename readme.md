# Task Management API
This is a FastAPI-based Task Management System (TMS) where users can create, update, delete, and fetch tasks. The API also includes authentication via login.

# Features
User Login: Secure login to access the task management features.
Task Creation: Create new tasks with a title, description, and status.
Get All Tasks: View a list of all tasks.
Get Task by ID: Retrieve task details by providing its ID.
Update Task: Modify task details, including status.
Delete Task: Remove a task from the system.

Setup Instructions
1. Clone the Repository
Clone the project from GitHub:

git clone https://github.com/Anshulp21/TMSFastAPI.git
2. Create a Virtual Environment
Set up a virtual environment in your project folder:

python -m venv venv

3. Install Dependencies
Activate the virtual environment and install the required dependencies:

venv\Scripts\activate

pip install -r requirements.txt


4. Set Up Database
Before running the application, configure your database connection.

Create a .env file in the root of the project directory and add the following:


DATABASE_URL=postgresql://username:password@localhost:5432/task_db
This URL connects to a PostgreSQL database. You may need to modify the credentials or database name according to your setup.

6. Running the Application
Once everything is set up, you can run the FastAPI application using the following command:

uvicorn main:app --reload

The application will be accessible at http://127.0.0.1:8000/.

**API Endpoints**



# Login
URL: http://127.0.0.1:8000/login
Method: POST
Request Body:
{
  "username": "admin",
  "password": "admin"
}
Description: Authenticates the user and returns a JWT token.


# Create Task
URL: http://127.0.0.1:8000/tasks
Method: POST
Request Body:
{
  "title": "Task Title",
  "description": "Task description",
  "status": "To Do",
  "due_date": "2024-11-30"
}
Description: Creates a new task.


# Get All Tasks

URL: http://127.0.0.1:8000/tasks
Method: GET
Description: Retrieves all tasks.


# Get Task by ID
URL: http://127.0.0.1:8000/tasks/{task_id}
Method: GET
Description: Fetches a task by its ID.


# Update Task
URL: http://127.0.0.1:8000/tasks/{task_id}
Method: PUT
Request Body:

Description: Updates a task by its ID. You can update any field (e.g., status).

# Delete Task
URL: http://127.0.0.1:8000/tasks/{task_id}
Method: DELETE
Description: Deletes a task by its ID.


**Running Tests**
The project includes test cases for task management functionality. To run the tests, use pytest:

pytest test_tasks.py


Make sure your virtual environment is activated and all dependencies are installed before running the tests.



