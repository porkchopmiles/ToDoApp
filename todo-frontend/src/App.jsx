import React, { useState, useEffect } from "react";
import axios from "axios";
import './App.css'
import TaskList from "./components/TaskList";

const BASE_URL = "http://127.0.0.1:5000";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  useEffect(() => {
    axios.get(`${BASE_URL}/tasks`)
      .then(res => setTasks(res.data))
      .catch(err => console.error(err));
  }, []);

  const addTask = () => {
    if (!title) return;
    axios.post(`${BASE_URL}/tasks`, { title })
      .then(res => setTasks([...tasks, res.data]))
      .catch(err => console.error(err));
    setTitle("");
  };

  const toggleTask = (id, completed) => {
    axios.put(`${BASE_URL}/tasks/${id}`, { completed: !completed })
      .then(res => setTasks(tasks.map(t => t.id === id ? res.data : t)))
      .catch(err => console.error(err));
  };

  const deleteTask = (id) => {
    axios.delete(`${BASE_URL}/tasks/${id}`)
      .then(() => setTasks(tasks.filter(t => t.id !== id)))
      .catch(err => console.error(err));
  };

  return (
    <div className="container">
      <h1>My To-Do List</h1>
      <div style={{ display: 'flex', marginBottom: '1rem' }}>
        <input
          type="text"
          placeholder="Add a new task..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <button onClick={addTask}>Add</button>
      </div>
      <TaskList
        tasks={tasks}
        toggleTask={toggleTask}
        deleteTask={deleteTask}
      />
    </div>
  );
}

export default App;