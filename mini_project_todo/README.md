# CLI Todo App (OOP + JSON)

## Project Overview

This is a simple Command Line Interface (CLI) Todo application built using Object-Oriented Programming (OOP) in Python.

The application allows users to:
- Add tasks
- View tasks
- Update tasks
- Delete tasks

All tasks are stored in a local `todo.json` file.  
When the program restarts, previously saved tasks are automatically loaded.

---

## Project Structure

todo_app/
│
├── main.py        # CLI interface
├── todo.py        # OOP classes and business logic
├── todo.json      # Local JSON storage
├── README.md
└── .gitignore

---

## How to Run the Project

1. Make sure Python 3 is installed.
2. Open terminal inside the project folder.
3. Run the following command:

python main.py

4. The menu will appear:

1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Exit

Follow the on-screen instructions.

---

## Features

- Add new task with unique ID
- View all saved tasks
- Update task title
- Mark task as completed or not completed
- Delete task by ID
- Data persistence using JSON file

---

## JSON Data Persistence

The application uses a local file named:

todo.json

Example JSON structure:

[
    {
        "id": 1,
        "title": "Study OOP",
        "completed": false
    }
]

All changes are saved automatically after adding, updating, or deleting tasks.

---

## JSON and Object Conversion

### Serialization (Object → JSON)

Each Task object is converted into a dictionary using:

to_dict()

Then it is saved to todo.json using:

json.dump()

Flow:

Task Object → Dictionary → JSON File

---

### Deserialization (JSON → Object)

When the program starts:

1. The JSON file is read using json.load()
2. JSON data becomes a list of dictionaries
3. Each dictionary is converted back into a Task object using:

from_dict()

Flow:

JSON File → Dictionary → Task Object

This ensures data remains available after restarting the program.

---

## Technologies Used

- Python 3
- Built-in json module
- Built-in os module
- Command Line Interface (CLI)

