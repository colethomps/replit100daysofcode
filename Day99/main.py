import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Find elements with the provided HTML structure
video_titles = soup.find_all("a", {"class": "style-scope ytd-rich-grid-media"})

print((video_titles))

for title in video_titles:
    # Extract the title from the 'title' attribute of the 'a' tag
    video_title = title['title']
    print(video_title)

