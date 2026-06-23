# Example dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "Mumbai"
}
print(person["name"])  # prints "Alice"
print(person["age"])  # prints 30

# todo_persistent.py
import os

# File where tasks will be sum
TASKS_FILE = "tasks.txt"

# Dictionary to store tasks: key = task text, value = status("done" or "pending")
tasks = {}


# load_task()
# Checks if the file tasks.txt exists
# If yes, reads each line
# Each line has "task|status" - we split on | and store in the dictionary
def load_tasks():
    """Load tasks from the file into the dictionary"""
    global tasks
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    # Format: "task|status"
                    parts = line.split("|")
                    if len(parts) == 2:
                        task, status = parts[0], parts[1]
                        tasks[task] = status
       

# save_tasks()
# Writes each directionary entry to the file in the format "task|status\n"

# task dictioanry
# Key: the task text(e.g., "Buy milk")
# Value: "pending" or "done"                 
def save_tasks():
    """Save tasks dictionary to the file"""
    with open(TASKS_FILE, "w") as file:
        for task, status in tasks.items():
            file.write(f"{task}|{status}\n")
            
def view_tasks():
    """Display all tasks with their status"""
    if not tasks:
        print("\nYour to-do list is empty.")
        return
    
    print("\n--- YOUR TASKS --")
    for i, (task, status) in enumerate(tasks.items(), start = 1):
        status_symbol = "✅" if status =="done" else "⬜"
        print(f"{i}. {status_symbol} {task}")
        
def add_task():
    """Add a new task (default status: pending)"""
    task = input("Enter the new task: ")
    tasks[task] = "pending"
    print(f"Added: '{task}'")
    save_tasks()  # Save immediately
    
def mark_done():
    """Mark a task as done"""
    if not tasks:
        print("No tasks to mark as done.")
        
    view_tasks()
    try:
        choice = int(input("\Enter the number of the task to mark as done: "))
        task_list = list(tasks.keys())
        if 1 <= choice <= len(task_list):
            task = task_list[choice - 1]
            tasks[task] = "done"
            print(f"Marked as done: '{task}'")
            save_tasks()
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")
    

# del tasks[task]
# Removes a task from the dictionary completely   

# list(task.keys())
# Get all task names as a list (to show numbers and find by index)     
def remove_task():
    """Remove a task completely"""
    if not tasks:
        print("No tasks to remove.")
        return
    
    view_tasks()
    try:
        choice  = int(input("\nEnter the number of the task to remove: "))
        task_list = list(tasks.keys())
        if 1 <= choice <= len(task_list):
            task = task_list[choice - 1]
            del tasks[task]
            print(f"Removed: '{task}'")
            save_tasks()
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")
        
def main():
    """Main program loop"""
    load_tasks()
    print("\n--- PERSISTENT TO-DO LIST ---")
    print(f"Loaded {len(tasks)} tasks from '{TASKS_FILE}'")
    
    while True:
        print("\n--- MENU ---")
        print("1. View tasks") 
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Remove task")
        print("5. Quit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            save_tasks()
            print(f"Tasks saved to '{TASKS_FILE}'. Goodbye!")
            break
        else:
            print("Invalid choie. Please enter 1, 2, 3, 4, or 5.")
    
    
# if __name__ == "__main__":
# This is standard Python Practice - it means "run this code only if I run this file directly, not if i import it from another file."         
if __name__ == "__main__":
    main()
        