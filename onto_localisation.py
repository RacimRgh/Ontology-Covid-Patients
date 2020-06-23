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
        wil = types.new_class(nom_wil, (Localisation,))
    # for index_c, row_c in df_cm.iterrows():
    #     if (row_c['wilaya_id'] == row['code']):
    #         nom_cmn = row_c['nom'].replace(' ', '')
    #         commune = URIRef(myOntology[nom_cmn])
    #         g.add((commune, RDF.type, myOntology[nom_wil]))
    #         g.add((commune, RDFS.Literal, myOntology[nom_wil]))

# Output vers le fichier .owl
onto.save(file='maladies.owl', format='ntriples')

exec(open('onto_patient.py').read())
