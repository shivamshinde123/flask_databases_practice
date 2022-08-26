from app import db, Puppy, Owner, Toy


## creating two puppies
rufus = Puppy('rufus')
fido = Puppy('fido')

## adding puppies to the db
db.session.add_all([rufus,fido])
db.session.commit()

##check 
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='rufus').first()
print(rufus)


## creating a owners
shivam = Owner('Shivam',rufus.id)


## giving the toy to rufus
toy1 = Toy('chew toy',rufus.id)
toy2 = Toy('ball',rufus.id)

db.session.add_all([shivam,toy1,toy2])
db.session.commit()

# grab rufus
rufus  = Puppy.query.filter_by(name='rufus').first()

print(rufus)

rufus.report_toys()