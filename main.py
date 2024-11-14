import json
import sys
from datetime import datetime

TASK_FILE = "task.json"


# read tasks from the json file
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []




# save tasks to json file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


# add a new task with the specified description
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
    print(f"Task added successfully with (ID: {task['id']})")


# use the task id to update the task description
def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
        print(f"Task {task_id} not found")


# use the id to delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task with id {task_id} has been deleted")


# use the id to change task status
def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task {task_id} not found")


#  Lists tasks, optionally filtering by status
def list_tasks(status=None):
    tasks = load_tasks()
    for task in tasks:
        if status is None or task['status'] == status:
            print(
                f"ID: {task['id']} || Description: {task['description']} || status: {task['status']} || Created At: {task['createdAt']} || Updated At: {task['updatedAt']}   ")


def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [<Args>]")
        return

    command = sys.argv[1]

    if command == 'add':
        description = ''.join(sys.argv[2:])
        add_task(description)
    elif command == 'update':
        task_id = int(sys.argv[2])
        description = ''.join(sys.argv[3:])
        update_task(task_id, description)
    elif command == 'mark-in-progress':
        task_id = int(sys.argv[2])
        mark_task(task_id, "in-progress")
    elif command == 'done':
        task_id = int(sys.argv[2])
        mark_task(task_id, "done")
    elif command == 'list':
        if len(sys.argv) > 2:
            status = sys.argv[2]
            list_tasks(status)
        else:
            list_tasks()
    elif command == 'delete':
        task_id = int(sys.argv[2])
        delete_task(task_id)
    else:
        print("Unknown Command")


if __name__ == '__main__':
    main()
