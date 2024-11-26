import requests 
query = input("Which type of news do you want in ? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2024-10-26&sortBy=publishedAt&apiKey=API_KEY"

r =requests.get(url)

print(r.text)