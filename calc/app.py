from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def result_add():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = add(a,b)
  return str(result)



@app.route('/sub')
def result_sub():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = sub(a,b)
  return str(result)


@app.route('/mult')
def result_mult():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = mult(a,b)
  return str(result)


@app.route('/div')
def result_div():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = div(a,b)
  return str(result)



operators = {
  "add": add,
  "sub": sub,
  "mult": mult,
  "div": div,
}

@app.route('/math/<oper>')
def math_results(oper):
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = operators[oper](a,b)
  return str(result)