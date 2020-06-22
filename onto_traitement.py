import urllib.request
import re
import sys
import os
from http import server, HTTPStatus
from string import ascii_uppercase
# RDF imports
from rdflib import Graph, URIRef
from rdflib import Namespace
from rdflib.namespace import OWL, RDF, RDFS

print('Traitement médicaments...')
myOntology = Namespace("http://www.semanticweb.org/myOntology#")
g = Graph()
g.parse('maladies.owl', format='turtle')
g.bind("myOntology", myOntology)
Traitements = URIRef(myOntology["Traitements"])
# Add the OWL data to the graph
g.add((Traitements, RDF.type, OWL.Class))
g.add((Traitements, RDFS.subClassOf, OWL.Thing))

for c in ascii_uppercase:
    lettre = URIRef(myOntology[c])
    g.add((lettre, RDF.type, OWL.Class))
    g.add((lettre, RDFS.subClassOf, Traitements))
    url = urllib.request.urlopen(
        'https://www.vidal.fr/Sommaires/Substances-'+c+'.htm')
    res = url.read().decode('utf-8')
    fin = re.findall(r'href="Substance/.*-.*.htm">(\w*)', res)
    for mdc in fin:
        medic = URIRef(mdc)
        g.add((medic, RDF.type, myOntology[c]))
        g.add((medic, RDFS.Literal, myOntology[c]))

# Output vers le fichier .owl
Graph.serialize(g, destination='maladies.owl', format='turtle')
