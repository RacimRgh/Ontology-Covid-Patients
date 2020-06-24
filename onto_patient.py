# OwlReady2
from owlready2 import *  # pylint: disable=unused-wildcard-import

# pylint: disable=undefined-variable

print('Traitement patients...')
onto = get_ontology('maladies.owl').load()
myOntology = 'http://www.semanticweb.org/myOntology#'
classes = list(onto.classes())
i = 0
for x in classes:
    print(str(i)+' '+x.name)
    i += 1
with onto:
    class Humain(Thing):
        pass

    class Nom(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Humain]

    class Prenom(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Humain]

    class Age(DataProperty, FunctionalProperty):
        range = [int]
        domain = [Humain]

    class Medecin(Humain):
        pass

    class Specialite(DataProperty):
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

    class Consultation(Thing):
        pass

    class date_consultation(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Consultation]

    class cause_consultation(DataProperty):
        range = [str]
        domain = [Consultation]
    # Patient reserve une consultation

    class Patient(Humain):
        pass

    class reserve(Patient >> Consultation):
        pass

    class Enfant(Patient):
        pass

    class Adulte(Patient):
        pass

    class Femme(Adulte):
        pass

    class Homme(Adulte):
        pass

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

onto.save(file='maladies.owl', format='ntriples')
