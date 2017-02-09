from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hotdoggy'

@app.route('/')
def index():
    try:
        session['amount_gold'] = session['amount_gold']
    except KeyError:
        session['amount_gold'] = 0

    try:
        session['log'] += session['new_log']
    except KeyError:
        session['log'] = ""

    return render_template("NinjaGold.html")

@app.route('/earning', methods=['POST'])
def earning():
    import random, math, datetime
    session['timestamp'] = '{:(%Y/%m/%d %H:%M)}'.format(datetime.datetime.now())
    session['color'] = 'green'

    if request.form['action'] == 'Farm':
        session['location'] = request.form['action']
        session['earned'] = random.randint(10,20)
        session['amount_gold'] += session['earned']

    elif request.form['action'] == 'Cave':
        session['location'] = request.form['action']
        session['earned'] = random.randint(5,10)
        session['amount_gold'] += session['earned']

    elif request.form['action'] == 'House':
        session['location'] = request.form['action']
        session['earned'] = random.randint(2,5)
        session['amount_gold'] += session['earned']

    elif request.form['action'] == 'Casino':
        session['location'] = request.form['action']
        session['earned'] = int(random.uniform(-50,50))
        session['amount_gold'] += session['earned']
        if session['earned'] < 0 :
            session['new_log'] = "<p style='color:red'>Entered a casino and lost " + str(abs(session['earned'])) + " golds... Ouch... " + session['timestamp'] + "</p>"
            return redirect('/')
        else:
            session['color'] = 'green'
            session['new_log'] = "<p style='color:" + session['color'] +"'>Entered a casino and won " + str(session['earned']) + " golds! You're one lucky ninja! " + session['timestamp'] + "</p>"
            return redirect('/')

    session['new_log'] = "<p style='color:" + session['color'] +"'>Earned " + str(session['earned']) + " golds from the " + session['location'] + "! " + session['timestamp'] + "</p>"

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('amount_gold')
    session.pop('log')

    return redirect('/')

app.run(debug=True)
