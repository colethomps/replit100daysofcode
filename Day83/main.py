from flask import Flask, request
import datetime

app = Flask(__name__)

today = str(datetime.date.today())

print(today)

@app.route('/', methods=["GET", "POST"])
def index():
    get = request.args
    color = get.get("color", "blue").lower()
    if color == "green":
        color = "green"
    elif color == "red":
        color = "red"
    myName = "Cole"
    title = "Day 77 Solution"
    text = f"This is an example for a blog post for this day ({today})."
    image = "picard.jpg"
    page = ""
    with open("portfolio.html", "r") as f:
        page = f.read()
    page = page.replace("{name}", myName)
    page = page.replace("{title}", title)
    page = page.replace("{text}", text)
    page = page.replace("{image}", image)
    page = page.replace("{today}", today)
    page = page.replace("{color}", color)
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
