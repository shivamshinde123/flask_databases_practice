import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICAITONS'] = False
app.config

db = SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):

    __tablename__ = 'Puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # one to many relationship --> connecting one puppy with many toys
    toys = db.relationship('Toy',backref='Puppy',lazy='dynamic')
    # one to one relationship between the owner and puppy
    owner = db.relationship('Owner',backref='Puppy',uselist=False) 
    # here we are using uselist=False. This is because we don't need the list of items for the one-to-one relationships

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Owner of the puppy {self.name} is {self.owner.name}."
        else:
            return f"Puppy {self.name} has no owner yet."

    
    def report_toys(self):
        print('Here are my toys:')
        for toy in self.toys:
            print(toy.item_name)

class Toy(db.Model):
    
    __tablename__ = 'Toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('Puppies.id'))


    def __init__(self,item_name,puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):
    

    __tablename__ = 'Owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('Puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id
