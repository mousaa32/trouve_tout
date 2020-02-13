import urllib
import urllib.request
from bs4 import BeautifulSoup
import os,json,csv
from datetime import datetime
def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup
for link in range(1,80):
    try:
        soup=table("https://sn.comparez.co/telephones-et-tablettes/telephonie/?page="+str(link)+"")
        images=soup.findAll('div',{'class':'col-lg-3 col-md-3 col-sm-6 col-xs-6 text-center'})
        tabsource=list()
        alt=list()
        for i in images:   
            tabsource.append(i.find('img')['src'])
            alt.append(i.find('h2').text.replace("…","").replace(" - "," ").replace("-"," ").replace('"',''))
        with open('nom_compare.csv',"a", encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile,delimiter="\n")
            writer.writerow(alt)
        csvFile.close()
        for i,j in zip(alt,tabsource):
            imagefile=open("/home/moussa/Documents/PROJET/projethtml/trouve_tout/compare/"+i+".jpeg","wb")
            req = urllib.request.Request(j, headers={'User-Agent': 'Mozilla/5.0'})
            imagefile.write(urllib.request.urlopen(req).read()) 
    except Exception:   
        continue    
a=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
print("nouvel connection le",a)    