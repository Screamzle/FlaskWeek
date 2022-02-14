from app import db, Games

col = db.Column('game_description', String(100), nullable=False, default='none')
col.create(Games, populate_default=True)

# Column is added to table based on its name
assert col is Games.c.col1

# col1 is populated with 'foobar' because of `populate_default`


# test_game = Games(game_title='The Last of Us',game_price=39.99)
# Extra: this section populates the table with an example entry

# db.session.add(test_game)
# db.session.commit()
