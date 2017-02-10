from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hotdoggy'

@app.route('/')
def index():
    import random
    session['mynumber'] = random.randint(1,100)
    return render_template("great_number_game.html")

@app.route('/checkguess', methods=['POST'])
def checking():
    mynumber = session['mynumber']
    guess = request.form['guess']

    try:
        if int(guess) < mynumber:
            remark = "Too low!"
            color = "red"
            return render_template("great_number_game.html", remark=remark, color=color)

        elif int(guess) > mynumber:
            remark = "Too high!"
            color = "red"
            return render_template("great_number_game.html", remark=remark, color=color)

        elif int(guess) == mynumber:
            return redirect('/congratulations')

    except ValueError:
        return redirect('/')

@app.route('/congratulations')
def congratulations():
    mynumber = session['mynumber']
    remark = str(mynumber) + " was the number!"
    color = "green"
    return render_template("congratulations.html", remark=remark, color=color)

@app.route('/goback', methods=['POST'])
def goback():
    session.pop('mynumber')
    return redirect('/')

app.run(debug=True)
