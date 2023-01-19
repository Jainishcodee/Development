tasks = []
def display_tasks():
    print("Here are your tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}: {task}")


def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list")


def remove_task(index):
    del tasks[index]
    print("Task removed")


def complete_task(index):
    tasks[index] = f"{tasks[index]} (Completed)"
    print("Task marked as completed")


def menu():
    while True:
        display_tasks()
        print("""
Menu:
  1. Add task
  2. Remove task
  3. Complete task
  4. Quit
""")
        choice = input("Enter a choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            add_task(task)
        elif choice == "2":
            index = int(input("Enter the index of the task to remove: ")) - 1
            remove_task(index)
        elif choice == "3":
            index = int(
                input("Enter the index of the task to mark as completed: ")) - 1
            complete_task(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


menu()
