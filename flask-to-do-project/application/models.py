from application import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_description = db.Column(db.String(150), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, task_description):
        self.task_description = task_description