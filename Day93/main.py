import requests
import json
import os
from requests.auth import HTTPBasicAuth
from flask import Flask, request, redirect, session, render_template

app = Flask(__name__)
app.secret_key = os.environ['sessionKey']

@app.route('/')
def index():
    clientID = os.environ['CLIENT_ID']
    clientSecret = os.environ['CLIENT_SECRET']
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    auth = HTTPBasicAuth(clientID, clientSecret)
    response = requests.post(url, data=data, auth=auth)
    accessToken = response.json().get("access_token")

    year = request.args.get('year')  # Get the year from the request parameters

    if not year:
        return "Please provide a year."

    year = year.lower().replace(" ", "%20")
    url = "https://api.spotify.com/v1/search"
    headers = {'Authorization': f'Bearer {accessToken}'}
    search = f"?q=year%3A{year}&type=track&limit=10"
    fullURL = f"{url}{search}"
    response = requests.get(fullURL, headers=headers)

    if response.status_code != 200:
        return f"Error: {response.status_code}"

    data = response.json()
    tracks = []

    for track in data["tracks"]["items"]:
        track_info = {
            "name": track["name"],
            "url": track["external_urls"]["spotify"]  # Get the Spotify track URL
        }
        tracks.append(track_info)

    return render_template("form.html", tracks=tracks, year=year)  # Pass the year to the template
app.run(host='0.0.0.0', port=81)