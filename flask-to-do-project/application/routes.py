from application import app, db
from application.models import ToDo
from flask import Flask, render_template, request
from application.html_forms import AddForm, UpdateForm, DeleteForm, CompleteForm


@app.route('/')
@app.route('/home')
@app.route('/incomplete')
def view_to_do_list():
    incomplete_tasks = ToDo.query.filter_by(completed=False).all()
    tasks_list = '<ul>'
    for task in incomplete_tasks:
        tasks_list += '<li>' + str(task.id) + " - " + task.task_description + "</li>"
    tasks_list += '<ul>'
    return render_template('incomplete.html', tasks=tasks_list)


@app.route('/completed')
def view_completed_tasks():
    complete_tasks = ToDo.query.filter_by(completed=True).all()
    completed_tasks_list = '<ul>'
    for task in complete_tasks:
        completed_tasks_list += '<li>' + str(task.id) + " - " + task.task_description + "</li>"
    completed_tasks_list += '<ul>'
    return render_template('completed.html', tasks=completed_tasks_list)


@app.route('/add', methods=['GET', 'POST'])
def add_task():
    message = ""
    form = AddForm()

    if request.method == 'POST':
        task_description = form.task_description.data

        if len(task_description) == 0:
            message = "Please enter your to do list item"
        else:
            record = ToDo(task_description)
            db.session.add(record)
            db.session.commit()
            message = f'Thank you, your task "{task_description}" has been recorded'

    return render_template('add.html', form=form, message=message)


@app.route('/update/', methods=['GET', 'POST'])
def update_task():
    message = ""
    form = UpdateForm()

    if request.method == 'POST':
        task_id = form.task_id.data
        task_description = form.task_description.data

        if len(task_description) == 0:
            message = "Please enter your to do list item"
        else:
            update_item = ToDo.query.get(task_id)
            update_item.task_description = task_description
            db.session.commit()
            message = f'Thank you, task "{task_id}" has been updated to "{task_description}"'

    return render_template('update.html', form=form, message=message)


@app.route('/delete', methods=['GET', 'POST'])
def delete_task():
    message = ""
    form = DeleteForm()

    if request.method == 'POST':
        task_id = form.task_id.data

        if task_id is None:
            message = "Please enter number of item to delete"
        else:
            delete_item = ToDo.query.get(task_id)
            db.session.delete(delete_item)
            db.session.commit()
            message = f'Thank you, task "{task_id}" has been deleted'

    return render_template('delete.html', form=form, message=message)


@app.route('/status', methods=['GET', 'POST'])
def complete_task():
    message = ""
    form = CompleteForm()

    if request.method == 'POST':
        task_id = form.task_id.data
        status = form.status.data
    
        if task_id is None:
            message = "Please enter number of item to complete/resume"
        else:
            complete_item = ToDo.query.get(task_id)
            complete_item.completed = bool(status)
            db.session.commit()
            message = f'Thank you, the status of task "{task_id}" has been changed'

    return render_template('status.html', form=form, message=message)


@app.route('/resume/<int:resume>')
def resume_task(resume):
    task_to_resume = ToDo.query.get(resume)
    task_to_resume.completed = False
    db.session.commit()
    return f'Task {resume} has been resumed'
