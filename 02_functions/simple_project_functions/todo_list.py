# 02_functions/simple_project_functions/todo_list.py
# Simple to-do list

todo_list = []

def add_task(task):
    todo_list.append(task)

def show_tasks():
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

add_task("Buy groceries")
add_task("Finish homework")
show_tasks()