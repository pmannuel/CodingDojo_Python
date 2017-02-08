from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form

@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/result', methods=['POST'])
def give_result():
   print "Got Post Info"

   name = request.form['name']
   dojolocation = request.form['dojolocation']
   favlanguage = request.form['favlanguage']
   comment = request.form['comment']

   return render_template("result.html", name=name, dojolocation=dojolocation, favlanguage=favlanguage, comment=comment)

@app.route('/goback', methods=['POST'])
def go_back():
     return redirect('/')

@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')

app.run(debug=True) # run our server
