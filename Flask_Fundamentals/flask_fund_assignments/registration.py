from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = "hotdoggy"

#global variable
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
m = re.compile(r'^(?=.*?\d)+(?=.*?[A-Z])+$')

@app.route('/')
def index():
  return render_template("registration.html")

@app.route('/validating', methods=['POST'])
def give_result():
   print "Got Post Info"

   session['firstname'] = request.form['firstname']
   session['lastname'] = request.form['lastname']
   session['email'] = request.form['email']
   session['pass'] = request.form['pass']
   session['cpass'] = request.form['cpass']

   firstname_l = len(session['firstname'])
   lastname_l = len(session['lastname'])
   email_l = len(session['email'])
   pass_l = len(session['pass'])
   cpass_l = len(session['cpass'])

   warning = ""
   session['color'] = "red"

   if firstname_l < 1 or lastname_l < 1 or email_l < 1 or pass_l < 1 or cpass_l < 1 :
       warning += "All fields are required and must not be blank.<br />"
   if not EMAIL_REGEX.match(session['email']) :
       warning += "Invalid email address!<br />"
   if str.isalpha(str(session['firstname']))==False or str.isalpha(str(session['lastname']))==False:
       warning += "Invalid name!<br />"
   if pass_l < 5 :
       warning += "Password should be more than 5 characters.<br />"
   if not m.match(session['pass']):
       warning += "Password must have at least 1 uppercase letter and 1 numeric value.<br />"
   if session['pass'] != session['cpass']:
       warning += "Password do not match.<br />"
   elif warning == "":
       flash("You're one of us now!")
       session['color'] = "green"
       return redirect('/')

   flash(warning)
   return redirect('/')

app.run(debug=True) # run our server
