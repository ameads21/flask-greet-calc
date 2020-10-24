from flask import Flask, request

app = Flask(__name__)

@app.route("/welcome")
def page_welcome():
  return "Welcome"

@app.route("/welcome/home")
def page_welcome_home():
  return "Welcome home"

@app.route("/welcome/back")
def page_welcome_back():
  return "Welcome back"