import rdflib

graph = rdflib.Graph()
graph.parse("ontology_patients.owl", format='turtle')
graph.serialize("ontology_patients_out.rdf", "turtle")


def get_props(prop='prend'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id ?nom ?valeur
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:Nom ?nom .
        ?valeur rdf:type ns1:Traitements .
        ?code ns1:prend ?valeur
    }}
    """
    return graph.query(requete)


# Requete pour avoir les patients selon leur age
def get_multiples_conditions(agep=150, sexep='.', poidsp=0, taillep=0, temp=35, enceintep=False):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id ?age ?sexe ?poids ?taille ?temperature ?enceinte
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:Age ?age .
        ?code ns1:Sexe ?sexe .
        ?code ns1:Poids ?poids .
        ?code ns1:Taille ?taille .
        ?code ns1:Temperature ?temperature .
        ?code ns1:Est_Enceinte ?enceinte .
        FILTER((?age < {agep}) 
            && regex(?sexe, '{sexep}') 
            && (?poids > {poidsp}) 
            && (?taille > {taillep}) 
            && (?temperature > {temp})
            && (?enceinte = {enceintep}))
    }}
    """
    return graph.query(requete)


# Requete pour avoir les patients selon leurs localisation
def get_selon_localisation(wilaya='Alger'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id ?nom ?adr
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:Nom ?nom .
        ?adr rdf:type ns1:{wilaya} .
        ?code ns1:habite_a ?adr
    }}
    """
    return graph.query(requete)


# Requete pour avoir les patients selon leurs localisation
def get_selon_maladie(maladiep='cancer'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id ?nom ?adr
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:Nom ?nom .
        ?adr rdf:type ns1:{maladiep} .
        ?code ns1:est_atteint_de ?adr
    }}
    """
    return graph.query(requete)


# resultat = get_multiples_conditions()
# resultat = get_selon_maladie('rhumatologie')
resultat = get_props('est_atteint_de')
print(len(list(resultat)))
for res in list(resultat):
    for x in list(res):
        print(x)
    print('___________________________')
