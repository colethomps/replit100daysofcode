import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?find_desc=Top+Restaurants&find_loc=Scottsdale%2C+AZ&sortby=rating"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')


myLinks = soup.find_all("a", {"class":"css-19v1rkv"})

print(len(myLinks))

counter = 0
for link in myLinks:
  if counter > 1:
    print(link.text)
    print(f"""https://www.yelp.com{link["href"]}""")
  counter +=1