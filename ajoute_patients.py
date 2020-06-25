from owlready2 import *  # pylint: disable=unused-wildcard-import
import rdflib
import numpy as np
import pandas as pd


def isNaN(string):
    return string != string


onto = get_ontology('maladies.owl').load()
myOntology = 'http://www.semanticweb.org/racim_katia/maladies.owl#'
classes = list(onto.classes())
# Lire le fichier qui contient les infos sur les patients
patients_df = pd.read_csv('Data/informations_patient.csv')

for index, row in patients_df.iterrows():
    patient = classes[70]
    pat = patient()
    pat.ID = row['ID']
    pat.Age = row['Age']
    pat.Nom = row['Nom']
    pat.Prenom.append(row['Prénom'])
    pat.poids = row['Poids']
    pat.est_enceinte = True if row['Enceinte'] == 'oui' else False
    # maladies = str(row['Antécédent médical']).split(',')
    medics = str(row['Traitements']).split(',')
    symptomes = str(row['Symptomes']).split(',')
    # Parcourir les maladies fournit pas le patient
    ns = myOntology + pat.ID + '/'
    for sp in symptomes:
        if (onto.search(iri='*'+sp) != []):
            symptome = classes[16]
            symp = symptome()
            symp.iri = ns + 'symptomes/' + sp.replace(' ', '')
            pat.présente.append(symp)
    for tr in medics:
        if (onto.search(iri='*'+tr) != []):
            traitement = classes[16]
            trt = traitement()
            trt.iri = ns + 'traitements/' + tr.replace(' ', '')
            pat.prend.append(trt)

            # Output vers le fichier .owl
onto.save(file='maladies.owl', format='ntriples')
