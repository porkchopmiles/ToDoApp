import requests

BASE_URL = "http://127.0.0.1:5000"

# Get all tasks
response = requests.get(f"{BASE_URL}/tasks")
print("Tasks:", response.json())

# Add a new task
new_task = {"title": "Learn Flask"}
response = requests.post(f"{BASE_URL}/tasks", json=new_task)
print("Added Task:", response.json())

# Update task completion
task_id = response.json()["id"]
update = {"completed": True}
response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update)
print("Updated Task:", response.json())

# Delete task
response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
print("Delete Response:", response.json())
