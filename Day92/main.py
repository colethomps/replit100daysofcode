import requests, json
timezone = "GMT"
latitude = 51.5002
longitude = -0.1262

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()
print("High:", user["daily"]["temperature_2m_max"][0], "Low:", user["daily"]["temperature_2m_min"][0])
