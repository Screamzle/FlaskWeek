from app import db, Products, Orders, Orders_Products

db.create_all() # Creates all table classes defined

# prod1 = Products(product_name='Bently Maybach', price=150000) #Add example to products table
# prod2 = Products(product_name='Ferrari 360 Spider', price=125000) #Add example to products table
# db.session.add(prod1)
# db.session.add(prod2)
# db.session.commit()
#
# # Here we reference the country that london belongs to useing 'country', this is what we named the backref variable in db.relationship()
# ldn = Cities(name='London', country = uk)
# mcr = Cities(name='Manchester', country = Countries.query.filter_by(name='United Kingdom').first())
#
# db.session.add(ldn)
# db.session.add(mcr)
# db.session.commit()
#
# print(f"Cities in the UK are: {uk.cities[0].name}, {uk.cities[1].name}")
# print(f"London's country is: {ldn.country.name}")
# print(f"Manchester's country is: {mcr.country.name}")