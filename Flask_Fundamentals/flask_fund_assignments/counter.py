from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hotdoggy'
# our index route will handle rendering our form

def SessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def index():

    SessionCounter()
    return render_template("counter.html")

@app.route('/plustwo', methods=['POST'])
def counted():

    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():

    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
