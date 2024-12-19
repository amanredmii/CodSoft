class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the list.")
        else:
            print(f"Task '{task}' not found in the list.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in your list.")
        else:
            print("Your To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def main():
    todo_list = ToDoList()

    while True:
        show_menu()
        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task you want to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task you want to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()
