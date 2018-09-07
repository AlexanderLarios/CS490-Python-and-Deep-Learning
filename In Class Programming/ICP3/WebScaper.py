from bs4 import BeautifulSoup
import requests
import os


link = "https://en.wikipedia.org/wiki/Deep_learning"
source = requests.get(link)
text = source.text

bSoup = BeautifulSoup(text, "html.parser")
print(bSoup.title)

for link in bSoup.find_all('a', href=True):
    print(link['href'])