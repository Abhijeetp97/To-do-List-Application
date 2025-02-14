import json
from datetime import datetime
from typing import List, Dict, Any, Optional

def show_menu() -> None:
    """
    Display the menu options.
    """
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Mark a task as completed")
    print("5. View completed tasks")
    print("6. Edit a task")
    print("7. Filter tasks by category")
    print("8. Save tasks")
    print("9. Load tasks")
    print("10. Exit")

def add_task(tasks: List[Dict[str, Any]]) -> None:
    """
    Add a new task to the to-do list with category, priority, and due date.
    Keeps prompting until valid inputs are provided.
    """
    while True:
        task = input("Enter the task: ").strip()
        if not task:
            print("Task description cannot be empty. Please try again.")
            continue

        category = input("Enter the category (e.g., Work, Personal): ").strip()
        if not category:
            print("Category cannot be empty. Please try again.")
            continue

        priority = input("Enter the priority (high, medium, low): ").strip().lower()
        if priority not in ['high', 'medium', 'low']:
            print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
            continue

        due_date_input = input("Enter the due date (YYYY-MM-DD, leave empty if not applicable): ").strip()
        if due_date_input:
            try:
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue
        else:
            due_date = None

        tasks.append({
            "task": task,
            "category": category,
            "priority": priority,
            "due_date": due_date,
            "completed": False
        })
        print(f"Task '{task}' added under category '{category}' with priority '{priority}' and due date '{due_date}'.")
        break

def format_due_date(due_date: Optional[datetime.date]) -> str:
    """
    Format the due_date to a string in YYYY-MM-DD format, or return 'None' if no due date.
    """
    return due_date.strftime("%Y-%m-%d") if due_date else "None"

def view_tasks(tasks: List[Dict[str, Any]]) -> None:
    """
    Display the current list of tasks with their categories, priorities, and due dates.
    """
    if tasks:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, start=1):
            if not task["completed"]:
                due_date_str = format_due_date(task["due_date"])
                print(f"{i}. {task['task']} - Category: {task['category']} - Priority: {task['priority']} - Due Date: {due_date_str}")
    else:
        print("\nNo tasks in the list.")

def remove_task(tasks: List[Dict[str, Any]]) -> None:
    """
    Remove a task from the to-do list by its number.
    """
    if not tasks:
        print("No tasks to remove.")
        return

    while True:
        view_tasks(tasks)
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['task']}' removed.")
                break
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

def mark_task_completed(tasks: List[Dict[str, Any]]) -> None:
    """
    Mark a task as completed by its number.
    """
    if not tasks:
        print("No tasks to mark as completed.")
        return

    while True:
        view_tasks(tasks)
        try:
            task_num = int(input("Enter the number of the task to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as completed.")
                break
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

def view_completed_tasks(tasks: List[Dict[str, Any]]) -> None:
    """
    Display the list of completed tasks with their categories, priorities, and due dates.
    """
    completed_tasks = [task for task in tasks if task["completed"]]
    if completed_tasks:
        print("\nCompleted Tasks:")
        for i, task in enumerate(completed_tasks, start=1):
            due_date_str = format_due_date(task["due_date"])
            print(f"{i}. {task['task']} - Category: {task['category']} - Priority: {task['priority']} - Due Date: {due_date_str}")
    else:
        print("\nNo completed tasks in the list.")

def edit_task(tasks: List[Dict[str, Any]]) -> None:
    """
    Edit the description, category, priority, or due date of a task by its number.
    """
    if not tasks:
        print("No tasks available to edit.")
        return

    while True:
        view_tasks(tasks)
        try:
            task_num = int(input("Enter the number of the task to edit: "))
            if 1 <= task_num <= len(tasks):
                task = tasks[task_num - 1]
                new_description = input(f"Enter the new description (leave empty to keep '{task['task']}'): ").strip()
                if new_description:
                    task["task"] = new_description

                new_category = input(f"Enter the new category (leave empty to keep '{task['category']}'): ").strip()
                if new_category:
                    task["category"] = new_category

                new_priority = input(f"Enter the new priority (high, medium, low, leave empty to keep '{task['priority']}'): ").strip().lower()
                if new_priority:
                    if new_priority in ['high', 'medium', 'low']:
                        task["priority"] = new_priority
                    else:
                        print("Invalid priority. Please try editing the task again.")
                        continue

                new_due_date_input = input(f"Enter the new due date (YYYY-MM-DD, leave empty to keep '{task['due_date']}'): ").strip()
                if new_due_date_input:
                    try:
                        task["due_date"] = datetime.strptime(new_due_date_input, "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD and try editing the task again.")
                        continue

                print(f"Task '{task['task']}' updated.")
                break
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

def filter_tasks_by_category(tasks: List[Dict[str, Any]]) -> None:
    """
    Display tasks filtered by a specific category.
    """
    category = input("Enter the category to filter by: ").strip()
    filtered_tasks = [task for task in tasks if task["category"].lower() == category.lower() and not task["completed"]]
    if filtered_tasks:
        print(f"\nTasks in category '{category}':")
        for i, task in enumerate(filtered_tasks, start=1):
            due_date_str = task["due_date"].strftime("%Y-%m-%d") if task["due_date"] else "None"
            print(f"{i}. {task['task']} - Priority: {task['priority']} - Due Date: {due_date_str}")
    else:
        print(f"\nNo tasks found in category '{category}'.")

def save_tasks(tasks: List[Dict[str, Any]], filename: str) -> None:
    """
    Save the tasks to a JSON file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(tasks, file, default=str)
        print(f"Tasks saved to {filename}.")
    except IOError as e:
        print(f"Error saving tasks to {filename}: {e}")

def load_tasks(filename: str) -> List[Dict[str, Any]]:
    """
    Load the tasks from a JSON file.
    Returns a list of tasks.
    """
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            for task in tasks:
                if task["due_date"]:
                    task["due_date"] = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
        print(f"Tasks loaded from {filename}.")
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error loading tasks from {filename}. Starting with an empty task list.")
        tasks = []
    return tasks


def main() -> None:
    """
    Main function to run the To-Do List application.
    """
    filename = "tasks.json"
    tasks = load_tasks(filename)
    
    while True:
        show_menu()
        while True:
            choice = input("Enter your choice (1-10): ").strip()
            if choice in [str(i) for i in range(1, 11)]:
                break      
                
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            view_completed_tasks(tasks)
        elif choice == '6':
            edit_task(tasks)
        elif choice == '7':
            filter_tasks_by_category(tasks)
        elif choice == '8':
            save_tasks(tasks, filename)
        elif choice == '9':
            tasks = load_tasks(filename)
        elif choice == '10':
            save_tasks(tasks, filename)
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 10.")

if __name__ == "__main__":
    main()