from owlready2 import *  # pylint: disable = unused-wildcard-import
import pandas as pd


# Fonction pour récupérer le numéro de la classe en connaissant son nom dans l'ontologie
def get_num_classe(nom_classe):
    classes = list(onto.classes())
    i = 0
    for cl in classes:
        if(cl.name == nom_classe):
            return i
        i += 1


def get_num_individu(nom):
    individus = list(onto.individuals())
    i = 0
    for ind in individus:
        if(ind.name == nom):
            return i
        i += 1


print('Traitement fichier medecin...')
onto = get_ontology('maladies.owl').load()
myOntology = 'http://www.semanticweb.org/racim_katia/maladies.owl#'
# Récupérer une liste de toutes les classes de l'onto
classes = list(onto.classes())
individus = list(onto.individuals())
# Lire le fichier qui contient les infos sur les patients
fiche_df = pd.read_csv('Data/rapport_du_medecin.csv')

# On parcourt le fichier qui contient les infos remplies par le médecin sur le patient
for index, row in fiche_df.iterrows():
    # Récupérer le code du patient consulté
    code_patient = get_num_individu(row['A consulté le patient'])
    patient = individus[code_patient]
    # Instancier le médecin
    medecin = classes[get_num_classe('Medecin')]()
    medecin.name = str(row['Nom']) + '_' + str(row['Prénom'])
    medecin.Nom = row['Nom']
    medecin.Prenom.append(row['Prénom'])
    medecin.spécialité.append(row['Spécialité'])
    # Ajouter la consultation
    medecin.date_consultation.append(row['Date consultation'])
    # Infos sur le patient
    patient.ausculté_par.append(onto.search(iri='*'+medecin.name)[0])
    patient.Gravité_symptomes.append(row['Gravité symptomes'])
    # Orientation du patient par le medecin
    patient.orienté_vers.append(onto.search(iri='*'+row['Orientation'])[0])
    patient.prise_en_charge.append(row['Prise en charge'])

# Output vers le fichier .owl
onto.save(file='maladies.owl', format='ntriples')
