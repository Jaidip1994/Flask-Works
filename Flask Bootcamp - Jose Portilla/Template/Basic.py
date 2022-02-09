from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def indecroute():
    return "Nothing here"

@app.route("/<name>")
def index(name):
    letters = list(name)
    return render_template('basic.html', my_var = letters)

if __name__ == '__main__':
    app.run(debug=True)