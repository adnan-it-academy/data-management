import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.klix.ba/biznis/finansije/zastupnici-ulozili-41-amandman-na-budzet-sutra-slijedi-izjasnjenje-vlade-fbih-i-glasanje/250128053')
web_stranica = response.text

soup = BeautifulSoup(web_stranica, 'html.parser')

p_content = soup.find_all('p')

for i in p_content:
    print(i)

