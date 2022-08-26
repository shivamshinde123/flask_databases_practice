from app import db, Puppy

# creates all the table 
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])
db.session.commit()

print(sam.id)
print(frank.id)

moti = Puppy('Moti',5)
db.session.add_all([moti])
db.session.commit()

print(moti.id)
