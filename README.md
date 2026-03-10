# 📋 Python Task Manager

A command-line **Task Manager application built in Python** that allows users to manage tasks efficiently with features such as **priority-based task management, undo functionality, and JSON-based persistence**.

The application uses a **priority queue (heap)** to organize tasks based on their priority and supports saving and loading tasks using JSON files.

---

# 🚀 Features

- Add new tasks with title, status, deadline, and priority
- Delete tasks
- Edit existing tasks
- Undo the last action (add, delete, or edit)
- View all tasks
- View tasks ordered by priority
- Save tasks to a JSON file
- Load tasks from a JSON file
- Priority-based task organization using **Heap (Priority Queue)**

---

# 🧠 Data Structures Used

This project demonstrates the use of several core data structures:

### 1. List
Stores all tasks in memory.

```
tasks = []
```

Each task is represented as a dictionary:

```
{
    "title": "Complete Assignment",
    "status": "Pending",
    "deadline": "2026-03-15",
    "priority": 1
}
```

---

### 2. Priority Queue (Heap)

Implemented using Python's **heapq** module to manage tasks based on priority.

Lower priority number = Higher importance.

Example:

```
Priority 1 → Highest Priority
Priority 3 → Lower Priority
```

---

### 3. Stack

Used to implement the **Undo functionality**.

```
undo_stack = []
```

The stack stores actions such as:

- Add
- Delete
- Edit

This allows reversing the most recent operation.

---

# 🛠 Technologies Used

- **Python 3**
- `heapq` – for priority queue implementation
- `json` – for saving and loading tasks
- Command Line Interface (CLI)

No external libraries are required.

---

# 📂 Project Structure

```
Task Manager Using Data Structures/
│
├── taskManager.py
└── sample.json
```

---

# ▶️ How to Run the Program

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/python-task-manager-cli.git
cd Task Manager Using Data Structures
```

---

### 2️⃣ Run the Program

```bash
python taskManager.py
```

---

# 📌 Menu Options

When the program runs, you will see the following options:

```
1. Add Task
2. Delete Task
3. Edit Task
4. Undo Last Action
5. View All Tasks
6. View Tasks by Priority
7. Load Tasks from JSON
8. Save Tasks to JSON
9. Exit
```

Users can interact with the application by entering the corresponding number.

---

# 💾 JSON File Example

Tasks can be saved in JSON format.

Example:

```json
[
    {
        "title": "Finish Project",
        "status": "Pending",
        "deadline": "2026-04-01",
        "priority": 1
    },
    {
        "title": "Buy Groceries",
        "status": "Completed",
        "deadline": "2026-03-12",
        "priority": 3
    }
]
```

---

# 🔄 Undo Functionality

The program supports **undoing the most recent action**.

Supported undo operations:

- Undo task addition
- Undo task deletion
- Undo task edit

This is implemented using a **stack-based approach**.

---

# 🎯 Learning Outcomes

This project helps demonstrate:

- Priority Queue implementation using `heapq`
- Stack-based undo operations
- File persistence using JSON
- CLI-based application design
- Basic task management systems
