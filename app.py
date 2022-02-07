from flask import Flask

app = Flask(__name__)

@app.route('/home/<word>')
def hello_internet(word):
    return word.upper()

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)