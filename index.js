const taskInput = document.querySelector(".task-input input"),
filters = document.querySelectorAll(".filters span"),
clearAll = document.querySelector(".clear-btn"),
taskBox = document.querySelector(".task-box");

let editId,
isEditTask = false,
todos = JSON.parse(localStorage.getItem("todo-list"));

filters.forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelector("span.active").classList.remove("active");
        btn.classList.add("active");
        showTodo(btn.id);
    });
});

function showTodo(filter) {
    if(todos) {
        todos.forEach((todo, id) => {
            let completed = todo.status == "completed" ? "checked" : "";
            if(filter == todo.status || filter == "all") {
                eel.add_task(todo.name, todo.status, id)();
            }
        });
    }
}
showTodo("all");

function updateStatus(selectedTask) {
    eel.mark_completed(selectedTask.id, selectedTask.checked)();
}

function editTask(taskId, textName) {
    editId = taskId;
    isEditTask = true;
    taskInput.value = textName;
    taskInput.focus();
    taskInput.classList.add("active");
    eel.edit_task(taskId, textName, filter)();
}

function deleteTask(deleteId, filter) {
    isEditTask = false;
    eel.delete_task(deleteId, filter)();
}

clearAll.addEventListener("click", () => {
    isEditTask = false;
    eel.clear_list()();
});

