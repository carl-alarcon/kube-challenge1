from flask import Flask
from flask import request
import pyjokes

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is index'

@app.route('/greet')
def greet():
    name = request.args.get('name')
    return f"Hello {name}"

@app.route('/joke')
def joke():
    j = pyjokes.get_joke()
    return j


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')