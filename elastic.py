from flask import Flask, render_template, request, flash, redirect
from elasticsearch import Elasticsearch
import sys, json

app = Flask(__name__)
es = Elasticsearch()
 
@app.route('/', methods=['GET', 'POST'])
def home():
    q = request.form.get("q")
    if q is not None:
        resp = es.search(index='trouve',doc_type='tout',
        size=1000,
        body={
            "query":{
            "multi_match" : {
                "query": q,
                "fields": [
                            "nom",
                            "localite",
                            "publie_le",
                          "description",
                            "source",
                            "image",
                            "publie_par",
                            "prix",
                            "alt"
                        
                     ]  
            }}})
        a=resp['hits']['hits']
        return render_template('elastic.html',q=q,reponse=a)

    return render_template('elastic.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)