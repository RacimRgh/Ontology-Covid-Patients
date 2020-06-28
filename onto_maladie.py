# Scraping imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
# Regex import
import re
# Owlready
from owlready2 import *  # pylint: disable=unused-wildcard-import
import types
# Os import pour la gestion des path
import os
# Importer les fonctions nécessaire qu'on a créés
from onto_functions import maladie_existe


def create_maladies(onto, myOntology):
    print("Working Directory: "+os.getcwd())
    print("Traitement maladies...")
    # Création de la classe Maladies
    with onto:
        class Maladies(Thing):
            pass
    # Récuperation du site des maladies et leurs types
    quote_page = 'https://www.sante-sur-le-net.com/maladies/'
    # query the website and return the html to the variable ‘page’
    page = urlopen(quote_page)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    # Take out the <div> of name and get its value
    name_box = soup.find(
        'div', attrs={'class': 'panel-body'})

    # Récuperer les liens (href) des types de maladies
    types_maladies = [i['href'] for i in name_box.find_all('a', href=True)]
    noms_types = []  # list qui va contenir les types de maladies
    liste_maladies = []  # list qui va contenir les noms des maladies
    i = 1
    # Récupérer les noms des types des maladies sans le lien complet
    for mld in types_maladies:
        noms_types.append(mld.split('/')[-1])

    # Parcourir chaque type de maladie
    for maladie in noms_types:
        if maladie != "gynecologie" and maladie != "ophtalmologie":
            # Création de chaque type de maladie
            with onto:
                types.new_class(maladie, (Maladies,))

            # Récupération des maladies de chaque type
            page_maladie = urlopen(quote_page+maladie)
            soup = BeautifulSoup(page_maladie, 'html.parser')
            header_maladies = soup.find_all('h3')
            for x in header_maladies:
                lien_maladie = [i['href'] for i in x.find_all('a', href=True)]
                # Filtrer les pages pour n'avoir que des maladies dans l'ontologie
                condition = ("myopathies" not in lien_maladie[0]
                             and "definition" not in lien_maladie[0]
                             and "symptomes" not in lien_maladie[0]
                             and "qu-est-ce" not in lien_maladie[0])

                if "maladies" in lien_maladie[0] and condition:
                    liste_maladies.append(lien_maladie[0].split('/')[-2])
                    nom = lien_maladie[0].split('/')[-2]
                    if not maladie_existe(onto, nom):
                        inst_maladie = list(onto.classes())[i]()
                        inst_maladie.iri = myOntology + nom
            i += 1
    # Output vers le fichier .owl
    # onto.save('ontology_patients.owl', format='ntriples')
    return onto
