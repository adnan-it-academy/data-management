import requests

response = requests.get('https://openlibrary.org/search?mode=everything')

print(response.text)
type(response.text)