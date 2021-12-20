from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_cors import CORS
from models import engine, Base, session, Booking, Review

Base.metadata.create_all(engine)

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def about():
    return render_template("about_us.html")

@app.route('/our-activities')
def our_activities():
    return render_template("our_activities.html")

@app.route('/visit-us')
def visit_us():
    return render_template("visit_us.html")

@app.route('/bookings', methods = ['GET', 'POST'])
def create_booking():
    if request.method == 'POST':

        booking = Booking(
            name=request.form.get('name'), 
            email=request.form.get('email'),
            phone=request.form.get('phone'), 
            guestNum=request.form.get('guestNum'),
            accommodationType=request.form.get('accommodationType'),
            checkIn=request.form.get('checkIn'), 
            checkOut=request.form.get('checkOut')
            )
        
        session.add(booking)
        session.commit()
    return render_template('create_booking.html')

@app.route('/reviews', methods = ['GET', 'POST'])
def create_review():
    if request.method == 'POST':
        if not request.form.get('name') or not request.form.get('rating') or not request.form.get('comment') or not request.form.get('reviewDate'):
            flash('Please enter all the fields', 'error')
        else:
            review = Review(
                name=request.form.get('name'),
                rating=request.form.get('rating'),
                comment=request.form.get('comment'),
                reviewDate=request.form.get('reviewDate')
                )
        
            session.add(review)
            session.commit()
            flash('Review was successfully added')
            return redirect(url_for('show_reviews'))
    return render_template('create_review.html')

@app.route('/show-reviews')
def show_reviews():
   return render_template('show_reviews.html', reviews = session.query(Review).all() )

# sanity check route
@app.route('/flask-test', methods=['GET'])
def ping_pong():
    return jsonify('sanity check route')

if __name__ == '__main__':
    app.run(debug = True)