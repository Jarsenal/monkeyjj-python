from flask import Flask
app = Flask(__name__)

from flask import render_template

@app.route("/")
def hello():
    return "<h1>Hello, World! This is Monkey JayJay</h1>"
    
@app.route("/index.html")
@app.route("/fake.html")
def indexG():
    return "<h1>Hello, World! This is index.html</h1>"

username = 'Daddy Zhou'
@app.route("/" + username)
def name():
    return render_template('index.html', title='Hohoho', username=username)
