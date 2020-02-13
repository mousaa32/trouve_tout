import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os
import json
import csv

def table(url):
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup
req = Request("https://www.leboncoin.fr", headers={
              'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'})
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')

# soup=table("https://www.leboncoin.fr/annonces/offres/")
# print(soup.find('title'))
