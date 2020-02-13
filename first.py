import urllib
import urllib.request
from bs4 import BeautifulSoup
import os,json,csv
from elasticsearch import Elasticsearch
from datetime import datetime

def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup
grand=list()
for link in range(1,72):
    try:
        soup=table("https://www.expat-dakar.com/telephones?page="+str(link)+"") 
        # print(soup.find('title'))
        les_noms=soup.findAll('div',{'class':'listing-details'})
        nom=list()
        for i in les_noms:
            nom.append(i.find('h2').text.replace("LE N°1 DE L'ELECTROMENAGER AU SENEGAL","").replace('T\u00e9l\u00e9phone','telephone')
            .strip())
        noms=[x for x in nom if x != '']
        # print(noms)
        infos=soup.findAll('div',{'class':'picto-block'})
        localite=list()
        stocage=list()
        ram=list()
        for i in infos:
            try:
                localite.append(i.find('span',{'class':'picto picto-place ed-icon-before icon-location'}).text.replace("Sacr\u00e9","Sacre")
                .replace("Gueule-Tap\u00e9e","Gueule-Tape").replace("M\u00e9dina","Medina").replace("Dieuppeul Derkl\u00e9","")
                .replace("Libert\u00e9","liberte").replace("Camb\u00e9r\u00e8ne","Camberene").replace('Cit\u00e9','cite').strip())
            except Exception:   
                continue
        describe=soup.findAll('div',{'class':'description-block'})
        description=list()
        for i in describe:
            description.append(i.find('p').text.replace("Des centaines de produits high- tech au meilleur prix garantie 1 an. Livraison & Installation Gratuites. Tel : 775506161","")
            .replace('à','a').replace("'"," ").replace("utilis\u00e9","utilise").replace('scell\u00e9','scelle').replace('tr\u00e8s','tres')
            .replace('t\u00e9l\u00e9phones','telephones').replace('\u00c9tat','etat').replace('\u00e9cran','ecran').replace('m\u00e9moire','memoire')
            .replace('Syst\u00e8me','systeme').replace('arri\u00e8re','arriere').strip())
            descriptions=[x for x in description if x != '']
        prix=soup.findAll('div',{'class':'bottom-content-left text-left'})
        prixexpt=list()
        for i in prix:
            prixexpt.append(i.find('span').text.replace("\xa0","").strip())
        date=soup.findAll('span',{'class':'picto picto-clock'})
        dates=list()
        for i in date:
            dates.append(i.find('b').text.replace('aujourd\u2019hui','aujourd hui').strip())
        images=soup.findAll('div',{'class':'listing-thumbnail videoless'})
        tabimag=list()
        tabsource=list()
        alt=list()
        for i in images:   
            try:
                http = "https://www.expat-dakar.com"
                image = i.find('img')['data-src'] 
                product_image = http + image
                tabimag.append(product_image)
                
                v=i.find('a')
                http="https://www.expat-dakar.com"
                a=http+v.get('href')
                tabsource.append(a)
                alt.append(i.find('img')['alt'])
                
            except Exception:   
               continue
        publie_par=soup.findAll('span',{'class':'user-names'})
        publie_pars=list()
        for i in publie_par:
            publie_pars.append(i.find('b').text.strip().replace('\u00c9lectronique','electronique'))    

        with open('nom_produit.csv','w') as csvFile:
            writer = csv.writer(csvFile,delimiter="\n")
            writer.writerow(alt)
        csvFile.close()
        for i,j,k,l,m,n,o,p,q in zip(noms,prixexpt,localite,dates,descriptions,tabsource,tabimag,publie_pars,alt):
            dic = {'nom':i,'prix':j,'localite':k,'publie_le':l,'description':m,'source':n,'image':o,'publie_par':p,'alt':q}
            grand.append(dic)
      
            # imagefile=open("/home/moussa/Documents/PROJET/projethtml/trouve_tout/images/"+q+".jpeg","wb")
            # imagefile.write(urllib.request.urlopen(o).read())
            # imagefile.close()
             
    except Exception:   
        continue
outfile=open("/home/moussa/Documents/PROJET/projethtml/trouve_tout/fichier.json",'w+')
rows=json.dumps(grand,indent=4)
outfile.write(rows)

es = Elasticsearch()
es.indices.delete(index='trouve', ignore=[400, 404])
 
with open("/home/moussa/Documents/PROJET/projethtml/trouve_tout/fichier.json") as json_file:
    json_docs = json.load(json_file)
for i in json_docs:
    es.index(index='trouve', doc_type='tout',body=i)
a=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
print("nouvel connection le",a)    