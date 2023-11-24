# To-Do List Application
x = []
task_id = 1

while True:
    print("\nChoose any option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        x.append({"id": task_id, "task": task, "completed": False})
        print(f"Task '{task}' added with ID: {task_id}")
        task_id += 1
    elif choice == "2":
        if not x:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for t in x:
                status = "Completed" if t["completed"] else "Pending"
                print(f"ID: {t['id']} - Task: {t['task']} - Status: {status}")
    elif choice == "3":
        if not x:
            print("No tasks to mark.")
        else:
            task_id = int(input("Enter the ID of the task to mark as completed: "))
            for t in x:
                if t["id"] == task_id:
                    t["completed"] = True
                    print(f"Task ID {task_id} marked as completed.")
                    break
            else:
                print("Invalid task ID.")
    elif choice == "4":
        if not x:
            print("No tasks to delete.")
        else:
            task_id = int(input("Enter the ID of the task to delete: "))
            for t in x:
                if t["id"] == task_id:
                    x.remove(t)
                    print(f"Task ID {task_id} deleted.")
                    break
            else:
                print("Invalid task ID.")
    elif choice == "5":
        print("Exiting the to-do list app. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
