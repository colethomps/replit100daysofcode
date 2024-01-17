import os
from openai import OpenAI
import requests
import json
from requests.auth import HTTPBasicAuth

news_api_key = os.environ['newsapi']
country = "us"
news_url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_api_key}"
news_result = requests.get(news_url)
news_data = news_result.json()

# Loop through each article in the news data
for article in news_data['articles']:
    article_title = article['title']
    article_url = article['url']
    article_content = str(article['content'])

    # Initialize the OpenAI client for each article
    openai_client = OpenAI(api_key=os.environ['openai'])
    prompt = "Summarize this in 1 word. " + article_content
    chat_completion = openai_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    summarized_artist = str(chat_completion.choices[0].message.content)
    summarized_artist = summarized_artist.lower()
    summarized_artist = summarized_artist.replace(" ", "%20")

    # Initialize Spotify API credentials
    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']

    spotify_url = "https://accounts.spotify.com/api/token"
    spotify_data = {"grant_type": "client_credentials"}
    auth = HTTPBasicAuth(client_id, client_secret)

    spotify_response = requests.post(spotify_url, data=spotify_data, auth=auth)
    access_token = spotify_response.json()["access_token"]

    # Search for a track based on the artist name
    spotify_search_url = "https://api.spotify.com/v1/search"
    headers = {'Authorization': f'Bearer {access_token}'}
    search_query = f"?q=artist%3A{summarized_artist}&type=track&limit=1"
    full_spotify_url = f"{spotify_search_url}{search_query}"

    spotify_response = requests.get(full_spotify_url, headers=headers)
    spotify_data = spotify_response.json()

    # Check if there are tracks in the Spotify API response
    if 'tracks' in spotify_data and 'items' in spotify_data['tracks']:
        track = spotify_data['tracks']['items'][0]
        track_name = track['name']
        track_preview_url = track['preview_url']

        # Print the information
        print(f"Article Title: {article_title}")
        print(f"Article URL: {article_url}")
        print(f"Summarized Artist: {summarized_artist}")
        print(f"Track Name: {track_name}")
        print(f"Track Preview URL: {track_preview_url}")
        print("\n")
    else:
        print(f"No tracks found for artist: {summarized_artist}")
