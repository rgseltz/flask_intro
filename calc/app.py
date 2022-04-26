from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def show_landing():
    return f"""<h1>Show Landing Page</h1>"""

@app.route('/add')
def calc_add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = str(add(a,b))
    return result

@app.route('/sub')
def calc_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(sub(a,b))
    return result

@app.route('/mult')
def calc_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(mult(a,b))
    return result

@app.route('/div')
def calc_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(div(a,b))
    return result

operators = {
    "add" : add,
    "sub" : sub,
    "mult": mult,
    "div" : div
}
@app.route('/math/<opr>')
def do_math(opr):
    """Do math using operator"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(operators[opr](a,b))
    return result



    



