import json
import os

# File to save tasks
TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

# View existing tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task['done'] else "✗"
            print(f"{index}. [{status}] {task['name']}")

# Add a new task
def add_task(tasks):
    task_name = input("Enter the task name: ").strip()
    if task_name:
        tasks.append({"name": task_name, "done": False})
        print(f"Task '{task_name}' added.")
    else:
        print("Task name cannot be empty.")

# Mark task as done/undone
def toggle_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to toggle: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['done'] = not tasks[task_index]['done']
            status = "done" if tasks[task_index]['done'] else "undone"
            print(f"Task '{tasks[task_index]['name']}' marked as {status}.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task['name']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== To-Do List ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done/Undone")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            toggle_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()