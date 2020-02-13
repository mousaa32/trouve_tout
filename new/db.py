from flask import Flask,render_template,request,redirect,url_for,flash,session,escape
import psycopg2 as psy
import os,json,csv,pandas
##*******************connection database***************************#########
def connexiondb():
    try:
        con = psy.connect(
                host="localhost",
                database="trouve_tout",
                user="postgres",
                password="Diop1957+",
                port=5432
                )
        return con
    except(Exception) as error:
        print("probleme connection",error)
con = connexiondb()
cur = con.cursor()
##*******************drop table & create it***************************#########

cur.execute("drop table produit ")
con.commit()
cur.execute("""CREATE TABLE  IF NOT EXISTS produit (
                        id_produit Int PRIMARY KEY NOT NULL,
                        nom_produit text,
                        prix_produit text, 
                        source_produit text,
                        image_produit text,
                        alt_produit text,           
                        logo text, 
                        categorie text
                                   )""")    

con.commit()
# ####*******************conversion du fichier json vers csv***************************#########
# with open("/home/moussa/Documents/PROJET/projethtml/trouve_tout/new/fichier.json") as json_file:
#     json_docs = json.load(json_file)
# pandas.read_json(json.dumps(json_docs)).to_csv('/home/moussa/Documents/PROJET/projethtml/trouve_tout/new/pandas.csv')
####*******************charger les donnees vers postgresql***************************#########
with open("/home/moussa/Documents/PROJET/projethtml/trouve_tout/new/pandas.csv",'r') as f:
    file_csv =csv.reader(f)  
    for row in file_csv:
        cur.execute("""INSERT INTO produit VALUES (%s, %s, %s, %s, %s, %s,%s,%s)""",row )
con.commit()

app = Flask(__name__)
app.secret_key="flash message"
#####*********************************************Categorie vehicules*****************************************************#########

#####*******************vehicule/voiture***************************#########
def voiture():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Voitures' """)
    voiture =cur.fetchall()
    con.commit()
    return voiture
#print(voiture())
#####*******************vehicule/Motos_Scooters***************************#########
def Motos_Scooters():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Motos & Scooters' """)
    Motos_Scooters =cur.fetchall()
    con.commit()
    return Motos_Scooters
#print(Motos_Scooters())

#####*******************vehicule/Location_de_vehicules***************************#########
def Location_de_vehicules():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Location de vehicules' """)
    Location_de_vehicules =cur.fetchall()
    con.commit()
    return Location_de_vehicules
#print(Location_de_vehicules())

#####*******************vehicule/Camions_Bus***************************#########
def Camions_Bus():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Camions & Bus' """)
    Camions_Bus =cur.fetchall()
    con.commit()
    return Camions_Bus
#print(Camions_Bus())

#####*******************vehicule/Pieces_detachees***************************#########
def Pieces_detachees():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Pieces detachees' """)
    Pieces_detachees =cur.fetchall()
    con.commit()
    return Pieces_detachees
#print(Pieces_detachees())

#####*******************vehicule/Bateaux***************************#########
def Bateaux():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Vehicules  - Bateaux' """)
    Bateaux =cur.fetchall()
    con.commit()
    return Bateaux
#print(Bateaux())

#####*********************************************Categories immobilier*****************************************************#########
#####*******************immobilier/Villas***************************#########
def Villas():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Villas' """)
    Villas =cur.fetchall()
    con.commit()
    return Villas
# print(Villas())

#####*******************immobilier/Immeubles***************************#########
def Immeubles():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Immeubles' """)
    Immeubles =cur.fetchall()
    con.commit()
    return Immeubles
# print(Immeubles())

#####*******************immobilier/Terrains***************************#########
def Terrains():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Terrains' """)
    Terrains =cur.fetchall()
    con.commit()
    return Terrains
# print(Terrains())

#####*******************immobilier/Appartements***************************#########
def Appartements():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Appartements' """)
    Appartements =cur.fetchall()
    con.commit()
    return Appartements
# print(Appartements())

#####*******************immobilier/Bureaux_Commerces***************************#########
def Bureaux_Commerces():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Bureaux & Commerces' """)
    Bureaux_Commerces =cur.fetchall()
    con.commit()
    return Bureaux_Commerces
# print(Bureaux_Commerces())

