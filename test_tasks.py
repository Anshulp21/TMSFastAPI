import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
# In test_tasks.py
def test_login():
    response = client.post("/login/", json={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    assert "access_token" in response.json()



def test_list_tasks_sorted_by_creation():
    token = client.post("/login/", json={"username": "admin", "password": "admin"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    # Create multiple tasks
    client.post("/tasks/", json={"title": "Task 1", "description": "Desc 1", "status": "To Do", "due_date": "2024-11-30"}, headers=headers)
    client.post("/tasks/", json={"title": "Task 2", "description": "Desc 2", "status": "In Progress", "due_date": "2024-12-01"}, headers=headers)

    # List tasks
    response = client.get("/tasks/", headers=headers)
    tasks = response.json()
    assert response.status_code == 200
    assert len(tasks) >= 2
    # Check if sorted by creation time (descending)
    assert tasks[0]["created_at"] >= tasks[1]["created_at"]





def test_create_task():
    token = client.post("/login/", json={"username": "admin", "password": "admin"}).json()["access_token"]
    response = client.post("/tasks/", headers={"Authorization": f"Bearer {token}"}, json={
        "title": "Sample Task",
        "due_date": "2024-12-01"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Sample Task"



def test_update_task():
    token = client.post("/login/", json={"username": "admin", "password": "admin"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    # Create a task
    task_data = {
        "title": "Task to Update",
        "description": "Update test description",
        "status": "To Do",
        "due_date": "2024-11-30"
    }
    created_task = client.post("/tasks/", json=task_data, headers=headers).json()
    task_id = created_task["id"]

    # Update the task
    update_data = {
        "title": "Updated Task Title",  # Include required fields
        "description": "Updated description",
        "status": "In Progress",
        "due_date": "2024-12-01"
    }
    response = client.put(f"/tasks/{task_id}", json=update_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] == "In Progress"
    assert response.json()["title"] == "Updated Task Title"


