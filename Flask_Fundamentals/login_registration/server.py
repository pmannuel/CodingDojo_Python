from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "hotdoggy"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'thewall')

#global variable
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/user/log_in', methods=['POST'])
def log_in():

   password = request.form['pass']

   query = "SELECT * FROM users WHERE email = :email LIMIT 1"
   data = {
        'email' : request.form['email']
    }

   user = mysql.query_db(query,data)

   if user == []:
       flash('Invalid login credentials')
       return redirect('/')
   if bcrypt.check_password_hash(user[0]['password'], password):
       session['user'] = user
       return redirect('/thewall')
   else:
       flash('Incorrect Password')
       return redirect('/')

@app.route('/user/log_off')
def log_off():
    session.pop('user')
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():

   query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :pass, NOW())"
   data = {
       'first_name' : request.form['first_name'],
       'last_name' : request.form['last_name'],
       'email' : request.form['email'],
       'pass' : request.form['pass'],
       'cpass' : request.form['cpass']
   }

   firstname_l = len(data['first_name'])
   lastname_l = len(data['last_name'])
   email_l = len(data['email'])
   pass_l = len(data['pass'])
   cpass_l = len(data['cpass'])

   warning = ""
   session['color'] = "red"

   if firstname_l < 1 or lastname_l < 1 or email_l < 1 or pass_l < 1 or cpass_l < 1 :
       warning += "All fields are required and must not be blank.<br />"
   if not EMAIL_REGEX.match(data['email']) :
       warning += "Invalid email address!<br />"
   if str.isalpha(str(data['first_name']))==False or str.isalpha(str(data['last_name']))==False:
       warning += "Invalid name!<br />"
   if pass_l < 8 :
       warning += "Password should be more than 8 characters.<br />"
   if data['pass'] != data['cpass']:
       warning += "Password do not match.<br />"
   elif warning == "":
       data['pass'] = bcrypt.generate_password_hash(data['pass'])
       mysql.query_db(query,data)
       query2 = "SELECT * FROM users WHERE email = :email LIMIT 1"
       session['user'] = mysql.query_db(query2,data)
       return redirect('/thewall')

   flash(warning)
   return redirect('/')

@app.route('/thewall')
def thewall():
    query = "SELECT * FROM users LEFT JOIN posts ON users.id = posts.user_id"
    posts = mysql.query_db(query)
    print posts
    query = "SELECT * FROM posts LEFT JOIN comments ON posts.id = comments.post_id LEFT JOIN users ON users.id = comments.user_id"
    comments = mysql.query_db(query)
    return render_template("dashboard.html", posts=posts, comments=comments)

@app.route('/post_message', methods=['POST'])
def post_message():
    query = "INSERT INTO posts (post, created_at, user_id) VALUES (:post, NOW(), :user_id)"
    data = {
        'post' : request.form['post'],
        'user_id' : session['user'][0]['id']
    }
    mysql.query_db(query,data)
    return redirect('/thewall')

@app.route('/post_comment', methods=['POST'])
def post_comment():
    query = "INSERT INTO comments (comment, created_at, user_id, post_id) VALUES (:comment, NOW(), :user_id, :post_id)"
    data = {
        'comment' : request.form['comment'],
        'user_id' : session['user'][0]['id'],
        'post_id' : request.form['post_id']
    }
    mysql.query_db(query,data)
    return redirect('/thewall')

app.run(debug=True) # run our server
