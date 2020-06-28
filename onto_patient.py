# OwlReady2
from owlready2 import *    # pylint: disable=unused-wildcard-import
from onto_functions import get_num_classe
# pylint: disable=undefined-variable
# pylint: disable=unused-variable


def create_patient(onto):
    print('Traitement patients...')
    # Récuperer toutes les classes dans une liste
    classes = list(onto.classes())
    with onto:
        class Humain(Thing):
            pass

        class Nom(DataProperty, FunctionalProperty):
            range = [str]
            domain = [Humain]

        class Prenom(DataProperty):
            range = [str]
            domain = [Humain]

        class Age(DataProperty, FunctionalProperty):
            range = [int]
            domain = [Humain]

        class Medecin(Humain):
            pass

        class Spécialité(DataProperty):
            range = [str]
            domain = [Medecin]
            pass

        class Date_Consultation(DataProperty):
            range = [str]
            domain = [Medecin]

        # Symptomes du Covid

        class Symptomes(Thing):
            pass
        # Instanciation des symptomes
        sympt = [
            'courbatures',
            'diarhee',
            'difficulté_respiration',
            'décoloration_des_doigts',
            'essoufflement',
            'fatigue_inhabituelle',
            'fièvre',
            'mal_de_gorge',
            'maux_de_tête',
            'perte_du_goût',
            'perte_odorat',
            'toux_sèche',
            'toux',
            'éruption_cutanée'
        ]
        for x in sympt:
            symptome = Symptomes(x)

        # Patient reserve une consultation

        class Patient(Humain):
            pass

        class Sexe(DataProperty, FunctionalProperty):
            range = [str]
            domain = [Patient]
            pass

        # Patient est atteint de maladies

        class est_atteint_de(Patient >> classes[get_num_classe('Maladies', onto)]):
            pass

        # Patient prend des traitements

        class prend(Patient >> classes[get_num_classe('Traitements', onto)]):
            pass

        # Patient habite dans une Localisation (wilaya et commune)

        class habite_a(Patient >> classes[get_num_classe('Localisation', onto)]):
            pass

        # Patient présente des symptomes

        class présente(Patient >> Symptomes):
            pass

        class Est_Enceinte(DataProperty, FunctionalProperty):
            range = [bool]
            domain = [Patient]

        class Poids(DataProperty, FunctionalProperty):
            range = [float]
            domain = [Patient]

        class ID(DataProperty, FunctionalProperty):
            range = [str]
            domain = [Patient]
            pass

        class Taille(DataProperty, FunctionalProperty):
            range = [int]
            domain = [Patient]
            pass

        class Temperature(DataProperty, FunctionalProperty):
            range = [int]
            domain = [Patient]
            pass

        class Gravité_symptomes(DataProperty):
            range = [str]
            domain = [Patient]
            pass

        class Prise_En_Charge(DataProperty):
            range = [str]
            domain = [Patient]
            pass

        class Orientation(Thing):
            pass

        # Instanciation des Orientation
        Orientation('Hopital')
        Orientation('Maison')

        class orienté_vers(Patient >> Orientation):
            pass

        class ausculté_par(Patient >> Medecin):
            pass

        class a_ausculté(Medecin >> Patient):
            inverse_property = ausculté_par
            pass
    # Output vers le fichier .owl
    # onto.save(file='ontology_patients.owl', format='ntriples')
    return onto
