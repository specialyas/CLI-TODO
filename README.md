# Task CLI Application

A simple command-line interface (CLI) application to create and manage tasks. This application supports adding, updating, deleting, and listing tasks, with tasks stored in a JSON file (`task.json`). Each task has an ID, description, status, and timestamps for creation and updates.

## Project URL
[Project Repository URL](https://roadmap.sh/projects/task-tracker) 

## Features

- **Add a Task**: Create a new task with a description.
- **Update a Task**: Update the description of an existing task by its ID.
- **Delete a Task**: Remove a task by its ID.
- **Mark Task Status**: Mark a task as "in-progress" or "done".
- **List Tasks**: List all tasks or filter tasks by status (e.g., only show tasks that are "done").

## Getting Started

### Prerequisites
- Python 3.x must be installed on your system.
- Basic knowledge of command-line operations is helpful.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/cli-todo.git
    ```

2. Navigate to the project directory:
    ```bash
    cd cli-todo
    ```

### Running the Project

1. Open a terminal or command prompt.
2. Run the application with the desired command:
    ```bash
    python main.py <command> [arguments]
    ```

### Commands

- **Add a Task**
    ```bash
    python main.py add <description>
    ```
    Example:
    ```bash
    python main.py add "Complete project documentation"
    ```

- **Update a Task**
    ```bash
    python main.py update <task_id> <new_description>
    ```
    Example:
    ```bash
    python main.py update 1 "Update project documentation with examples"
    ```

- **Delete a Task**
    ```bash
    python main.py delete <task_id>
    ```
    Example:
    ```bash
    python main.py delete 1
    ```

- **Mark Task Status**
    - To mark a task as "in-progress":
      ```bash
      python main.py mark-in-progress <task_id>
      ```
    - To mark a task as "done":
      ```bash
      python main.py done <task_id>
      ```
    Example:
    ```bash
    python main.py done 1
    ```

- **List Tasks**
    - List all tasks:
      ```bash
      python main.py list
      ```
    - List tasks by status ("todo", "in-progress", or "done"):
      ```bash
      python main.py list <status>
      ```
    Example:
    ```bash
    python main.py list done
    ```

## File Structure

- `main.py` - Main script for running the CLI commands
- `task.json` - JSON file used to store tasks

