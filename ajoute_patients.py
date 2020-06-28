from owlready2 import *  # pylint: disable=unused-wildcard-import
import pandas as pd

from onto_functions import get_num_classe

# pylint: disable=unused-variable


def instancier_patients(onto):

    print('Traitement fichier patients...')
    # Récupérer une liste de toutes les classes de l'onto
    classes = list(onto.classes())
    # Lire le fichier qui contient les infos sur les patients
    patients_df = pd.read_csv('Data/informations_patient.csv')

    # Parcourir le fichier de patient ligne par ligne
    for index, row in patients_df.iterrows():
        # Récupérer le numéro de la classe Patient
        patient = classes[get_num_classe('Patient', onto)]
        pat = patient()         # Instancier le patient
        # Remplir toute les infos du patient selon les donnés du fichier csv
        pat.Sexe = row['Sexe']
        pat.name = row['ID']
        pat.ID = row['ID']
        pat.Age = row['Age']
        pat.Nom = row['Nom']
        pat.Prenom.append(row['Prénom'])
        pat.Poids = row['Poids']
        pat.Taille = row['Taille']
        pat.Temperature = row['Temperature']
        pat.Est_Enceinte = True if row['Enceinte'] == 'oui' else False
        # Traitement de la localisation
        # Récupérer le numéro de la wilaya du patient dans l'ontologie pour l'instancier
        num_wilaya = (get_num_classe(
            str(row['Wilaya']), onto) - get_num_classe('Adrar', onto) + 1)
        commune = onto.search(
            iri='*' + str(row['Commune']) + '_' + str(num_wilaya))
        pat.habite_a.append(commune[0])
        # Récupérer les maladies, symptomes et traitements fournis par le patient
        maladies = str(row['Antécédent médical']).split(',')
        medics = str(row['Traitements']).split(',')
        symptomes = str(row['Symptomes']).split(',')
        # Parcourir les symptomes mentionnés par le patient
        for sp in symptomes:
            # Vérifier que la variable n'est pas vide
            if sp != 'nan':
                # Si elle est déjà instancié, on la lie à l'object property
                if (onto.search(iri='*'+sp) != []):
                    pat.présente.append(onto.search(iri='*'+sp)[0])
                # Sinon on l'instancie
                else:
                    symptome = classes[get_num_classe('Symptomes', onto)]
                    symp = symptome(sp.replace(' ', ''))
                    pat.présente.append(symp)
        # Récupérer les traitements que prend le patient
        for tr in medics:
            if tr != 'nan':
                if (onto.search(iri='*'+tr) != []):
                    pat.prend.append(onto.search(iri='*'+tr)[0])
                else:
                    traitement = classes[get_num_classe('Traitements', onto)]
                    trait = traitement(tr.replace(' ', ''))
                    pat.prend.append(trait)
        # Parcourir les maladies mentionnés par le patient
        for md in maladies:
            if md != 'nan':
                if(onto.search(iri='*'+md) != []):
                    pat.est_atteint_de.append(onto.search(iri='*'+md)[0])
                else:
                    maladie = classes[get_num_classe('Maladies', onto)]
                    mld = maladie(md.replace(' ', ''))
                    pat.est_atteint_de.append(mld)

    # Output vers le fichier .owl
    # onto.save(file='ontology_patients.owl', format='ntriples')
    return onto
