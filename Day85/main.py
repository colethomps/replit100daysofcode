from flask import Flask, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = os.environ['sessionKey']

@app.route('/')

def index():
  page = ""
  myName = ""
  myUsername = ""
  myPassword = ""
  if session.get("myName"):
    myName = session["myName"]
  if session.get("myUsername"):
    myUsername = session["username"]
  page += f"<h1>{myName}</h1>"
  f = open("form.html", "r")
  page += f.read()
  f.close()
  return page
  
@app.route("/reset")
def reset():
  session.clear()
  return redirect("/")
###### NEW BIT #######################
@app.route("/setName", methods=["POST"])

def setName():
  session["myName"] = request.form["name"]
  return redirect("/")
############################################
app.run(host='0.0.0.0', port=81)