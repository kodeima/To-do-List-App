from todo_functions import(
    add_task,
    view_tasks,
    mark_done,
    delete_task,
    task_statistics,
    show_priorities,
    user_settings,
    compare_lists
)

show_priorities('Low', 'Normal', 'High')

user_settings(
    name= 'John Doe',
    Theme= 'Dark',
    notifications= 'Enabled',
)

while True:
    print("\n==== To-Do List Menu ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Task Statistics")
    print("6. Compare Lists")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        task_name = input("Enter task name: ")
        priority = input("Enter task priority (Low, Normal, High): ")
        
        if priority == '':
            priority = 'Normal'

        add_task(task_name, priority)

        print(f"Task '{task_name}' added successfully!")

    elif choice == '2':
        view_tasks()

    elif choice == '3':
        view_tasks()

        if input('Mark a task? (y/n): ').lower() == 'y':
            try:
                number = int(input('Enter task number: '))

                if mark_done(number):
                    print(f'Task {number} marked as done.')

                else:
                    print(f'Task {number} does not exist.')

            except ValueError:
                print('Invalid input. Please enter a valid task number.')
    
    elif choice == '4':
        view_tasks()

        if input('Delete a task? (y/n): ').lower() == 'y':
            try:
                number = int(input('Enter task number: '))

                deleted = delete_task(number)

                if deleted:
                    print(f'Task "{deleted["name"]}" deleted successfully.')

                else:
                    print(f'Task {number} does not exist.')
            
            except ValueError:
                print('Invalid input. Please enter a valid task number.')

    elif choice == '5':
        task_statistics()

    elif choice == '6':
        compare_lists()

    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
