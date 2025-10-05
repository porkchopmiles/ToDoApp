import React from "react";

function TaskItem({ task, toggleTask, deleteTask }) {
  return (
    <li>
      <span
        className={task.completed ? "completed" : ""}
        onClick={() => toggleTask(task.id, task.completed)}
      >
        {task.title}
      </span>
      <button onClick={() => deleteTask(task.id)}>Delete</button>
    </li>
  );
}

export default TaskItem;
