from owlready2 import *  # pylint: disable = unused-wildcard-import


# Fonction pour récupérer le numéro de la classe en connaissant son nom dans l'ontologie
def get_num_classe(nom_classe, onto):
    classes = list(onto.classes())
    i = 0
    for cl in classes:
        if(cl.name == nom_classe):
            return i
        i += 1


# Fonction pour récupérer le numéro de l'individu en connaisant son IRI dans l'ontologie
def get_num_individu(nom, onto):
    individus = list(onto.individuals())
    i = 0
    for ind in individus:
        if(ind.name == nom):
            return i
        i += 1


# Fonction pour vérifier si une maladie existe déjà pour éviter le problème d'unicité d'IRI
def maladie_existe(onto, nom):
    individus = list(onto.individuals())
    for elt in individus:
        if elt.name == nom:
            return True
    return False
