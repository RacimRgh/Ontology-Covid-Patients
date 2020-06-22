# Scraping imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
# RDF imports
from rdflib import Graph, URIRef, Literal
from rdflib import Namespace
from rdflib.namespace import OWL, RDF, RDFS
# Regex import
import re
# Os import pour avoir absoulute path
import os

print("Working Directory: "+os.getcwd())
print("Traitements maladies...")
myOntology = Namespace("http://www.semanticweb.org/myOntology#")
g = Graph()
g.bind("myOntology", myOntology)
Maladies = URIRef(myOntology["Maladies"])
# Add the OWL data to the graph
g.add((Maladies, RDF.type, OWL.Class))
g.add((Maladies, RDFS.subClassOf, OWL.Thing))

quote_page = 'https://www.sante-sur-le-net.com/maladies/'
# query the website and return the html to the variable ‘page’
page = urlopen(quote_page)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')
# Take out the <div> of name and get its value
name_box = soup.find(
    'div', attrs={'class': 'panel-body'})
# Récuperer les liens (href) des types de maladies
types_maladies = [i['href'] for i in name_box.find_all('a', href=True)]
noms_types = []
liste_maladies = []
# Récupérer les noms des types des maladies sans le lien complet
for mld in types_maladies:
    noms_types.append(mld.split('/')[-1])
# Parcourir chaque type de maladie
for maladie in noms_types:
    if maladie != "dermatologie" and maladie != "gynecologie":
        # Créer le concept correspondant au type de maladie
        type_m = URIRef(myOntology[maladie])
        g.add((type_m, RDF.type, OWL.Class))
        g.add((type_m, RDFS.subClassOf, Maladies))
        # Parser la liste des maladies de la catégorie
        page_maladie = urlopen(quote_page+maladie)
        soup = BeautifulSoup(page_maladie, 'html.parser')
        header_maladies = soup.find_all('h3')
        for x in header_maladies:
            lien_maladie = [i['href'] for i in x.find_all('a', href=True)]
            # Filtrer les pages pour n'avoir que des maladies dans l'ontologie
            condition = ("myopathies" not in lien_maladie[0]
                         and "definition" not in lien_maladie[0]
                         and "symptomes" not in lien_maladie[0]
                         and "qu-est-ce" not in lien_maladie[0])
            if "maladies" in lien_maladie[0] and condition:
                liste_maladies.append(lien_maladie[0].split('/')[-2])
                nom = URIRef(myOntology[lien_maladie[0].split('/')[-2]])
                g.add((nom, RDF.type, myOntology[maladie]))
                g.add((nom, RDFS.Literal, myOntology[maladie]))
# Output vers le fichier .owl
Graph.serialize(g, destination='maladies.owl', format='turtle')
# Appeller le 2ème fichier
exec(open('onto_traitement.py').read())
