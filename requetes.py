import rdflib

graph = rdflib.Graph()
graph.parse("maladies.owl", format='turtle')
graph.serialize("maladies_out.rdf", "turtle")
prop = "présente"
requete = f""" 
prefix ns1: <http://www.semanticweb.org/racim_katia/maladies.owl#>
prefix ns2: <http://www.w3.org/2002/07/owl#>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix xml: <http://www.w3.org/XML/1998/namespace>
SELECT ?id ?maladie ?nom
WHERE{{
    ?code rdf:type ns1:Patient .
    ?code ns1:ID ?id .
    ?code rdf:type ns1:Patient .
    ?code ns1:{prop} ?maladie .
    ?code rdf:type ns1:Patient .
    ?code ns1:Nom ?nom
}}"""
# ?nom rdf:type ns1:Femme .
#     ?nom ns1:Nom ?name .
#     ?pren rdf:type ns1:Femme .
#     ?pren ns1:Prenom ?prenom .
resultat = graph.query(requete)
for i in list(resultat):
    # print(list(i)[1])
    print(i)
