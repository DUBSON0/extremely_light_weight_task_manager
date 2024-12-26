import datetime
import os
import time, sys, json
import keyboard

dt = time.localtime()

clear = lambda: os.system("clear")
clear()

def add_task():
    task_name = input("Enter new task name: ")
    task_description = input("Enter brief task description: ")
    task_due = input("Enter due date: ")
    date = str(datetime.date(dt.tm_year, dt.tm_mon, dt.tm_mday))
    with open("task_data.json", "r+") as f:
        file_data = json.load(f)
        task_id = len(file_data["Tasks"])
        data = {"id": task_id, "title": task_name, "desc": task_description, "due_date": task_due, "date_created" : date}
        file_data["Tasks"].append(data)
        f.seek(0)
        json.dump(file_data, f, indent =4)
        print("Task added.")

def list_tasks():
    with open("task_data.json", "r") as f:
        file_data = json.load(f)
        for task in file_data["Tasks"]:
            print("ID: " + str(task["id"]) + " | Title: " + task["title"]+ " | Due date: " + task["due_date"] + " | Date created: " + task["date_created"])
            print("Description: " + task["desc"])

def delete_task():
    task_id = int(input("Enter ID for task to be removed: "))
    file_data={}
    with open("task_data.json", "r+") as f:
        file_data = json.load(f)
        file_data["Tasks"].pop(task_id)
    for task in file_data["Tasks"]:
        task["id"] = file_data["Tasks"].index(task)
    with open("task_data.json", "w") as f:
        json.dump(file_data, f, indent =4)
    print("Task deleted.")

print("Extremely Light Weigth Task Manager")
while True:
    if keyboard.is_pressed("n"):
        keyboard.press_and_release('backspace')
        clear = lambda: os.system("clear")
        clear()
        print("Create New Task")
        add_task()
    elif keyboard.is_pressed("c"):
        keyboard.press_and_release('backspace')
        clear = lambda: os.system("clear")
        clear()
        print("Extremely Light Weigth Task Manager")
    elif keyboard.is_pressed("l"):
        keyboard.press_and_release('backspace')
        clear = lambda: os.system("clear")
        clear()
        print("All Tasks")
        list_tasks()
    elif keyboard.is_pressed("d"):
        keyboard.press_and_release('backspace')
        clear = lambda: os.system("clear")
        clear()
        delete_task()
    elif keyboard.is_pressed("h"):
        clear = lambda: os.system("clear")
        clear()
        print("ELWTM \n l - list all tasks.\n n - create a new task. \n d - to delete a task by task ID. \n q - to quit.")
    elif keyboard.is_pressed("q"):
        clear = lambda: os.system("clear")
        clear()
        break







