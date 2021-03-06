from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def greetings():
    return render_template('greetings.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojos():
    return render_template('dojo.html')

app.run(debug=True)
