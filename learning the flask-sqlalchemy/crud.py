from app import db, Puppy

############## CREATE

my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

################ READ
all_puppies = Puppy.query.all()  # this will give us list of all the puppies in the table
print(all_puppies)

## SELECT BY ID
puppy1 = Puppy.query.get(1)
print(puppy1.name)

## FILTER
puppy_franky = Puppy.query.filter_by(name='Moti')
print(puppy_franky.all())


####################### UPDATE

first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

###################### DELETE

second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()



# 
all_puppies = Puppy.query.all()
print(all_puppies)