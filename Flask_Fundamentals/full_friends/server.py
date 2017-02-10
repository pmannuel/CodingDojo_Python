from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'my_friends')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template("index.html", friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at) VALUES (:first_name, :last_name, :occupation, NOW())"
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'occupation' : request.form['occupation']
    }
    print data
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friends WHERE friends.id =" + id
    edit_friend = mysql.query_db(query)
    return render_template("edit.html", edit_friend=edit_friend, edit=TRUE)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'occupation' : request.form['occupation'],
        'id' : id
    }
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/friends/<id>/delete')
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True) # run our server
