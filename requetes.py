
# Requete pour avoir les patients selon les objects properties (relations)
# prend - habite_a - est_atteint_de - présente -ausculté_par - orienté_vers
def get_selon_obj_props(graph, prop='prend'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id ?nom ?prenom ?valeur
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:Nom ?nom .
        ?code ns1:Prenom ?prenom .
        ?code ns1:{prop} ?valeur
    }}
    """
    return graph.query(requete)


# Requete pour avoir les patients selon une ou plusieurs de leurs data properties
# Les arguments sont optionnels, pour en choisir un il suffit de faire l'appel comme cet exemple
# get_selon_data_prop(sexep='f', temp=37)
def get_selon_data_prop(graph, agep=150, sexep='.', poidsp=0, taillep=0, temp=35):
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
        ?code ns1:Suspicion_Covid ?susp .
        FILTER((?age < {agep})
            && regex(?sexe, '{sexep}', 'i')
            && (?poids > {poidsp})
            && (?taille > {taillep})
            && (?temperature > {temp})
            && (?susp = true))
    }}
    """
    return graph.query(requete)


# Requete pour avoir les patients selon leur Wilaya
def get_selon_wilaya(graph, wilaya='Alger'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id ?nom ?prenom ?adr
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:Nom ?nom .
        ?prenom ns1:Prenom ?prenom .
        ?adr rdf:type ns1:{wilaya} .
        ?code ns1:habite_a ?adr
    }}
    """
    return graph.query(requete)


# Requete pour avoir les patients selon le type de maladie
# Les types de maladies sont les sous classes de 'Maladies'
def get_selon_type_maladie(graph, maladiep='pneumologie'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id ?nom ?maladie
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:Nom ?nom .
        ?maladie rdf:type ns1:{maladiep} .
        ?code ns1:est_atteint_de ?maladie
    }}
    """
    return graph.query(requete)


# Requete pour avoir les patients selon les noms de maladies
def get_selon_nom_maladie(graph, mld='pneumonie'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id ?nom ?maladie
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:Nom ?nom .
        ?code ns1:est_atteint_de ?maladie .
        ?code ns1:est_atteint_de ns1:{mld} .
    }}
    """
    return graph.query(requete)
# Requete pour avoir les patients selon les médicaments qu'ils prennent


def get_selon_traitement(graph, medic='paracétamol'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id ?nom ?traitement
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:Nom ?nom .
        ?traitement rdf:type ns1:Traitements .
        ?code ns1:prend ?traitement .
        ?code ns1:prend ns1:{medic}
    }}
    """
    return graph.query(requete)


# Requete pour avoir les patients selon le medecin qui les a ausculté
def get_selon_medecin(graph, nom='Aissat_Abdelhak'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id ?code_med
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code_med rdf:type ns1:Medecin .
        ?code ns1:ausculté_par ?code_med .
        ?code ns1:ausculté_par ns1:{nom}
    }}
    """
    return graph.query(requete)


# Requete pour avoir les patients selon la gravité de symptomes
def get_selon_gravité(graph, gravité='sévère'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id ?etat_p
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:Gravité_symptomes ?etat_p
        FILTER regex(?etat_p, '{gravité}', 'i')
    }}
    """
    return graph.query(requete)


