import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')


myLinks = soup.find_all("a", {"span class":"titleline"})

print(len(myLinks))

counter = 0
for link in myLinks:
  if counter > 1:
    print(link.text)
    # print(f"""https://www.yelp.com{link["href"]}""")
  counter +=1

