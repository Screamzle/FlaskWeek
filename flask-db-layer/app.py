from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Games(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String(30), nullable=False)
    game_price = db.Column(db.Float, nullable=False)

print(db)

if __name__ == "__main__":
    app.run(debug=True)

