from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    dob = DateField('Enter D.O.B')
    fave_num = IntegerField('Enter your favourite number')
    fave_food = SelectField('Choose your favourite food', choices=[('pizza', 'Pizza'), ('spaghetti', 'Spaghetti'), ('chilli', 'Chilli')])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        number = form.fave_num.data
        dob = form.dob.data
        food = form.fave_food.data

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {first_name} {last_name}. Your username is: {number}{dob}{food}'

    return render_template('home.html', form=form, message=message)


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')