# OwlReady2
from owlready2 import *  # pylint: disable=unused-wildcard-import
# pylint: disable=undefined-variable

print('Traitement patients...')
onto = get_ontology('maladies.owl').load()
myOntology = 'http://www.semanticweb.org/racim_katia/maladies.owl#'
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

    class spécialité(DataProperty):
        range = [str]
        domaine = [Medecin]
        pass

    class date_consultation(DataProperty):
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

    class Enfant(Patient):
        pass

    class Adulte(Patient):
        pass

    AllDisjoint([Adulte, Enfant])

    class Femme(Adulte):
        pass

    class Homme(Adulte):
        pass

    AllDisjoint([Femme, Homme])

    class Fille(Enfant):
        pass

    class Garçon(Enfant):
        pass

    AllDisjoint([Fille, Garçon])

    # Patient est attein de maladies

    class est_atteint_de(Patient >> classes[0]):
        pass

    # Patient prend des traitements

    class prend(Patient >> classes[16]):
        pass

    # Patient habite dans une commune

    class habite_a(Patient >> classes[17]):
        pass

    # Patient présente des symptomes

    class présente(Patient >> Symptomes):
        pass

    class est_enceinte(DataProperty, FunctionalProperty):
        range = [bool]
        domain = [Femme]

    class poids(DataProperty, FunctionalProperty):
        range = [float]
        domain = [Patient]

    class ID(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Patient]
        pass

    class taille(DataProperty, FunctionalProperty):
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

    class prise_en_charge(DataProperty):
        range = [str]
        domaine = [Patient]
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

onto.save(file='maladies.owl', format='ntriples')

exec(open('ajoute_patients.py').read())
