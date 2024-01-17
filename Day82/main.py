from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/', methods=["GET"])
def index():
  get = request.args
  if get["language"].lower() == "english":
    return "Hello there"
  elif get["language"].lower() == "spanish":
    return "Hola"
  elif get["language"].lower() == "french":
    return "Bonjour"
  elif get["language"].lower() == "german":
    return "Hallo"
  elif get["language"].lower() == "italian":
    return "Ciao"
  return "No data"
app.run(host='0.0.0.0', port=81)