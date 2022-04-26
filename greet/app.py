from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def show_landing():
    return "<h1>welcome</h1>"

@app.route('/welcome/<subpage>')
def show_subupage(subpage):
    return f"<h1>welcome {subpage}"

