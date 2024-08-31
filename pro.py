def display_menu():
    print("\nWelcome To the ToDo application :")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def viewtodolist(todo_list):
    if not todo_list:
        print("\nYour list is empty.")
    else:
        print("\nTo-Do List:")
        for idx, (task, completed) in enumerate(todo_list, start=1):
            status = "✓" if completed else "✗"
            print(f"{idx}. {task} [{status}]")

def addtask(todo_list):
    task = input("Enter a new task: ")
    todo_list.append((task, False))
    print(f"Task '{task}' added to the list.")

def removetask(todo_list):
    viewtodolist(todo_list)
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)[0]
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def marktaskcompleted(todo_list):
    viewtodolist(todo_list)
    try:
        task_number = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_number <= len(todo_list):
            task, _ = todo_list[task_number - 1]
            todo_list[task_number - 1] = (task, True)
            print(f"Task '{task}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            viewtodolist(todo_list)
        elif choice == "2":
            addtask(todo_list)
        elif choice == "3":
            removetask(todo_list)
        elif choice == "4":
            marktaskcompleted(todo_list)
        elif choice == "5":
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()