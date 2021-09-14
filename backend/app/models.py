from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Jimakas123@localhost:5432/ufarm'

db = SQLAlchemy(app)

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    rating = db.Column(db.String(64), nullable=False)
    comment = db.Column(db.Text(), nullable=False)
    createdOn = db.Column(db.DateTime(), default=datetime.utcnow)
    updatedOn = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)    

    def __repr__(self):
        return '<Review %r>' % self.id

""" This is a one-to-many relationship from roles to users, because 
    one role belongs to many users and users have only one role. """

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')
    
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    app.run(debug = True)