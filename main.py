# add a task,
# write to a file

# variable to store task
# increament id
# save date
# variable to status

import json


# receive user input and continously save in a file until user quits


tasks = [{
    "id": 1,
    "description": "the first task",
    "status": "todo",
    "createdAt": "now",
    "updatedAt": "now",
}]
filename = 'data.json'
with open(filename, 'w') as f_obj:
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
# createdAt: The
# date and time
# when
# the
# task
# was
# created
# updatedAt: The
# date and time
# when
# the
# task
# was
# last
# updated
