import eel
import json

tasks = []

@eel.expose
def add_task(name, status, id):
    task = {"name": name, "status": status, "id": id}
    tasks.append(task)

@eel.expose
def edit_task(id, name, filter):
    tasks[id]["name"] = name
    eel.showTodo(filter)()

@eel.expose
def delete_task(id, filter):
    tasks.pop(id)
    eel.showTodo(filter)()

@eel.expose
def mark_completed(id, status):
    tasks[id]["status"] = "completed" if status else "pending"

@eel.expose
def clear_list():
    tasks.clear()
    eel.showTodo("all")()

eel.init('DSA/rough')
# Start the Eel web server
eel.start('index.html', mode='brave')
