from app import db, Games

db.create_all()

testgame = Games(game_title='The Last of Us',game_price=39.99)
# Extra: this section populates the table with an example entry

db.session.add(testgame)
db.session.commit()