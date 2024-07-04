tasks = []

while True:
    print("Todo List Manager")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
 
    if choice == "1":
        task_name = input("Enter task name: ")
        tasks.append({"task": task_name, "completed": False})
        print("Task added successfully!\n")
    
    
    elif choice == "2":
        task_index = int(input("Enter the task number you want to mark as completed: "))
        if task_index >= 1 and task_index <= len(tasks):
            tasks[task_index - 1]["completed"] = True
            print("Task marked as completed!\n")
        else:
            print("Invalid task number. Please try again.\n")
    
    
    elif choice == "3":
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index}. {task['task']} - {status}")
        print()
    
  
    elif choice == "4":
        task_index = int(input("Enter the task number you want to delete: "))
        if task_index >= 1 and task_index <= len(tasks):
            del tasks[task_index - 1]
            print("Task deleted successfully!\n")
        else:
            print("Invalid task number. Please try again.\n")
    
   
    elif choice == "5":
        print("Exiting Todo List Manager. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a valid option.\n")
