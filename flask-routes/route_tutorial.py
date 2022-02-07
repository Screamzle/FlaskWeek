# Create an application that reads a number in the URL and returns that number squared.

import math
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'

@app.route('/<int:Number>', methods=['GET', 'POST'])
def square_route(Number):
    square = Number * Number
    if request.method == 'POST':
        return f'{Number} * {Number} = {square}. This is a POST request.'
    else:
        return f'{Number} * {Number} = {square}. This is a GET request.'

# can also do str(Number ** 2) instead of creating a variable called square and calling it in an f string

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
