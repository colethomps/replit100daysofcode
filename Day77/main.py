from flask import Flask, redirect
import datetime
import timedelta

app = Flask(__name__)

today = str(datetime.date.today())
yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
print(today)

@app.route('/')
def seventySeven():
  return redirect(f"/{today}")

@app.route(f'/{today}')
def index():
  myName = "Cole"
  
  title = "Day 77 Solution"
  text = f"This is an example for a blog post for this day ({today})."
  image = "picard.jpg"
  link = yesterday
  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{name}", myName)
  page = page.replace("{title}", title)
  page = page.replace("{text}", text)
  page = page.replace("{image}", image)
  page = page.replace("{link}", link)
  page = page.replace("{today}", today)
  return page

@app.route(f'/{yesterday}') # Creates the path to the home page
def home(): # Subroutine to create the home page
  # Three quotes followed by the html for the baldies site. Three more quotes to close. All the HTML is assigned to the 'page' variable
  page = f"""html

  <html>

  <head>
    <title>David's World Of Baldies</title>
  </head>


  <body>
  <h1>Dave's World of Baldies</h1> 
  <h2>Welcome to our website!</h2>

  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

  <h2>Gallery of Baldies</h2>
  <p>Here are some of the legends of the bald world.</p>

  <img src="images/picard.jpg" width = 30%> 
  <p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>

  <ul>
    <li>Beautiful bald man</li>
    <li>Calm and cool under pressure</li>
    <li>All the Picard memes</li>
  </ul>

  <p><a href = "page2.html">Go to page 2</a></p>

</body>

</html>

  """

  return page # returns the contents of the page variable
  
@app.route('/56')
def fiftySix():
  myName = "Dave"
  title = "Day 56 Solution"
  text = "So, day 56 was all about using csv reading and file and folder manipulation to make 100 files in dozens of folders. This was tricky because the names of the folders and files were based on the top 100 streaming songs and so weren't simple to encode."
  image = "56.png"
  link = "https://replit.com/@DavidAtReplit/Day-056-Solution#main.py"

  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page.replace("{name}", myName)
  page.replace("{title}", title)
  page.replace("{text}", text)
  page.replace("{image}", image)
  page.replace("{link}", link)
  return page



app.run(host='0.0.0.0', port=81)