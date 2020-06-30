import rdflib
import requetes as rq
graph = rdflib.Graph()
graph.parse("ontology_patients.owl", format='turtle')
graph.serialize("ontology_patients_out.rdf", "turtle")

print("""
1 - Patients selon: maladies, traitements, symptomes, adresse, orientation ou medecin auscultant
2 - Patients suspecté de covid selon ses infos: (Ou non exlusif) Age, sexe, poids, taille, temperature
3 - Patients selon la wilaya
4 - Patients selon le type de maladie (Exemple type = neurologie)
5 - Patients selon le nom de maladie (Exemple nom = AVC)
6 - Patients selon les traitements pris
7 - Patient selon le medecin auscultant (Code)
8 - Patients selon la gravité des symptomes (faible, modérée, sévère)
9 - Patients et medecins selon la date de consultation (Date complète, ou jour/mois/année séparément)
10 - Nombre de patients suspectés de covid selon une date donnée
11 - Nombre de patients suspectés de covid détectés par chaque médecin
12 - Nombre de patients suspectés de covid dans une wilaya donnée
13 - Nombre de patients par: maladie, traitement, symptomes, orientation, ausculation
""")
choix = input('Votre choix? ')
if(choix == '1'):
    print('\n_______________________________')
    print('1:prend - 2:habite_a - 3:est_atteint_de - 4:présente - 5:ausculté_par - 6:orienté_vers')
    prop = input('Propriété: ')
    dic_choix = {
        '1': 'prend',
        '2': 'habite_a',
        '3': 'est_atteint_de',
        '4': 'présente',
        '5': 'ausculté_par',
        '6': 'orienté_vers',
    }
    rq.formater_resultat(rq.get_selon_obj_props(graph, dic_choix[prop]))

elif(choix == '2'):
    age = input('Age: ')
    poids = input('Poids: ')
    taille = input('Taille: ')
    temperature = input('Temperature: ')
    sexe = input('Sexe: \n______________')
    if sexe == '':
        sexe = '.'
    if age == '':
        age = 150
    if poids == '':
        poids = 0
    if taille == '':
        taille = 0
    if temperature == '':
        temperature = 35
    rq.print_resultat(rq.get_selon_data_prop(
        graph, age, sexe, poids, taille, temperature))

elif(choix == '3'):
    wilaya = input('Wilaya: ')
    if wilaya == '':
        wilaya = 'Alger'
    rq.print_resultat(rq.get_selon_wilaya(graph, wilaya))

elif(choix == '4'):
    type_maladie = input('Type maladie: ')
    if type_maladie == '':
        type_maladie = 'pneumologie'
    rq.print_resultat(rq.get_selon_type_maladie(graph, type_maladie))

elif(choix == '5'):
    maladie = input('Nom de la maladie: ')
    if maladie == '':
        maladie = 'pneumonie'
    rq.print_resultat(rq.get_selon_nom_maladie(graph, maladie))

elif(choix == '6'):
    medic = input('Nom du médicament: ')
    if medic == '':
        medic = 'paracétamol'
    rq.formater_resultat(rq.get_selon_traitement(graph, medic))

elif(choix == '7'):
    medecin = input('Nom du médecin: ')
    if medecin == '':
        medecin = 'Aissat_Abdelhak'
    rq.print_resultat(rq.get_selon_medecin(graph, medecin))

elif(choix == '8'):
    gravite = input('Gravité: ')
    if gravite == '':
        gravie = 'sévère'
    rq.print_resultat(rq.get_selon_gravité(graph, gravite))

elif(choix == '9'):
    date = input('Date: ')
    if date == '':
        date = '2020'
    rq.print_resultat(rq.get_selon_date_consultation(graph, date))

elif(choix == '10'):
    date = input('Date: ')
    if date == '':
        date = '2020'
    rq.print_resultat(rq.get_nombre_covid_date(graph, date))

elif(choix == '11'):
    rq.print_resultat(rq.get_nombre_covid_medecin(graph))

elif(choix == '12'):
    wilaya = input('Wilaya: ')
    if wilaya == '':
        wilaya = 'Alger'
    rq.print_resultat(rq.get_nombre_par_wilaya(graph, wilaya))

elif(choix == '13'):
    print('\n_______________________________')
    print('1:prend - 2:habite_a - 3:est_atteint_de - 4:présente - 5:ausculté_par - 6:orienté_vers')
    prop = input('Propriété: ')
    dic_choix = {
        '1': 'prend',
        '2': 'habite_a',
        '3': 'est_atteint_de',
        '4': 'présente',
        '5': 'ausculté_par',
        '6': 'orienté_vers',
    }
    valeur = input('Valeur: ')
    rq.print_resultat(rq.get_nombre_prop_valeur(
        graph, dic_choix[prop], valeur))
