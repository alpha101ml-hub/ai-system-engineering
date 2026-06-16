'''
A list is a container that holds multiple items in order.
'''


# Start with an empty list of tasks
tasks = []

'''
while true loop - True means "always true" - so this loop runs forever until we explicitly break out of it.
'''

while True:
    print("\n--- MY TO=DO LIST ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour tasks: ")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == "2":
        new_task = input("Enter the new task: ")
        tasks.append(new_task)
        print(f"Added: '{new_task}'")
        
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nyour tasks: ")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
                
            try:
                remove_num = int(input("Enter the number of the task to remove: "))
                # Convert to index (user sees 1, but list index starts as 0)
                removed_task = tasks.pop(remove_num - - 1)
                print(f"Removed: '{removed_task}'")
            except ValueError:
                print("Please enter a valid number.")
            except IndexError:
                print("That number doesn't exist.")
                
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter 1,2,3 or 4")
    

'''
\m creates a blank line before the menu (makes it look neat)
The user types 1,2,3 or 4

len(tasks) gives the number of items in the list. If it's 0, the list is empty
enumreate(tasks, start=1) is a speacial loop that gives you both the index (starting at 1) and the task itself.

Example: If tasks = ["Buy mils", "Call mom"]. the loop prints:
1. Buy mils
2. Call mom


tasks.append(new_task) adds the new task to the end of the list.

tasks.pop(index) removes the item at that position and returns it so we can print it.
remove_num - 1 converts the user's number (1,2,3) to the computer's index (0,1,2).
try/except catches two error:
  ValueError: user typed letters instead of a number.
  IndexError: user typed a number that's too high (e.g., 5 when when their are 3 only tasks).
  
break immediately exits the while True loop, ending the program
'''


'''
Test these scenarios: 

Choose "2" and add "Buy milk" and "Call mom".

Choose "1" – you should see both tasks.

Choose "3" – it shows the list, type 1 to remove "Buy milk".

Choose "1" again – only "Call mom" should remain.

Try typing "abc" when it asks for a number – it should catch the error.

Try removing task number 5 when only 1 exists – it should catch the error.

Choose "4" to quit.
'''
