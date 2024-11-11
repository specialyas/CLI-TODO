import json
import sys
from datetime import datetime

TASK_FILE = "task.json"


def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


print(load_tasks())


# save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


# use the description to create a task
def add_task(description):
    tasks = load_tasks()
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks)

def delete_task(id):
    

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [<Args>]")
        return

    command = sys.argv[1]

    if command == 'add':
        description = ''.join(sys.argv[2:])
        add_task(description)
    elif command == 'delete':
        task_id = int(sys.argv[2])
        delete_task = task_id
    else:
        print("Unknown Command")


if __name__ == '__main__':
    main()
