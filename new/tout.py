import urllib
import urllib.request
from bs4 import BeautifulSoup
import os,json,csv,pandas
from datetime import datetime

def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup
grand=list()
################*******************************************nova**********************************************#######################
soup=table("https://nova.sn/") 
liens_nova=[]
for lien in soup.findAll('li',{'data-depth':'1'}):
    liens_nova.append(lien.find('a').get('href'))
# print(liens_nova[14:16])
for link in liens_nova[14:16]:
    for i in range(1,6):
        nom_produit = list()
        prix_produit = list()
        image_produit = list()
        source_produit = list()
        alt_produit = list()
        soup=table(link+"?page="+str(i))
        categorie=soup.find('title').text
        logo="https://img.comparez.co/logo/sn/novs.jpg"
        for nov in soup.findAll('div',{'class':'second-block'}):
            nom_produit.append(nov.find('h5').text.replace('\n','').replace(',',';').replace('\xa0piece',' piece'))
            prix_produit.append(nov.find('span').text.replace('\xa0000\xa0',' 000'))
        for tof in soup.findAll('div',{'class':'first-block'}):
            source_produit.append(tof.find('img')['src'])
            alt_produit.append(tof.find('img')['alt'].replace(',',';').replace('\xa0piece',' piece'))
            image_produit.append(tof.find('a')['href'])
        for i,j,k,l,m in zip(nom_produit,prix_produit,image_produit,source_produit,alt_produit):
            dic = {'nom_produit':i,'prix_produit':j,'source_produit':k,'image_produit':l,'alt_produit':m,'logo':logo,'categorie':categorie}
            grand.append(dic)
###############*******************************************coinafrique/immobilier**********************************************#######################

soup=table("https://sn.coinafrique.com/categorie/immobilier/14")
lien_coin=[]
 
for lien in soup.findAll('li',{'class':'category gtm-sous-category center'}):
    lien_coin.append(lien.find('a').get('href'))
# print(lien_coin)
for link in lien_coin:
    for i in range(1,6):
        nom_produit = list()
        prix_produit = list()
        image_produit = list()
        source_produit = list()
        alt_produit = list()
        soup=table("https://sn.coinafrique.com"+link+"?page="+str(i)+"")
        categorie=soup.find('title').text.replace('CoinAfrique - Petites annonces au Sénégal - ','').replace('Immobilier  - ','')
        logo="https://img.comparez.co/logo/sn/coinafrique.jpg"
        for nov in soup.findAll('div',{'class':'card round'}):
            nom_produit.append(nov.find('p',{'class':'card-desc'}).text.replace('\n','').replace(',',';').replace('\xa0piece',' piece'))
            prix_produit.append(nov.find('p',{'class':'card-title activator orange-text'}).text)
            source_produit.append(nov.find('img')['src'])
            alt_produit.append(nov.find('a')['title'].replace(',',';').replace('\xa0piece',' piece'))
            image_produit.append("https://sn.coinafrique.com"+nov.find('a')['href'])
        for i,j,k,l,m in zip(nom_produit,prix_produit,image_produit,source_produit,alt_produit):
            dic = {'nom_produit':i,'prix_produit':j,'source_produit':k,'image_produit':l,'alt_produit':m,'logo':logo,'categorie':categorie}
            grand.append(dic)

################*******************************************vehicule/coinafrique**********************************************#######################

soup=table("https://sn.coinafrique.com/categorie/vehicules/3")
lien_coin=[]
 
for lien in soup.findAll('li',{'class':'category gtm-sous-category center'}):
    lien_coin.append(lien.find('a').get('href'))
# print(lien_coin)
for link in lien_coin:
    for i in range(1,6):
        nom_produit = list()
        prix_produit = list()
        image_produit = list()
        source_produit = list()
        alt_produit = list()
        soup=table("https://sn.coinafrique.com"+link+"?page="+str(i)+"")
        categorie=soup.find('title').text.replace('CoinAfrique - Petites annonces au Sénégal - ','').replace('Véhicules neuf et occasion - ','')
        logo="https://img.comparez.co/logo/sn/coinafrique.jpg"
        for nov in soup.findAll('div',{'class':'card round'}):
            nom_produit.append(nov.find('p',{'class':'card-desc'}).text.replace('\n','').replace(',',';').replace('\xa0piece',' piece'))
            prix_produit.append(nov.find('p',{'class':'card-title activator orange-text'}).text)
            source_produit.append(nov.find('img')['src'])
            alt_produit.append(nov.find('a')['title'].replace(',',';').replace('\xa0piece',' piece'))
            image_produit.append("https://sn.coinafrique.com"+nov.find('a')['href'])
        for i,j,k,l,m in zip(nom_produit,prix_produit,image_produit,source_produit,alt_produit):
            dic = {'nom_produit':i,'prix_produit':j,'source_produit':k,'image_produit':l,'alt_produit':m,'logo':logo,'categorie':categorie}
            grand.append(dic)   
#################*******************************************electronique/immobilier**********************************************#######################

soup=table("https://sn.coinafrique.com/categorie/electronique/10")
lien_coin=[]
 
for lien in soup.findAll('li',{'class':'category gtm-sous-category center'}):
    lien_coin.append(lien.find('a').get('href'))
# print(lien_coin)
for link in lien_coin:
    for i in range(1,6):
        nom_produit = list()
        prix_produit = list()
        image_produit = list()
        source_produit = list()
        alt_produit = list()
        soup=table("https://sn.coinafrique.com"+link+"?page="+str(i)+"")
        categorie=soup.find('title').text.replace('CoinAfrique - Petites annonces au Sénégal - ','').replace('Electronique neuf et occasion - ','').replace('Electronique  - ','')
        logo="https://img.comparez.co/logo/sn/coinafrique.jpg"
        for nov in soup.findAll('div',{'class':'card round'}):
            nom_produit.append(nov.find('p',{'class':'card-desc'}).text.replace('\n','').replace(',',';').replace('\xa0piece',' piece'))
            prix_produit.append(nov.find('p',{'class':'card-title activator orange-text'}).text)
            source_produit.append(nov.find('img')['src'])
            alt_produit.append(nov.find('a')['title'].replace(',',';').replace('\xa0piece',' piece'))
            image_produit.append("https://sn.coinafrique.com"+nov.find('a')['href'])
        for i,j,k,l,m in zip(nom_produit,prix_produit,image_produit,source_produit,alt_produit):
            dic = {'nom_produit':i,'prix_produit':j,'source_produit':k,'image_produit':l,'alt_produit':m,'logo':logo,'categorie':categorie}
            grand.append(dic)

outfile=open("/home/moussa/Documents/PROJET/projethtml/trouve_tout/new/fichier.json",'w+')
rows=json.dumps(grand,indent=4)
outfile.write(rows)



             