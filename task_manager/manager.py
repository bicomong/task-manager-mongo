from .db import tasks_collection
from .models import Task

class TaskManager:
    def add_task(self, title, description, due_date, priority):
        task_id = self.generate_task_id()
        task = Task(task_id, title, description, due_date, priority)
        tasks_collection.insert_one(task.to_dict())
        print(f"Task {task_id} added successfully.")

    def list_tasks(self, sort_by=None):
        sort_field = sort_by if sort_by in ["priority", "due_date", "status"] else "due_date"

        #convert priority
        priority_order = {"Low": 1, "Medium": 2, "High": 3}

        tasks = list(tasks_collection.find())

        if sort_field == "priority":
            tasks.sort(key=lambda x: priority_order.get(x.get("priority", ""), 0))
        elif sort_field == "due_date":
            from datetime import datetime
            tasks.sort(key=lambda x: datetime.strptime(x.get("due_date", "9999-12-31"), "%Y-%m-%d"))
        elif sort_field == "status":
            status_order = {"Pending": 1, "In Progress": 2, "Completed": 3}
            tasks.sort(key=lambda x: status_order.get(x.get("status", ""), 0))

        for task in tasks:
            task_id = task.get("task_id", "")
            title = task.get("title", "")
            filter_value = task.get(sort_field, "N/A")
            print(f"{task_id} - [{filter_value}] - {title}")

    def update_task(self, task_id, updates):
        tasks_collection.update_one({"task_id": task_id}, {"$set": updates})

    def delete_task(self, task_id):
        tasks_collection.delete_one({"task_id": task_id})

    def mark_complete(self, task_id):
        self.update_task(task_id, {"status": "Completed"})

    def generate_task_id(self):
        #fetch all task_id find the maximum
        tasks = tasks_collection.find({}, {"task_id": 1})
        ids = [int(task["task_id"][1:]) for task in tasks if task.get("task_id")]
        next_id = max(ids) + 1 if ids else 1
        return f"T{next_id:03d}"  #formats like T001, T002...

    def clear_tasks(self):
        result = tasks_collection.delete_many({})
        print(f"Cleared {result.deleted_count} tasks from the database.")
