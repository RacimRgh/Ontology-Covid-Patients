# importer les autres fichiers py
import onto_traitement as ot
import onto_maladie as om
import onto_localisation as ol
import onto_patient as op
import ajoute_patients as ap
import fiche_medecin as fm
# Owlready
from owlready2 import *  # pylint: disable=unused-wildcard-import


default_world.set_backend(filename="file_back3.sqlite3", exclusive=False)

onto = get_ontology('http://www.semanticweb.org/racim_katia/ontology_covid#')
myOntology = 'http://www.semanticweb.org/onto_covid#'


onto = om.create_maladies(onto, myOntology)
onto = ot.create_traitements(onto)
onto = ol.create_localisation(onto, myOntology)
onto = op.create_patient(onto)
onto = ap.instancier_patients(onto)
onto = fm.creation_fiche_medecin(onto)

# Output vers le fichier .owl
onto.save(file='ontology_patients.owl', format='ntriples')
