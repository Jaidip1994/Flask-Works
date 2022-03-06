from flask import Flask, render_template
# Python Jinja Template Filters
# https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)