from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "hotdoggy"
# our index route will handle rendering our form

@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/result', methods=['POST'])
def give_result():
   print "Got Post Info"

   session['name'] = request.form['name']
   session['dojolocation'] = request.form['dojolocation']
   session['favlanguage'] = request.form['favlanguage']
   session['comment'] = request.form['comment']

   if len(session['name']) < 1 or session['dojolocation'] == "none" or session['favlanguage'] == "none":
       flash("All survey questions must be answered!")
       return redirect('/')
   else:
       flash("Thank you {} for filling this survey!".format(session['name']))
       return render_template("result.html")

@app.route('/goback', methods=['POST'])
def go_back():
    session.clear()
    return redirect('/')

@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')

app.run(debug=True) # run our server
