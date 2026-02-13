from todo import TodoManager


def main():
    manager = TodoManager()

    while True:
        print("\n===== TODO APP =====")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
            print("Task added successfully!")

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to update: "))
                print("1. Change title")
                print("2. Mark as completed")
                print("3. Mark as not completed")
                update_choice = input("Choose update option: ")

                if update_choice == "1":
                    new_title = input("Enter new title: ")
                    if manager.update_task(task_id, new_title=new_title):
                        print("Task updated successfully!")
                    else:
                        print("Task not found.")

                elif update_choice == "2":
                    if manager.update_task(task_id, completed=True):
                        print("Task marked as completed!")
                    else:
                        print("Task not found.")

                elif update_choice == "3":
                    if manager.update_task(task_id, completed=False):
                        print("Task marked as not completed!")
                    else:
                        print("Task not found.")

            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                if manager.delete_task(task_id):
                    print("Task deleted successfully!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
