from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "hotdoggy"
mysql = MySQLConnector(app, 'valid_emails')

#global variable
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    flash("Receive $1,000 today! Just submit your email! (not a scam)")
    return render_template("index.html", notValid=True, color="green")

@app.route('/validating', methods=['POST'])
def give_result():

   email = request.form['email']
   email_l = len(email)

   if not EMAIL_REGEX.match(email) or email_l < 1:
       flash("Email is not valid!")
       return render_template("index.html", notValid=True, color="red", emails=emails)

   else:
       flash(email + " is a valid email address! The Prince of Nigeria thanks you!")

       query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
       data = {
            'email' : email,
        }
       mysql.query_db(query,data)

       query = "SELECT * FROM emails"
       emails = mysql.query_db(query)

       return render_template("index.html", Valid=True, color="green", emails=emails)

print mysql.query_db("SELECT * FROM emails")
app.run(debug=True) # run our server
