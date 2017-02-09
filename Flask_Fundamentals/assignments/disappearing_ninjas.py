from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "hotdoggy"

@app.route('/')
def index():
    return render_template("ninjas_color.html", noNinjas=True)

@app.route('/ninja')
def show_ninjas():
    # session['content'] = "<img src='{{ url_for('static', filename='ninja_img/tmnt.png') }}' alt='tmnt'>"
    return render_template("ninjas_color.html", allNinjas=True)

@app.route('/ninja/<color>')
def show_a_ninja(color):
    return render_template("ninjas_color.html", color=color, allNinjas=False)

app.run(debug=True) # run our server
