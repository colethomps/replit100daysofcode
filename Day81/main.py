from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
  page = ""
  form = request.form
  if form["made"] == "yes":
    page += "You're a robot!"
  else:
    page += "You're not a robot!"
  return page

@app.route('/')
def index():
  page = """<form method = "post" action = "/login">
    <p>Are you made of metal? <select name="made"><option>yes</option><option>no</option></select> </p>

    <p>Were you constructed by the Sirius Cybernetrics Corporation?<input type="radio" id="yes" name="agree" value="yes">
        <label for="yes">Yes</label><br>
        <input type="radio" id="no" name="agree" value="no">
        <label for="no">No</label><br></p>

    <p>Do you dream of being ED-209 when you grow up?: <input type="text" name="ed" required> </p>
    <button type="submit">login</button>
  </form>
    """
  return page
app.run(host='0.0.0.0', port=81)