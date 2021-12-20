from flask import Flask
app = Flask(__name__)

from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:Jimakas123@localhost:5432/flask-project', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column('booking_id', Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    phone = Column(String(50))
    guestNum = Column(String(50))
    accommodationType = Column(String(50))
    checkIn = Column(Date)
    checkOut = Column(Date)

    def __repr__(self):
        return '<Booking %r>' % self.id

class Review(Base):
    __tablename__ = 'reviews'
    id = Column('review_id', Integer, primary_key=True)
    name = Column(String(50))
    rating = Column(String(50))
    comment = Column(String(50))
    reviewDate = Column(Date)

    def __repr__(self):
        return '<Review %r>' % self.id

from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    app.run(debug = True)