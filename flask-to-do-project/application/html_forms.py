from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField


class AddForm(FlaskForm):
    task_description = StringField('Enter your To Do list item')
    submit = SubmitField('Add Item')


class UpdateForm(FlaskForm):
    task_id = IntegerField('Enter To Do list item number')
    task_description = StringField('Enter text to update To Do list item')
    submit = SubmitField('Submit Item')


class DeleteForm(FlaskForm):
    task_id = IntegerField('Enter To Do list item number')
    submit = SubmitField('Delete Item')


class CompleteForm(FlaskForm):
    task_id = IntegerField('Enter To Do list item number')
    status = SelectField('Choose whether to complete or resume task', choices=[
        ('True', 'Completed'),
        ('False', 'Resume')
    ])
    submit = SubmitField('Complete Item')

