import os
from openai import OpenAI
import requests, json, os
newsKey = os.environ['newsapi']
country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"
result = requests.get(url)
data = result.json()
# print(json.dumps(data, indent=2))
##### The new bit #####################
for article in data['articles']:
  article['title']
  article['url']
  content = str(article['content'])
  
  client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ['openai'],
  )
  prompt = "Summarize this for a second-grade class in English in 100 words. "+ content
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