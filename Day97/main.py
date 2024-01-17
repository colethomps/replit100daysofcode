import os
import requests
from openai import OpenAI
from bs4 import BeautifulSoup

url = input("Paste wiki URL > ")

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

refs = soup.find_all("ol", {"class": "references"})

# Create an empty string to store the selected references
selected_refs = ""

# Iterate through the found references and add them to selected_refs
for ref in refs:
    ref_text = ref.get_text()
    if len(selected_refs) + len(ref_text) <= 1000:
        selected_refs += ref_text
    else:
        break

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ['openai'],)

# Use selected_refs in the prompt
prompt = "Summarize this for a second-grade class in English in 10 words. " + selected_refs

chat_completion = client.chat.completions.create(
      messages=[
          {
            "role": "user",
            "content": prompt,
          }
      ],
      model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)
