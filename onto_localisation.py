import pandas as pd
import numpy as np
# RDF imports
from rdflib import Graph, URIRef
from rdflib import Namespace
from rdflib.namespace import OWL, RDF, RDFS

print('Traitement localisation')
myOntology = Namespace('http://www.semanticweb.org/myOntology#')
g = Graph()
g.parse('maladies.owl', format='turtle')
g.bind('myOntology', myOntology)
Localisation = URIRef(myOntology['Localisation'])
# Add the OWL data to the graph
g.add((Localisation, RDF.type, OWL.Class))
g.add((Localisation, RDFS.subClassOf, OWL.Thing))
# Recuperer les wilayas
df = pd.read_csv('wilayas.csv', usecols=['nom', 'code'])
# Recuperer les communes
df_cm = pd.read_csv('communes.csv', usecols=['nom', 'wilaya_id'])
for index, row in df.iterrows():
    # Ajouter la wilaya dans l'ontologie
    nom_wil = row['nom'].replace(' ', '')
    wilaya = URIRef(myOntology[nom_wil])
    g.add((wilaya, RDF.type, OWL.Class))
    g.add((wilaya, RDFS.subClassOf, Localisation))
    for index_c, row_c in df_cm.iterrows():
        if (row_c['wilaya_id'] == row['code']):
            nom_cmn = row_c['nom'].replace(' ', '')
            commune = URIRef(myOntology[nom_cmn])
            g.add((commune, RDF.type, myOntology[nom_wil]))
            g.add((commune, RDFS.Literal, myOntology[nom_wil]))

# Output vers le fichier .owl
Graph.serialize(g, destination='maladies.owl', format='turtle')
