# Ontology-Covid-Patients

Creating an ontology using python's owlready2 and rdflib

## Requirements

Python3, pip, protege5.5.0
After downloading and installing Python3 and pip3, use this command to install the required libraries

- pip3 install beautifulsoup4 urllib pandas numpy rdflib owlready2

## How to use

To start it, type in the CMD:

**python3 creation_ontologie.py**

The file _ontology_patients.owl_ will be created and updated in the current working directory

## SPARQL queries

To use the SPARQL queries, go to "requetes.py"
Every query is documented and ready to use, along with some formatting functions

The file "menu_requetes.py" contains a menu that allows the user to choose the query he needs and executes it. He is also prompted to give optionnal parameters if necessary (Leave it blank to use the default parameters)
