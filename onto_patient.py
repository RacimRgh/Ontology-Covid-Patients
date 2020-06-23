# OwlReady2
from owlready2 import *  # pylint: disable=unused-wildcard-import


print('Traitement patients...')
onto = get_ontology('maladies.owl')
myOntology = 'http://www.semanticweb.org/myOntology#'

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

    # class (DataProperty, FunctionalProperty):
    #     range = [str]
    #     domain = [Humain]
    class Medecin(Humain):
        pass

    class Specialite(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Medecin]

    class Patient(Humain):
        pass

onto.save(file='maladies.owl', format='ntriples')
