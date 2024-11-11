# add a task,
# write to a file

# variable to store task
# increment id
# save date
# variable to status

import datetime
import json

# receive user input and continuously save in a file until user quits

date_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format date and time as a string
date_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format date and time as a string
task_id = 1
task_description = input("Enter task description: ")

tasks = [{
    "id": task_id,
    "description": task_description,
    "status": "todo",
    "createdAt": date_created,
    "updatedAt": date_updated,
}]

filename = 'data2.json'
with open(filename, 'a') as f_obj:
    json.dump(tasks, f_obj)




# update a task
# append
# to
# a
# file
#
# mark in progress
# ???
#
# list
# all
# tasks
# read
# contents
# of
# the
# file
#
# task
# status
# done
# todo
# in -progress
#
# tasks
# properties
#


# id: A unique identifier for the task
# description: A short description of the task
# status: The status of the task(todo, in -progress, done)
# createdAt: The date and time when the task was created
# updatedAt: The date and time when the task was last updated
