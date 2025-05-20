from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, World! This is Monkey JayJay</h1>"
def index():
    return "<h1>Hello, World! This is index</h1>"
