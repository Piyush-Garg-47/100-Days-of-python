import requests

response = requests.get("https://www.google.co.in/")

print(response.text)