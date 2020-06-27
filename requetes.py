import rdflib

graph = rdflib.Graph()
graph.parse("maladies.owl", format='turtle')
graph.serialize("maladies_out.rdf", "turtle")
