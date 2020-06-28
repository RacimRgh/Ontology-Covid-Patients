from owlready2 import *  # pylint: disable = unused-wildcard-import
import pandas as pd
from onto_functions import get_num_classe, get_num_individu

# pylint: disable=unused-variable


def creation_fiche_medecin(onto):
    print('Traitement fichier medecin...')
    # Récupérer une liste de toutes les classes de l'onto
    classes = list(onto.classes())
    individus = list(onto.individuals())
    # Lire le fichier qui contient les infos sur les patients
    fiche_df = pd.read_csv('Data/rapport_du_medecin.csv')

    # On parcourt le fichier qui contient les infos remplies par le médecin sur le patient
    for index, row in fiche_df.iterrows():
        # Récupérer le code du patient consulté
        code_patient = get_num_individu(row['A consulté le patient'], onto)
        patient = individus[code_patient]
        # Instancier le médecin
        medecin = classes[get_num_classe('Medecin', onto)]()
        medecin.name = str(row['Nom']) + '_' + str(row['Prénom'])
        medecin.Nom = row['Nom']
        medecin.Prenom.append(row['Prénom'])
        medecin.Spécialité.append(row['Spécialité'])
        # Ajouter la consultation
        medecin.Date_Consultation.append(row['Date consultation'])
        # Infos sur le patient
        patient.ausculté_par.append(onto.search(iri='*'+medecin.name)[0])
        patient.Gravité_symptomes.append(row['Gravité symptomes'])
        # Orientation du patient par le medecin
        patient.orienté_vers.append(onto.search(iri='*'+row['Orientation'])[0])
        patient.Prise_En_Charge.append(row['Prise en charge'])

    # Output vers le fichier .owl
    # onto.save(file='ontology_patients.owl', format='ntriples')

    return onto
