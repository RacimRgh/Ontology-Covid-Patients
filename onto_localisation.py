import pandas as pd
import numpy as np

from owlready2 import *  # pylint: disable=unused-wildcard-import
import types


print('Traitement localisation...')
onto = get_ontology('maladies.owl').load()
myOntology = 'http://www.semanticweb.org/myOntology#'

with onto:
    class Localisation(Thing):
        pass

# Recuperer les wilayas
df = pd.read_csv('Localisation_csv/wilayas.csv',
                 usecols=['nom', 'code'])
# Recuperer les communes
df_cm = pd.read_csv('Localisation_csv/communes.csv',
                    usecols=['nom', 'wilaya_id'])
liste_communes = []
# Récupérer toutes les communes
for index_c, row_c in df_cm.iterrows():
    liste_communes.append([row_c['wilaya_id'], row_c['nom'].replace(' ', '')])
    # liste_communes.append(row_c['nom'].replace(' ', ''))
i = 18
# Parcourir les wilayas et les créer
for index, row in df.iterrows():
    nom_wil = row['nom'].replace(' ', '')
    # Ajouter la wilaya dans l'ontologie
    with onto:
        Wil = type(nom_wil, (Localisation, ), {})
    # Parcourir les classes wilayas
    liste_classes = list(onto.classes())
    for elt in liste_communes:
        if row['code'] == elt[0]:
            print(liste_classes[i].name + ' - '+str(elt[0])+elt[1])
            commune = liste_classes[i]()
            commune.iri = myOntology + elt[1] + '_' + str(elt[0])
    i += 1

# Output vers le fichier .owl
onto.save(file='maladies.owl', format='ntriples')

exec(open('onto_patient.py').read())
