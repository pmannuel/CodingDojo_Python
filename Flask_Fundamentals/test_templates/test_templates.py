from flask import Flask, render_template
app = Flask(__name__)

@app.route('/pokedex')
def index():
    return render_template('pokedex_flask.html')

app.run(debug=True)
