from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Jimakas123@localhost:5432/ufarm'

db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)    

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.title[:10])


@app.route('/')
def about():
    return render_template("about.html")

@app.route('/activities')
def visit():
    return render_template("activities.html")

@app.route('/coffee')
def coffeeProcess():
    return render_template("coffee.html")

@app.route('/testimonial')
def testimonial():
    return render_template("testimonial.html")

@app.route('/dashboard')
def index():
    return render_template("dashboard.html")
    
if __name__ == '__main__':
    app.run(debug = True)