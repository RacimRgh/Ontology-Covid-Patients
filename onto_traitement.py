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
myOntology = 'http://www.semanticweb.org/racim_katia/maladies.owl#'
# Création de la classe Traitements
with onto:
    class Traitements(Thing):
        pass

for c in ascii_uppercase:
    url = urllib.request.urlopen(
        'https://www.vidal.fr/Sommaires/Substances-'+c+'.htm')
    res = url.read().decode('utf-8')
    fin = re.findall(r'href="Substance/.*-.*.htm">(\w*)', res)
    # Parcours de tout les médicaments trouvés
    for mdc in fin:
        # Instanciation des médicaments
        medic = Traitements(mdc)

# Sauvegarder la nouvelle ontologie
onto.save(file='maladies.owl', format='ntriples')
# Appeller le 3ème fichier
exec(open('onto_localisation.py').read())
