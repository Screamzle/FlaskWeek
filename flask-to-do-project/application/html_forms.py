from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField

class AddForm(FlaskForm):
    task_description = StringField('Enter your To Do list item')
    submit = SubmitField('Add Item')
