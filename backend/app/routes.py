from flask import Flask, render_template

app = Flask(__name__)

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