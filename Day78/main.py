from flask import Flask
import datetime
import random

app = Flask(__name__)

today = str(datetime.date.today())
print(today)

@app.route('/<pageNumber>')
def index(pageNumber):
  myName = "Cole"
  title = "Day 77 Solution"
  text = f"This is an example for a blog post for this day ({today})."
  randint = random.randint(1,1000)
  link = f"/{randint}"
  page = ""
  f = open(".tutorial/template/portfolio.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{name}", myName)
  page = page.replace("{title}", title)
  page = page.replace("{text}", text)
  page = page.replace("{link}", link)
  page = page.replace("{today}", today)
  return f"This is page number {pageNumber}.  {page} "

@app.route('/')
def home():
  myName = "Cole"
  title = "Day 77 Solution"
  text = f"This is an example for a blog post for this day ({today})."
  randint = random.randint(1,1000)
  link = f"/{randint}"
  page = ""
  f = open(".tutorial/template/portfolio.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{name}", myName)
  page = page.replace("{title}", title)
  page = page.replace("{text}", text)
  page = page.replace("{link}", link)
  page = page.replace("{today}", today)
  return f"This is homepage.  {page} "

app.run(host='0.0.0.0', port=81)