# Requete pour avoir les patients et medecins selon la date de consultation
def get_selon_date_consultation(graph, date='2020'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT ?id_m ?date_p ?id_p ?nomp ?prenomp
    WHERE{{
        ?codem rdf:type ns1:Medecin .
        ?codem ns1:ID ?id_m .
        ?codem ns1:Date_Consultation ?date_p .
        ?codep rdf:type ns1:Patient .
        ?codep ns1:ID ?id_p .
        ?codep ns1:Nom ?nomp .
        ?codep ns1:Prenom ?prenomp .
        ?codem ns1:a_ausculté ?codep .
        FILTER CONTAINS(?date_p, '{date}')
    }}
    """
    return graph.query(requete)


# Requete pour récupérer le nombre de patients suspectés de covid à une date donnée
def get_nombre_covid_date(graph, date='2020'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT (COUNT(?susp) as ?countp)
    WHERE{{
        ?codem rdf:type ns1:Medecin .
        ?codem ns1:ID ?id_m .
        ?codem ns1:Date_Consultation ?date_p .
        ?codep rdf:type ns1:Patient .
        ?codep ns1:ID ?id_p .
        ?codem ns1:a_ausculté ?codep .
        ?codep ns1:Suspicion_Covid ?susp .
        FILTER (?susp = true)
        FILTER CONTAINS(?date_p, '{date}')
    }}
    GROUP BY ?susp
    """
    return graph.query(requete)


# Requete pour récupérer le nombre de patients atteints de covid détectés par un medecin
def get_nombre_covid_medecin(graph):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT (COUNT(?id_m) as ?idm)
    WHERE{{
        ?codem rdf:type ns1:Medecin .
        ?codem ns1:ID ?id_m .
        ?codep rdf:type ns1:Patient .
        ?codep ns1:ID ?id_p .
        ?codem ns1:a_ausculté ?codep .
        ?codep ns1:Suspicion_Covid ?susp .
        FILTER (?susp = true)
    }}
    GROUP BY ?susp
    """
    return graph.query(requete)


# Requete pour avoir le nombre de patients atteints selon la wilaya
def get_nombre_par_wilaya(graph, wilaya='Alger'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT (COUNT(?susp) as ?countp)
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:Nom ?nom .
        ?adr rdf:type ns1:{wilaya} .
        ?code ns1:habite_a ?adr .
        ?code ns1:Suspicion_Covid ?susp .
        FILTER (?susp = true)
    }}
    GROUP BY ?susp
    """
    return graph.query(requete)


# Requete pour avoir le nombre de patient selon l'une des valeurs des propriétés
def get_nombre_prop_valeur(graph, prop='orienté_vers', valeur='Hopital'):
    requete = f"""
    prefix ns1: <http://www.semanticweb.org/racim_katia/ontology_covid#>
    prefix ns2: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    SELECT (COUNT(?id) as ?idp)
    WHERE{{
        ?code rdf:type ns1:Patient .
        ?code ns1:ID ?id .
        ?code ns1:{prop} ns1:{valeur}
    }}
    GROUP BY ?{valeur}
    """
    return graph.query(requete)


# Fonction pour imprimer le résultat directement sur l'écran (sans traitement)
def print_resultat(resultat):
    for res in list(resultat):
        for x in list(res):
            print(x)
        print('___________________________')


# Fonction pour arranger les résultat et les mettre dans un dictionnaire (utile pour get_selon_obj_props seulement)
# Cette fonction va prendre les maladies/traitements/symptomes du patient, les mettre dans une
# seule liste, puis mettre le code, nom, prenom et la liste dans une dictionnaire python
def formater_resultat(resultat):
    j = 0
    i = 0
    list_dic = []
    while i < len(list(resultat)):
        list_mald = []
        dic_mld = {}
        j = i + 1
        code = list(resultat)[i][0]
        nom = list(resultat)[i][1]
        prenom = list(resultat)[i][2]
        list_mald.append(str(list(resultat)[i][-1]))
        while j < len(resultat) and code == list(resultat)[j][0]:
            list_mald.append(str(list(resultat)[j][-1]))
            j += 1
        i = j
        dic_mld = {
            'ID': str(code),
            'Nom': str(nom),
            'Prenom': str(prenom),
            'Maladies': list_mald}
        list_dic.append(dic_mld)
    for elt in list_dic:
        print(elt)
        print('______________')


# resultat = get_selon_obj_props('prend')
# resultat = get_selon_data_prop(sexep='m')
# resultat = get_selon_wilaya('TiziOuzou')
# resultat = get_selon_type_maladie('rhumatologie')
# resultat = get_selon_traitement()
# resultat = get_selon_nom_maladie('scoliose')
# resultat = get_selon_medecin()
# resultat = get_selon_gravité()
# resultat = get_selon_date_consultation('2020')
# resultat = get_nombre_covid_date()
# resultat = get_nombre_covid_medecin()
# resultat = get_nombre_par_wilaya()
# resultat = get_nombre_prop_valeur()
# print_resultat(resultat)
