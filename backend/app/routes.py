from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def about():
    return render_template("aboutUs.html")

@app.route('/farm-activities')
def coffeeProcess():
    return render_template("farmActivities.html")

@app.route('/tourism')
def testimonial():
    return render_template("tourism.html")

@app.route('/dashboard')
def index():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug = True)