from flask import Flask, request, redirect
from replit import db
# imports request and redirect as well as flask

app = Flask(__name__, static_url_path='/static')
# path to the static file that stores my images

users = {}
@app.route('/signup', methods=["POST"])
def signup():
      form = request.form
      try:
        if form["username"] in db:
          return redirect("/error_username_exists")
        else:
          db[form["username"]] = {"name": form["name"], "password": form["password"]}
          return redirect("/login")
      except Exception as e:
        return f"An error occurred: {str(e)}"
    
# db["david"] = {"password":"Baldy1"}
# db["katie"] = {"password":"k8t"}
# users["david"] = {"password" : "Baldy1"}
# users["katie"] = {"password" : "k8t"}
# A dictionary hard coded into the program that stores the login details for two users


@app.route('/login', methods=["POST"])
def login():
  form = request.form
  try:
    if db[request.form["username"]]["password"]== request.form["password"]:
      return redirect("/yup")
    else:
      return redirect("/nope")
  except:
    return redirect("/nope")
# Login checking code - uses POST because it's dealing with usernames & passwords so we want encryption

# If the user details are correct, they get a lovely success gif, if not, they get a 'nope' gif.

# Try except used to load the 'nope' in case there's an error.

@app.route("/nope")
def nope():
  return """<img src="static/nerdy.gif" height="100">"""

@app.route("/yup")
def yup():
  page = """<img src="static/yup.gif" height="100">"""
  f = open("change.html", "r")
  page += f.read()
  f.close()
  return page

# The two methods above load the relevant gif depending on the result of the '/login' method
@app.route("/changePass", methods=["POST"])
def change():
  form = request.form
  db[request.form["username"]] ["password"]= request.form["newPassword"]
  return f"""Password changed to {request.form['newPassword']}"""

@app.route('/')
def index():
  redirection_target = request.args.get('redirect')
  page = ""
  f = open("home.html", "r")
  page = f.read()
  f.close()

# Check if the redirection_target is specified and valid
  if redirection_target and redirection_target in ['/signup', '/login']:
      return redirect(redirection_target)

  return page
# Loads the login HTML page that I've built separately on run.

app.run(host='0.0.0.0', port=81)