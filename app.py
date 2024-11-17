from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list
tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")  # Get task from form
    if task:
        tasks.append(task)  # Add to the task list
    return redirect(url_for("home"))  # Redirect to home page

@app.route("/clear", methods=["POST"])
def clear_tasks():
    tasks.clear()  # Clear all tasks
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
