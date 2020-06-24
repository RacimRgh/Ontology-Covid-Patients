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

for index, row in df.iterrows():

    nom_wil = row['nom'].replace(' ', '')
    # Ajouter la wilaya dans l'ontologie
    with onto:
        Wil = type(nom_wil, (Localisation, ), {})
liste_communes = []
# Récupérer toutes les communes
for index_c, row_c in df_cm.iterrows():
    liste_communes.append([row_c['wilaya_id'], row_c['nom']])
# Parcourir les classes wilayas
liste_classes = list(onto.classes())
for i in range(19, 66):
    for elt in liste_communes:
        if(elt[0] == i-18):
            cmn = liste_classes[i]()
            cmn.name = elt[1]
            break
#     for index_c, row_c in df_cm.iterrows():
#         if (row_c['wilaya_id'] == i-18):
#             print(str(row_c['wilaya_id']) + ' : '+str(i-18))
#             nom_cmn = row_c['nom'].replace(' ', '')
#             # Ajouter les instances(Communes)
#             print(liste_classes[i])
#             cmn = liste_classes[i]
#             cmn.name = nom_cmn

# Output vers le fichier .owl
onto.save(file='maladies.owl', format='ntriples')

exec(open('onto_patient.py').read())