#####*******************immobilier/Maisons_de_vacances***************************#########
def Maisons_de_vacances():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Maisons de vacances' """)
    Maisons_de_vacances =cur.fetchall()
    con.commit()
    return Maisons_de_vacances
# print(Maisons_de_vacances())

#####*******************immobilier/Chambres***************************#########
def Chambres():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Chambres' """)
    Chambres =cur.fetchall()
    con.commit()
    return Chambres
# print(Chambres())

#####*********************************************Categorie electroniques*****************************************************#########
#####*******************electroniques/Imprimantes_Photocopieurs***************************#########
def Imprimantes_Photocopieurs():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Imprimantes & Photocopieurs' """)
    Imprimantes_Photocopieurs =cur.fetchall()
    con.commit()
    return Imprimantes_Photocopieurs
#print(Imprimantes_Photocopieurs())

#####*******************electroniques/Montres_connectees_GPS***************************#########
def Montres_connectees_GPS():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Montres connectees & GPS' """)
    Montres_connectees_GPS =cur.fetchall()
    con.commit()
    return Montres_connectees_GPS
#print(Montres_connectees_GPS())

#####*******************electroniques/Appareils_photos_et_Cameras***************************#########
def Appareils_photos_et_Cameras():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Appareils photos et Cameras' """)
    Appareils_photos_et_Cameras =cur.fetchall()
    con.commit()
    return Appareils_photos_et_Cameras
#print(Appareils_photos_et_Cameras())

#####*******************electroniques/TV_box_Video_projecteurs***************************#########
def TV_box_Video_projecteurs():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='TV ;box  & Video projecteurs' """)
    TV_box_Video_projecteurs =cur.fetchall()
    con.commit()
    return TV_box_Video_projecteurs
#print(TV_box_Video_projecteurs())

#####*******************electroniques/Accessoires_Telephonie***************************#########
def Accessoires_Telephonie():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Accessoires Telephonie' """)
    Accessoires_Telephonie =cur.fetchall()
    con.commit()
    return Accessoires_Telephonie
#print(Accessoires_Telephonie())

#####*******************electroniques/Jeux_video_Consoles***************************#########
def Jeux_video_Consoles():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Jeux video & Consoles' """)
    Jeux_video_Consoles =cur.fetchall()
    con.commit()
    return Jeux_video_Consoles
#print(Jeux_video_Consoles())

#####*******************electroniques/Accessoires_Informatiques***************************#########
def Accessoires_Informatiques():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Accessoires Informatiques' """)
    Accessoires_Informatiques =cur.fetchall()
    con.commit()
    return Accessoires_Informatiques
#print(Accessoires_Informatiques())

#####*******************electroniques/Son_Hifi_Casques***************************#########
def Son_Hifi_Casques():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Son Hifi & Casques' """)
    Son_Hifi_Casques =cur.fetchall()
    con.commit()
    return Son_Hifi_Casques
#print(Son_Hifi_Casques())

#####*******************electroniques/Ordinateurs***************************#########
def Ordinateurs():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Ordinateurs' """)
    Ordinateurs =cur.fetchall()
    con.commit()
    return Ordinateurs
#print(Ordinateurs())

#####*******************electroniques/Telephones_Tablettes***************************#########
def Telephones_Tablettes():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Telephones & Tablettes' """)
    Telephones_Tablettes =cur.fetchall()
    con.commit()
    return Telephones_Tablettes
#print(Telephones_Tablettes())

#####*******************electroniques/Telephonie_et_mobiles***************************#########
def Telephonie_et_mobiles():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Telephonie et mobiles' """)
    Telephonie_et_mobiles =cur.fetchall()
    con.commit()
    return Telephonie_et_mobiles
#print(Telephonie_et_mobiles())

#####*******************electroniques/Informatiques***************************#########
def Informatiques():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Informatiques' """)
    Informatiques =cur.fetchall()
    con.commit()
    return Informatiques
#print(Informatiques())

#####*******************electroniques/Autres_electronique***************************#########
def Autres_electronique():
    cur.execute("""SELECT nom_produit, prix_produit, source_produit, image_produit, alt_produit, logo, categorie
	FROM public.produit where categorie ='Autres electronique' """)
    Autres_electronique =cur.fetchall()
    con.commit()
    return Autres_electronique
# print(Autres_electronique())

@app.route('/')
def index():
    return render_template('pages/index.html')



if __name__ == '__main__':
    app.run(debug=True)