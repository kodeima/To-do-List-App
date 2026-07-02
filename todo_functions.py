tasks = []

def add_task(task_name, priority='normal'):
    '''Add a new task to the list.'''
    task = {
        'name': task_name,
        'priority': priority,
        'done': False
    }

    tasks.append(task)
    return task

def view_tasks():
    '''Display all tasks'''
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return
    
    print('\n==== Task List ====')

    for index, task in enumerate(tasks, start=1):
        status = 'Done' if task['done'] else 'Pending'

        print(
            f"{index}. {task['name']} |" 
            f" Priority: {task['priority']} |"
            f" Status: {status}"
        )

    print(f"\nTotal Tasks: {len(tasks)}\n")

def mark_done(task_number):
    '''Mark a task as done.'''

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        return True
    
    return False

def delete_task(task_number):
    '''Delete a task.'''

    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        return removed
    
    return None

def task_statistics():
    '''Display task statistics.'''

    if len(tasks) == 0:
        print('\nNo statistics available.\n')
        return
    
    completed = sum(task['done'] for task in tasks)
    remaining = len(tasks) - completed

    numbers = list(range(1, len(tasks) + 1))

    print('\n==== Task Statistics ====')
    print(f"Completed Tasks: {completed}")
    print(f"Remaining Tasks: {remaining}")
    print(f"Total Tasks: {len(tasks)}")
    print(f"Smallest Task Number: {min(numbers)}")
    print(f"Largest Task Number: {max(numbers)}\n")

def show_priorities(*priorities):
    '''Display tasks with specific priorities.'''

    print('\nAccepted Priorities:')

    for priority in priorities:
        print('-', priority)

def user_settings(**settings):
    '''Display user settings.'''

    print('\nUser Settings:')

    for key, value in settings.items():
        print(f"{key}: {value}")

def compare_lists():
    '''Compare lists of tasks.'''

    if len(tasks) == 0:
        return '\nNo tasks available to compare.\n'
    
    names = [task['name'] for task in tasks]
    statuses = [
        'Done' if task['done'] else 'Pending' for task in tasks
    ]

    print('\nTask Summary')

    for name, status in zip(names, statuses):
        print(f"{name} - {status}")
