import heapq
import json

# Global Variables
tasks = []
priority_queue = []
undo_stack = []

def rebuild_priority_queue():
    global priority_queue
    priority_queue = [(task['priority'], i, task) for i, task in enumerate(tasks)]
    heapq.heapify(priority_queue)

def load_tasks_from_json(filename):
    global tasks, undo_stack
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        rebuild_priority_queue()
        undo_stack.clear()  # Clearing undo stack on reload
        print(f"Tasks successfully loaded from {filename}.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not a valid JSON file.")

def save_tasks_to_json(filename):
    try:
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=4)
        print(f"Tasks successfully saved to {filename}.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(title = "New Task", status = "pending", deadline = "None", priority = 2):
    global tasks
    task = {'title': title, 'status': status, 'deadline': deadline, 'priority': priority}   # Creating a Dictionary to Store the Respective Values into Global Task Dictionary
    tasks.append(task)  # Adding the New Task to Original List
    heapq.heappush(priority_queue, (priority, len(tasks) - 1, task))
    undo_stack.append(("delete", task.copy()))    # If We Want to Undo the New Addition 
    print(f"Task Added : {task}")

def delete_task(title):
    global tasks, undo_stack
    
    # Checking if the Task Exists
    task_delete = None
    for task in tasks:
        if task['title'] == title:
            task_delete = task
            break
    
    if task_delete:
        tasks.remove(task_delete)
        rebuild_priority_queue()
        undo_stack.append(("add", task_delete.copy()))  # If We Want to Undo the Deletion
        print(f"Deleted the Task : {task_delete}")
    
    else:
        print(f"Task: '{title}' doesn't exists!")

def edit_task(title):
    global tasks, undo_stack
    task_edit = None
    for task in tasks:
        if task['title'] == title:
            task_edit = task
            break
    
    if task_edit:
        original_task = task_edit.copy()
        print(f"Editing Task : {task_edit}")

        # 1. Collect inputs first
        new_title = input(f"Enter New Title (Current : {task_edit['title']}): ") or task_edit['title']
        new_status = input(f"Enter New Status (Current : {task_edit['status']}): ") or task_edit['status']
        new_deadline = input(f"Enter New Deadline (Current : {task_edit['deadline']}): ") or task_edit['deadline']
        
        # 2. Handle priority input with proper try-except
        try:
            priority_input = input(f"Enter new priority (current: {task_edit['priority']}): ")
            new_priority = int(priority_input) if priority_input else task_edit['priority']
        except ValueError:
            print("Invalid priority. Defaulting to Current Priority.")
            new_priority = task_edit['priority']

        # 3. Perform the update
        task_edit.update({
            'title': new_title,
            'status': new_status,
            'deadline': new_deadline,
            'priority': new_priority
        })

        rebuild_priority_queue()
        undo_stack.append(("edit", original_task, task_edit.copy()))
        print(f"Task edited: {task_edit}")
    
    else:
        print(f"Task: '{title}' doesn't exist!")

def undo_last_action():
    global tasks
    # Checkling if There are Actions Already Performed
    if not undo_stack:
        print("No Actions to be Undone!")
    
    else:
        # Getting the Action to be Undone
        action_data = undo_stack.pop()
        
        # Reversing the Addition Operation
        if action_data[0] == "delete":
            task = action_data[1]
            if task in tasks:
                tasks.remove(task)
                rebuild_priority_queue()
                print(f"Undone the Addition of Task: {task}")
            else:
                print("Task not found while deleting!")
        
        # Reversing the Delete Operation
        elif action_data[0] == "add":
            task = action_data[1]
            if task not in tasks:
                tasks.append(task)
                rebuild_priority_queue()
                print(f"Undone the Deletion of the Task : {task}")
            else:
                print("Task already present!")

        # Reversing the Edit Operation   
        elif action_data[0] == "edit":
            original_task = action_data[1]
            edit_task = action_data[2]
            for i, task in enumerate(tasks):
                if task['title'] == edit_task['title']:
                    tasks[i] = original_task
                    rebuild_priority_queue()
                    print(f"Undone the Edit and Restored the Task: {original_task}")
                    break

def view_tasks():
    print("\nCurrent Tasks:")
    if not tasks:
        print("No Tasks Available.")
    else:
        for i, task in enumerate(tasks, start = 1): # 'start' indicates the start index to print 
            print(f"{i}. {task['title']} - Status: {task['status']}, Deadline: {task['deadline']}, Priority: {task['priority']}")


def view_priority_tasks():
    print("\nTasks by Priority:")
    if not priority_queue:
        print("No Tasks Available.")

    else:
        heap_copy = priority_queue[:]
        while heap_copy:
            priority, idx, task = heapq.heappop(heap_copy)
            print(f"Priority {priority}: Task: {task['title']} (Status: {task['status']}, Deadline: {task['deadline']})")


# Selecting the Options and Performing the Tasks
print("Task Manager: With JSON Save and Load Functionality")
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Edit Task")
    print("4. Undo Last Action")
    print("5. View All Tasks")
    print("6. View Tasks by Priority")
    print("7. Load Tasks from JSON")
    print("8. Save Tasks to JSON")
    print("9. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        title = input("Enter task title: ")
        status = input("Enter task status (default: Pending): ") or "Pending"
        deadline = input("Enter task deadline (optional): ") or None
        priority = int(input("Enter task priority (default: 2): ") or 2)
        add_task(title, status, deadline, priority)
    elif choice == "2":
        title = input("Enter task title to delete: ")
        delete_task(title)
    elif choice == "3":
        title = input("Enter task title to edit: ")
        edit_task(title)
    elif choice == "4":
        undo_last_action()
    elif choice == "5":
        view_tasks()
    elif choice == "6":
        view_priority_tasks()
    elif choice == "7":
        filename = input("Enter the filename to load tasks from: ")
        load_tasks_from_json(filename)
    elif choice == "8":
        filename = input("Enter the filename to save tasks to: ")
        save_tasks_to_json(filename)
    elif choice == "9":
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")