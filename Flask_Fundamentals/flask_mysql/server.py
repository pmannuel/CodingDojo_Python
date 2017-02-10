from flask import Flask, render_template, redirect, request
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'user_demo')
# an example of running a query

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)

    return render_template("index.html", users=users)

@app.route('/create', methods=['POST'])
def create():
    query = "INSERT INTO users (first_name, last_name, age, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW())"
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }
    print data
    mysql.query_db(query,data)
    return redirect('/')

print mysql.query_db("SELECT * FROM users")
app.run(debug=True)
