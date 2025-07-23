from .models import Task
from .manager import TaskManager
from datetime import datetime

manager = TaskManager()

def main_menu():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Mark as Completed")
        print("5. Delete Task")
        print("6. Clear All Tasks")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            while True:
                due_date = input("Due Date (YYYY-MM-DD): ")
                if is_valid_date(due_date):
                    break
                else:
                    print("Invalid date format. Please enter in YYYY-MM-DD format: ")
            while True:
                priority = input("Priority (Low/Medium/High): ").capitalize()
                if is_valid_priority(priority):
                    break
                else:
                    print("Invalid priority. Please enter Low, Medium, or High: ")
            manager.add_task(title, description, due_date, priority)
            print("Task added!")

        elif choice == "2":
            print("Sort by (default is Due Date):")
            print("1. Due Date")
            print("2. Priority")
            print("3. Status")

            sort_choice = input("Choose sort option: ")

            if sort_choice == "1":
                sort_by = "due_date"
            elif sort_choice == "2":
                sort_by = "priority"
            elif sort_choice == "3":
                sort_by = "status"
            else:
                sort_by = "due_date"

            manager.list_tasks(sort_by)
        
        elif choice == "3":
            task_id = input("Task ID: ")
            field = input("Field to update (title/description/due_date/priority/status): ")
            value = input("New value: ")
            while True:
                if field in ["title", "description", "due_date", "priority", "status"]:
                    manager.update_task(task_id, {field: value})
                    print("Task updated.")
                    break
                else:
                    print('Invalid field. Choose from "title", "description", "due_date", "priority", "status".')

        elif choice == "4":
            task_id = input("Task ID to complete: ")
            manager.mark_complete(task_id)
            print("Task marked as completed.")

        elif choice == "5":
            task_id = input("Task ID to delete: ")
            manager.delete_task(task_id)
            print("Task deleted.")

        elif choice == "6":
            confirm = input("Are you sure you want to delete ALL tasks? (y/n): ").lower()
            if confirm == 'y':
                manager.clear_tasks()
            else:
                print("Clear operation cancelled.")

        elif choice == "0":
            break
        else:
            print("Invalid choice. Please select a number from 0-6.")


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")  #expected format, like 2024-07-23
        return True
    except ValueError:
        return False

def is_valid_priority(priority):
    return priority.upper() in ["LOW", "MEDIUM", "HIGH"]