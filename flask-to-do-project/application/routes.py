from application import app, db
from application.models import ToDo
from flask import Flask, render_template


@app.route('/')
@app.route('/home')
def view_to_do_list():
    incomplete_tasks = ToDo.query.filter_by(completed=False).all()
    tasks_string = ""
    for task in incomplete_tasks:
        tasks_string += str(task.id) + " " + task.task_description + "\n"
    return render_template('completed.html', tasks=tasks_string)


@app.route('/completed')
def view_completed_tasks():
    complete_tasks = ToDo.query.filter_by(completed=True).all()
    completed_tasks_string = ""
    for task in complete_tasks:
        completed_tasks_string += str(task.id) + " " + task.task_description + "\n"
    return render_template('incomplete.html', tasks=completed_tasks_string)


@app.route('/add/<new_task>')
def add_task(new_task):
    new_todo = ToDo(task_description=new_task)
    db.session.add(new_todo)
    db.session.commit()
    return f'Added "{new_task}" to To Do List'


@app.route('/update/<description>')
def update_task(description):
    update_item = ToDo.query.get(1)
    update_item.task_description = description
    db.session.commit()
    return f'Task has been updated to "{update_item.task_description}"'


@app.route('/delete/<int:delete>')
def delete_task(delete):
    task_to_delete = ToDo.query.get(delete)
    db.session.delete(task_to_delete)
    db.session.commit()
    return "Deleted task from To Do List"


@app.route('/complete/<int:complete>')
def complete_task(complete):
    task_to_complete = ToDo.query.get(complete)
    task_to_complete.completed = True
    db.session.commit()
    return f'Task {complete} has been completed'


@app.route('/resume/<int:resume>')
def resume_task(resume):
    task_to_resume = ToDo.query.get(resume)
    task_to_resume.completed = False
    db.session.commit()
    return f'Task {resume} has been resumed'
