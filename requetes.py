import rdflib

graph = rdflib.Graph()
graph.parse("ontology_patients.owl", format='turtle')
graph.serialize("ontology_patients_out.rdf", "turtle")


def get_props(prop, value=None):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id ?nom ?prenom ?age ?sexe ?enceinte ?poids ?taille ?temp ?maladie
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:Nom ?nom .
        ?code ns1:Prenom ?prenom .
        ?code ns1:Age ?age .
        ?code ns1:Sexe ?sexe .
        ?code ns1:Est_Enceinte ?enceinte .
        ?code ns1:Poids ?poids .
        ?code ns1:Taille ?taille .
        ?code ns1:Temperature ?temp .
        ?code rdf:type ns1:Patient .
        ?code ns1:{prop} ?maladie
    }}
    """
    resultat = graph.query(requete)
    for res in list(resultat):
        for x in list(res):
            print(x)
        print('___________________________')


get_props('prend')
