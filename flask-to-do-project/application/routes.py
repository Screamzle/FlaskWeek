from application import app, db
from application.models import ToDo

@app.route('/')
@app.route('/home')
@app.route('/view')
def view_to_do_list():
    incomplete_tasks = ToDo.query.filter_by(completed=False).all()
    tasks_string = ""
    tasks_id = ""
    for task in incomplete_tasks:
        tasks_string += str(task.id) + " " + task.task_description + "<br>"
    return f'Incomplete tasks are as follows:<br><br>{tasks_string}{tasks_id}'

@app.route('/completed')
def view_completed_tasks():
    complete_tasks = ToDo.query.filter_by(completed=True).all()
    tasks_string = ""
    for task in complete_tasks:
        tasks_string += str(task.id) + " " + task.task_description + "<br>"
    return f'Completed tasks are as follows:<br><br>{tasks_string}'

@app.route('/add/<newtask>')
def add_task(newtask):
    new_todo = ToDo(task_description=newtask)
    db.session.add(new_todo)
    db.session.commit()
    return f'Added "{newtask}" to To Do List'

@app.route('/update/<description>')
def update_task(description):
    update_item = ToDo.query.get(1)
    update_item.task_description = description
    db.session.commit()
    return f'Task has been updated to "{update_item.task_description}"'

@app.route('/delete')
def delete_task():
    task_to_delete = ToDo.query.get(1)
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