from owlready2 import *  # pylint: disable=unused-wildcard-import
import rdflib
import numpy as np
import pandas as pd


# Fonction pour récupérer le numéro de la classe en connaissant son nom dans l'ontologie
def get_num_classe(nom_classe):
    classes = list(onto.classes())
    i = 0
    for cl in classes:
        if(cl.name == nom_classe):
            return i
        i += 1


onto = get_ontology('maladies.owl').load()
myOntology = 'http://www.semanticweb.org/racim_katia/maladies.owl#'
# Récupérer une liste de toutes les classes de l'onto
classes = list(onto.classes())
# Lire le fichier qui contient les infos sur les patients
patients_df = pd.read_csv('Data/informations_patient.csv')

# Parcourir le fichier de patient ligne par ligne
for index, row in patients_df.iterrows():
    # Instancier le patient selon l'age et le sexe (enfant/adulte) (homme/femme)
    if (row['Age'] > 16):
        if(row['Sexe'] == 'femme'):
            patient = classes[get_num_classe('Femme')]
        else:
            patient = classes[get_num_classe('Homme')]
    else:
        if(row['Sexe'] == 'femme'):
            patient = classes[get_num_classe('Fille')]
        else:
            patient = classes[get_num_classe('Garçon')]
    pat = patient()         # Instancier le patient
    pat.name = row['ID']
    pat.ID = row['ID']
    pat.Age = row['Age']
    pat.Nom = row['Nom']
    pat.Prenom.append(row['Prénom'])
    pat.poids = row['Poids']
    pat.est_enceinte = True if row['Enceinte'] == 'oui' else False
    maladies = str(row['Antécédent médical']).split(',')
    medics = str(row['Traitements']).split(',')
    symptomes = str(row['Symptomes']).split(',')
    # Parcourir les symptomes mentionnés par le patient
    for sp in symptomes:
        if sp != 'nan':
            if (onto.search(iri='*'+sp) != []):
                pat.présente.append(onto.search(iri='*'+sp)[0])
            # ns = get_ontology(myOntology + pat.ID + '/' + 'symptomes/')
            # symptome = classes[16]
            # symp = symptome()
            # symp.iri = ns + sp.replace(' ', '')
    # Récupérer les traitements que prend le patient
    for tr in medics:
        if tr != 'nan':
            if (onto.search(iri='*'+tr) != []):
                pat.prend.append(onto.search(iri='*'+tr)[0])
            # ns = get_ontology(myOntology + pat.ID + '/' + 'traitements/')
            # traitement = classes[16]
            # trt = traitement()
            # trt.iri = ns + tr.replace(' ', '')
    # Parcourir les maladies mentionnés par le patient
    for md in maladies:
        if md != 'nan':
            if(onto.search(iri='*'+md) != []):
                pat.est_atteint_de.append(onto.search(iri='*'+md)[0])
            # Output vers le fichier .owl
onto.save(file='maladies.owl', format='ntriples')
