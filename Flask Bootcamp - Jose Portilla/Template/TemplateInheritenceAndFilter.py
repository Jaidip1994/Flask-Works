from flask import Flask, render_template, send_file
import os

# Python Jinja Template Filters
# https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html', name=name)


@app.route('/getImage/<imgName>')
def getImage(imgName):
    filePath = 'static'
    return send_file(os.path.join(filePath, imgName))

if __name__ == '__main__':
    app.run(debug=True)