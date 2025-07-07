from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Buy groceries", "completed": False},
    {"id": 2, "task": "Walk the dog", "completed": True}
]

next_id = 3

@app.route("/todo", methods=["GET", "POST"])
def todo():
    global next_id
    if request.method == "POST":
        new_task = request.form.get("task")
        if new_task:
            tasks.append({"id": next_id, "task": new_task, "completed": False})
            next_id += 1
        return redirect(url_for("todo"))
    return render_template("todolist.html", tasks=tasks)

@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    return redirect(url_for("todo"))

if __name__ == "__main__":
    app.run(debug=True)