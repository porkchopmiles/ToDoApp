from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password", # Deleted for github
    database="todo_app"
)

# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    cursor = db.cursor()
    cursor.execute("SELECT id, title, completed FROM tasks")
    rows = cursor.fetchall()
    cursor.close()
    tasks = [{"id": r[0], "title": r[1], "completed": bool(r[2])} for r in rows]
    return jsonify(tasks)

# Add task
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data["title"]
    cursor = db.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    db.commit()
    task_id = cursor.lastrowid
    cursor.close()
    return jsonify({"id": task_id, "title": title, "completed": False})

# Update task
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.get_json()
    completed = data["completed"]
    cursor = db.cursor()
    cursor.execute("UPDATE tasks SET completed=%s WHERE id=%s", (completed, id))
    db.commit()
    cursor.close()
    return jsonify({"id": id, "completed": completed})

# Delete task
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (id,))
    db.commit()
    cursor.close()
    return jsonify({"message": "Deleted"})

if __name__ == "__main__":
    app.run(debug=True)
