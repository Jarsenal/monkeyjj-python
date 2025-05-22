from flask import Flask
myapp = Flask(__name__)

from flask import render_template

@myapp.route("/")
def hello():
    return "<h1>Hello, World! This is Monkey JayJay</h1>"
    
@myapp.route("/index.html")
@myapp.route("/fake.html")
def indexG():
    return "<h1>Hello, World! This is index.html</h1>"

username = 'daddyyyy'
@myapp.route("/" + username)
def name():
    return render_template('index.html', username=username)
