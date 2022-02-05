from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/info')
def info():
    return '<h1>Puppies are cute</h1>'

# Dynamic Routing
@app.route('/info/<name>')
def getuserinfo(name):
    return f'Hello {name}'

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1] == 'y':
        name = name[:-1] + 'iful'
    else:
        name += 'y'
    return f'<h1>Puppies in latin is {name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)