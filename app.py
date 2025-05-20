from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, World! This is Monkey JayJay</h1>"
@app.route("/index.html")
def indexG():
    return "<h1>Hello, World! This is index.html</h1>"
