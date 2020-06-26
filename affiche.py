from owlready2 import *  # pylint: disable=unused-wildcard-import


onto = get_ontology('maladies.owl').load()
myOntology = 'http://www.semanticweb.org/racim_katia/maladies.owl#'
classes = list(onto.classes())
individus = list(onto.individuals())
i = 0
# j = 0
# for x in individus:
#     print(j)
#     print(x.iri)
#     print(x.namespace)
#     print(x.name)
#     print('_______________________\n')
#     j += 1


for y in classes:
    print(i)
    print(y.iri)
    print(y.namespace)
    print(y.name)
    print('_______________________\n')
    i += 1
