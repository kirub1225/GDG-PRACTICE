import json
import os


class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    # Serialization 
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

    # Deserialization
    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["title"], data["completed"])


class TodoManager:
    def __init__(self, filename="todo.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    # Load tasks from JSON file
    def load_tasks(self):
        if not os.path.exists(self.filename):
            self.tasks = []
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            self.tasks = []

    # Save tasks to JSON file
    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    # Generate next unique ID
    def generate_id(self):
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    # Add new task
    def add_task(self, title):
        new_task = Task(self.generate_id(), title)
        self.tasks.append(new_task)
        self.save_tasks()

    # View all tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for task in self.tasks:
            status = "✔ Completed" if task.completed else "✘ Not Completed"
            print(f"ID: {task.id} | Title: {task.title} | Status: {status}")

    # Update task
    def update_task(self, task_id, new_title=None, completed=None):
        for task in self.tasks:
            if task.id == task_id:
                if new_title is not None:
                    task.title = new_title
                if completed is not None:
                    task.completed = completed
                self.save_tasks()
                return True
        return False

    # Delete task
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                return True
        return False
