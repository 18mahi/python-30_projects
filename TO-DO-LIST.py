print("this is a to-do list program")
print("you can add, remove, and view tasks")
task=[]
while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task2 = input("Enter the task to add: ")
        task.append(task2)
        
    elif choice == '2':
        task3 = input("Enter the task to remove: ")
        if task3 in task:
            print(f"Removing task: {task3}")
            task.remove(task3)
        else:
            print(f"Task '{task3}' not found in the list.")
        print("Task removed successfully.")
    
    elif choice == '3':
        print("Your current to-do-list items are:")
        if not task:
            print("No tasks available.")
        else:
            for i, t in enumerate(task, start=1): #enumerate function to get index and value Display tasks with their index
                print(f"{i}. {t}")
        print("Total tasks:", len(task))  # Display total number of tasks
        print("now you can add, remove, and view tasks if you want to do that")
            
    elif choice == '4':
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice, please try again.")