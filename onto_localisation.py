import pandas as pd
import numpy as np

from owlready2 import *     # pylint: disable=unused-wildcard-import
import types

# pylint: disable=unused-variable


def create_localisation(onto, myOntology):
    print('Traitement localisation...')
    # Créer la classe Localisation
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
        liste_communes.append(
            [row_c['wilaya_id'], row_c['nom'].replace(' ', '')])
        # liste_communes.append(row_c['nom'].replace(' ', ''))
    i = 19
    # Parcourir les wilayas et les créer
    for index, row in df.iterrows():
        nom_wil = row['nom'].replace(' ', '')
        # Ajouter la wilaya dans l'ontologie
        with onto:
            type(nom_wil, (Localisation, ), {})
        # Parcourir les classes wilayas
        liste_classes = list(onto.classes())
        for elt in liste_communes:
            if row['code'] == elt[0]:
                commune = liste_classes[i]()
                commune.iri = myOntology + elt[1] + '_' + str(elt[0])
        i += 1

    # Output vers le fichier .owl
    # onto.save(file='ontology_patients.owl', format='ntriples')
    return onto
