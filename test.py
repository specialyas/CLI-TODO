import json


# menu displaying functionalities
def menu():
    print("""1. Add task
    2.View all tasks
    3. Edit task
    4. Quit""")




def addTask():
    # add task\ save to file
    task_description = input("Enter Task description: ")
    with open("task.txt", "w") as f_obj:
        f_obj.writelines(task_description)


# show tasks\ read from file
def showTasks():
    with open("task.txt", "r") as f_obj:
        data = f_obj.readlines()
    for lines in data:
        print(lines)

option = input("""Enter 1-4 to select an option:
    1. Add task
    2.View all tasks
    3. Edit task
    4. Quit
      """)
while option != "q":
    option = int(option)
    if int(option) == 1:
        addTask()
    elif int(option) == 2:
        showTasks()
    elif int(option) == 4:
        break
    option = input("""Enter 1-4 to select an option:
        1. Add task
        2.View all tasks
        3. Edit task
        4. Quit
          """)


