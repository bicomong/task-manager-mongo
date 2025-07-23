from task_manager.db import tasks_collection
from task_manager.models import Task
from task_manager.manager import TaskManager

manager = TaskManager()

tasks_collection.delete_many({})

superhero_tasks = [
    {
        "title": "Stop the Joker's bank heist",
        "description": "Gotham Central Bank is under attack. Respond immediately.",
        "due_date": "2025-07-25",
        "priority": "High",
        "status": "Pending"
    },
    {
        "title": "Rescue civilians from burning building",
        "description": "Building on fire in Midtown. Superman to assist with evacuation.",
        "due_date": "2025-07-24",
        "priority": "High",
        "status": "In Progress"
    },
    {
        "title": "Brief Avengers on new threat",
        "description": "Meeting at Stark Tower. Discuss incoming alien signals.",
        "due_date": "2025-07-26",
        "priority": "Medium",
        "status": "Pending"
    },
    {
        "title": "Fix Batmobile engine",
        "description": "Need replacement parts from Lucius Fox.",
        "due_date": "2025-07-30",
        "priority": "Low",
        "status": "Pending"
    },
    {
        "title": "Update S.H.I.E.L.D. database",
        "description": "Add new meta-humans from recent encounters.",
        "due_date": "2025-07-28",
        "priority": "Medium",
        "status": "Completed"
    },
    {
        "title": "Scout alien activity in Queens",
        "description": "Spider-Man to patrol area for anomalies.",
        "due_date": "2025-07-27",
        "priority": "Low",
        "status": "In Progress"
    },
    {
        "title": "Train new X-Men recruits",
        "description": "Cyclops and Storm to lead tactical drills.",
        "due_date": "2025-08-01",
        "priority": "Medium",
        "status": "Pending"
    },
    {
        "title": "Deactivate Ultron fragment",
        "description": "Analyze and destroy remnant AI from Sokovia.",
        "due_date": "2025-07-29",
        "priority": "High",
        "status": "Pending"
    },
    {
        "title": "Clean Fortress of Solitude",
        "description": "Dust off Kryptonian relics and re-index archives.",
        "due_date": "2025-08-03",
        "priority": "Low",
        "status": "Pending"
    },
    {
        "title": "Write mission report for Justice League",
        "description": "Summarize Metropolis incident for Batman’s records.",
        "due_date": "2025-07-31",
        "priority": "Medium",
        "status": "In Progress"
    }
]

for task_data in superhero_tasks:
    task = Task(
        task_id=manager.generate_task_id(),
        title=task_data["title"],
        description=task_data["description"],
        due_date=task_data["due_date"],
        priority=task_data["priority"],
        status=task_data["status"]
    )
    tasks_collection.insert_one(task.to_dict())

print("Tasks successfully inserted!")
