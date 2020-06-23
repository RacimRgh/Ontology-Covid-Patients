import urllib.request
import re
import sys
import os
from http import server, HTTPStatus
from string import ascii_uppercase
from owlready2 import *  # pylint: disable=unused-wildcard-import
import types

print('Traitement médicaments...')

onto = get_ontology('maladies.owl').load()
myOntology = 'http://www.semanticweb.org/myOntology#'
# Création de la classe Traitements
with onto:
    class Traitements(Thing):
        pass

for c in ascii_uppercase:
    url = urllib.request.urlopen(
        'https://www.vidal.fr/Sommaires/Substances-'+c+'.htm')
    res = url.read().decode('utf-8')
    fin = re.findall(r'href="Substance/.*-.*.htm">(\w*)', res)
    # for mdc in fin:
    #     medic = URIRef(mdc)
    #     g.add((medic, RDF.type, Traitements))
    #     g.add((medic, RDFS.Literal, Traitements))

# Sauvegarder la nouvelle ontologie
onto.save(file='maladies.owl', format='ntriples')
# Appeller le 3ème fichier
exec(open('onto_localisation.py').read())
