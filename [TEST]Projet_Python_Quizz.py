# Créé par Idjellidaine Wassim, le 17/12/2024 en Python 3.7

#===============================================================================
#*******************************************************************************
#******************************* PROJET QUIZZ **********************************
#*******************************************************************************
#===============================================================================

#******************************* Les Fonctions *********************************

#La fonction menu identification :

def identification_menu():
    print("veuillez-vous identifier")
    print("1 --> s'identifier")
    print("2 --> créer un mot de passe et identifiant")
    choix=input("Choisissez une option parmis celles proposées")
    if choix == "1":
        identification()
    elif choix == "2":
        creation()
    else :
        print("La valeur entrée est incorrecte")
        identification_menu()



#fonction d'identification : l'utilisateur entre son mdp et id pour s'identifier

'''
Il permet également de vérifier si les identifiants et mots de passes entrés
sont bien existants pour donner l'accès ou non à l'utilisateur.
'''

def identification():
    written_id=input("entrez votre identifiant")
    with open('identifiants.txt','r') as f:
        dico = {}
        for ligne in f:
            ligne = ligne.replace("\n","")
            ligne = ligne.split(";;")
            dico[ligne[0]] = ligne[-1]
        if written_id in dico:
            written_password=input("entrez votre mot de passe")
            print(f"Authentification réussie.\n Bienvenue {written_id} !")
            return written_id
        else:
            print("Erreur. Veuillez Ressayer.")


#fonction de création d'identifiant et mot de passe:

'''
Cette fonction permet de créer un identifiant et un mot de passe, elle va vérifier
si les identifiants et mot de passe que l'utilisateur veut créer existent déjà
dans le fichier CSV avant de les créer. S'il existent déjà, elle ne va pas
les créer et va re-demander l'utilisateur de re-écrire en input de nouvelles
informations.
'''

def creation():

    created_id = input("Entrez un identifiant à créer : ")
    created_password = input("Entrez un mot de passe à créer : ")

    # Lire les identifiants existants depuis le fichier
    with open('identifiants.txt', 'r') as f:
        identifiants_existants = [ligne.strip().split(";;")[0] for ligne in f]
        mots_de_passe_existants = [ligne.strip().split(";;")[1] for ligne in f]

    # Vérifier si l'identifiant ou le mot de passe existe déjà
    if created_id in identifiants_existants:
        print("L'identifiant existe déjà. Veuillez en choisir un autre.")
        return creation()
    elif created_password in mots_de_passe_existants:
        print("Le mot de passe existe déjà. Veuillez en choisir un autre.")
        return creation() # Retourne sans écrire dans le fichier

    # Ajouter l'identifiant et le mot de passe si ils n'existent pas
    with open('identifiants.txt', 'a') as f:
        f.write(f"{created_id};;{created_password}\n")
    print("Identifiant et mot de passe créés avec succès !")


#La fonction menu : sélection des options.

def menu():
    print("Que voulez vous faire ?")
    print("1 --> Lancer le Quiz")
    print("2 --> Se déconnecter")
    reponse=input("choisissez une des deux options.")
    if reponse == "1":
        print("votre choix :")
        print("Vous avez choisi de lancer le Quiz")
        menu_selection_de_jeu()
    elif reponse == "2":
        print("votre choix")
        print("vous avez choisi de vous déconnecter")
        identification()
    else :
        print("La valeur choisie est incorrecte, veuillez réessayer")
        menu()


#La fonction du menue de sélection du Quizz:


def menu_selection_de_jeu():
    print("                                                                   ")
    print("                     BIENVENUE DANS LE QUIZ                        ")
    print("                                                                   ")
    print("        Vous avez différentes options ci-dessous veuillez          ")
    print("             Choisir ce que vous souhaiez faire.                   ")
    print("               Voici les différentes options :                     ")
    print("                                                                   ")
    print("1--> choisir un thème")
    print("2 --> afficher les scores")
    print("3--> retour en arrière")
    choix = input("Faîte votre choix.")
    if choix=="1":
        themes()
    elif choix =="2":
        affichage_des_scores(written_id,score_Hist_Geo,score_sciences_generales)
    elif choix =="3":
        menu()



#Fonction theme : Liste de tous les thèmes mis à disposition du joueur.

def themes():
    print("Vous voilà dans la sélection de thèmes, vous avez l'embarras du choix")
    print("                 1--> Histoire et géographie                       ")
    print("                 2--> Sciences générale                            ")
    print("                 3--> Films et séries                              ")
    print("                 4--> Musiques                                     ")
    print("                 5--> Jeux vidéos                                  ")
    print("")
    print("                 6--> revenir en arrière                           ")
    selection=input("Sélectionnez votre thèmes")
    if selection == "1":
        print("Vous avez choisi le Quiz sur l'Histoire et la Géographie.")
        quiz_histoire_geo(written_id)
    elif selection == "2":
        ("Vous avez choisi le Quiz sur Les siences générales.")
        quiz_sciences_generales(written_id)
    elif selection =="3":
        ("Vous avez choisi le Quiz sur les films et séries.")
        quiz_films_series(written_id)
    elif selection =="4":
        print("Vous avez choisie le Quiz sur les musiques.")
        #quiz_musique

    elif selection =='6':
        print("Vous avez choisie de revenir en arrière.")
        menu_selection_de_jeu()



#fonction enregistrement des scores

def enregistrement_score(written_id, score_Hist_Geo,score_sciences_generales,score_films_series):
    with open('scores.txt', 'a') as fichier:
        fichier.write(f"{written_id};{score_Hist_Geo};{score_sciences_generales};{score_films_series}\n")


#Fonction d'affichage des scores :

def affichage_des_scores(written_id,score_Hist_Geo,score_sciences_generales,score_films_series):
    print("==============================================================")
    print(f"[{written_id} :                                             ]")
    print(f"[Score du Quiz Histoire et géographie: {score_Hist_Geo}     ]")
    print(f"[Score du Quiz science générales: {score_sciences_generales}]")
    print(f"[Score du Quiz film et série: {score_films_series}          ]")
    print("==============================================================")





# Fonction du Quizz Histoire Géographie :

def quiz_histoire_geo(written_id):
    score_Hist_Geo = 0
    print("-------------------------------------------------------------------")
    print("Comment se prénomme l'homme qui a élevé Louis XIV ?")
    print("-------------------------------------------------------------------")
    print("1--> Le cardinal Mazarin.")
    print("2--> Louis XVIII, son père.")
    print("3--> Vauban.")
    print("4--> Jean-Baptiste Colbert")
    rep = input("Entrez votre choix.")
    if rep == "1":
        print("Bravo, c'est la bonne réponse !")
        score_Hist_Geo += 1
    else :
        print("Faux. La bonne réponse était Le cardinal Mazarin.")

    print("-------------------------------------------------------------------")
    print("En quelle année fut assasiné Jules Cesar ?")
    print("-------------------------------------------------------------------")
    print("1--> en 67 avant J.C")
    print("2--> en 45 avant J.C")
    print("3--> en 44 avant J.C")
    print("4--> en 50 avant J.C")
    rep = input("Entrez votre choix.")
    if rep == "3":
        print("Bravo, c'est la bonne réponse !")
        score_Hist_Geo += 1
    else :
        print("Faux. La bonne réponse était en 44 avant J.C.")

    print("-------------------------------------------------------------------")
    print("Quel est le seul pays sud américain avec Paraguay \n à ne pas avoir accès à la mer ?")
    print("-------------------------------------------------------------------")
    print("1--> Uruguay")
    print("2--> Bolivie")
    print("3--> Surinam")
    print("4--> Argentine")
    rep = input("Entrez votre choix.")
    if rep == "2":
        print("Bravo, c'est la bonne réponse !")
        score_Hist_Geo += 1
    else :
        print("Faux. La bonne réponse était la Bolivie.")

    print("-------------------------------------------------------------------")
    print(" Quelle est la capitale de l'Azerbaïdjan")
    print("-------------------------------------------------------------------")
    print("1--> Gandja")
    print("2--> Quba")
    print("3--> Ucar")
    print("4--> Bakou")
    rep = input("Entrez votre choix.")
    if rep == "4":
        print("Bravo, c'est la bonne réponse !")
        score_Hist_Geo += 1
    else :
        print("Faux. La bonne réponse était Bakou.")

    print("-------------------------------------------------------------------")
    print(" Quand a été mit en place le système de monarchie parlementaire \n en angleterrre ?")
    print("-------------------------------------------------------------------")
    print("1--> XVII siècle.")
    print("2--> XV siècle.")
    print("3--> XVI siècle.")
    print("4--> XIV siècle.")
    rep = input("Entrez votre choix.")
    if rep == "1":
        print("Bravo, c'est la bonne réponse !")
        score_Hist_Geo = score_Hist_Geo + 1
    else :
        print("Faux. La bonne réponse était au XVII siècle.")

    print("-------------------------------------------------------------------")
    print(" Quel édit a permi aux protestants d'appliquer leur religion ?")
    print("-------------------------------------------------------------------")
    print("1--> L'édit d'Écouen.")
    print("2--> L'édit de Nantes.")
    print("3--> L'édit de Compiègne.")
    print("4--> L'édit de Milan.")
    rep = input("Entrez votre choix.")
    if rep == "2":
        print("Bravo, c'est la bonne réponse !")
        score_Hist_Geo += 1
    else :
        print("Faux. La bonne réponse était l'édit de Nantes.")
    print("-------------------------------------------------------------------")
    print("Quelle est la plus grande île du monde ?")
    print("-------------------------------------------------------------------")
    print("1--> Groenland")
    print("2--> Madagascar")
    print("3--> Borneo")
    print("4--> Nouvelle-Guinée")
    rep = input("Entrez votre choix.")
    if rep == "1":
        print("Bravo, c'est la bonne réponse !")
        score_Hist_Geo += 1
    else:
        print("Faux. La bonne réponse était le Groenland.")

    print("-------------------------------------------------------------------")
    print("Quel événement a marqué la fin de la Seconde Guerre mondiale ?")
    print("-------------------------------------------------------------------")
    print("1--> La libération de Paris")
    print("2--> La chute de Berlin")
    print("3--> La capitulation du Japon")
    print("4--> Le débarquement en Normandie")
    rep = input("Entrez votre choix.")
    if rep == "3":
        print("Bravo, c'est la bonne réponse !")
        score_Hist_Geo += 1
    else:
        print("Faux. La bonne réponse était la capitulation du Japon.")

    print("-------------------------------------------------------------------")
    print("Quel est le fleuve le plus long du monde ?")
    print("-------------------------------------------------------------------")
    print("1--> Le Nil")
    print("2--> L'Amazone")
    print("3--> Le Yangtsé")
    print("4--> Le Mississippi")
    rep = input("Entrez votre choix.")
    if rep == "2":
        print("Bravo, c'est la bonne réponse !")
        score_Hist_Geo += 1
    else:
        print("Faux. La bonne réponse était l'Amazone.")

    print("-------------------------------------------------------------------")
    print("Qui était le premier président des États-Unis ?")
    print("-------------------------------------------------------------------")
    print("1--> Abraham Lincoln")
    print("2--> Thomas Jefferson")
    print("3--> George Washington")
    print("4--> John Adams")
    rep = input("Entrez votre choix.")
    if rep == "3":
        print("Bravo, c'est la bonne réponse !")
        score_Hist_Geo += 1
    else:
        print("Faux. La bonne réponse était George Washington.")

    print("Vous avez fini le quiz sur l'histoire géographie")
    print(f"votre score est de : {score_Hist_Geo}")
    enregistrement_score(written_id, score_Hist_Geo,0,0)
    themes()
    return score_Hist_Geo


# Fonction du Quiz sicence générale :


def quiz_sciences_generales(written_id):

    score_sciences_generales = 0
    print("--------------------------------------------------------------------")
    print("Comment appele t-on le phénomène de passage de la matière \n de l'état solide à gazeux ?")
    print("-------------------------------------------------------------------")
    print("1--> La fusion.")
    print("2--> La condensation.")
    print("3--> La ionisation.")
    print("4--> La sublimation")
    rep = input("Entrez votre choix.")
    if rep == "4":
        print("Bravo, c'est la bonne réponse !")
        score_sciences_generales += 1
    else :
        print("Faux. La bonne réponse était La sublimation.")

    print("-------------------------------------------------------------------")
    print("Quel a été le premier trou noir photographié ?")
    print("-------------------------------------------------------------------")
    print("1--> Sagittarius A*")
    print("2--> TON 618")
    print("3--> M87*")
    print("4--> M49*")
    rep = input("Entrez votre choix.")
    if rep == "3":
        print("Bravo, c'est la bonne réponse !")
        score_sciences_generales += 1
    else :
        print("Faux. La bonne réponse était M87*.")

    print("-------------------------------------------------------------------")
    print("À quelle famille appartenait le Tyrannotitan ?")
    print("-------------------------------------------------------------------")
    print("1--> À la famille des carcharodontosauridés")
    print("2--> À la famille des Tyrannosauridés")
    print("3--> À la famille des dromeosauridés")
    print("4--> À la famille des sauropodes")
    rep = input("Entrez votre choix.")
    if rep == "1":
        print("Bravo, c'est la bonne réponse !")
        score_sciences_generales += 1
    else :
        print("Faux. La bonne réponse était qu'il appartenait à la famille \n des carcharodontosauridés.")

    print("-------------------------------------------------------------------")
    print(" Sous quel nom connait-on mieux l’acide L-ascorbique ?")
    print("-------------------------------------------------------------------")
    print("1--> La vitamine C")
    print("2--> l'ADN")
    print("3--> l'Aspirine")
    print("4--> la bile")
    rep = input("Entrez votre choix.")
    if rep == "1":
        print("Bravo, c'est la bonne réponse !")
        score_sciences_generales += 1
    else :
        print("Faux. La bonne réponse était la vitamine C.")

    print("-------------------------------------------------------------------")
    print("Comment appellee-t-on la science de l'étude des foules ?")
    print("-------------------------------------------------------------------")
    print("1--> La foulologie.")
    print("2--> La fouloscopie.")
    print("3--> La foulothérapie.")
    print("4--> La foulométrie.")
    rep = input("Entrez votre choix.")
    if rep == "2":
        print("Bravo, c'est la bonne réponse !")
        score_sciences_generales += 1
    else :
        print("Faux. La bonne réponse était la fouloscopie.")

    print("-------------------------------------------------------------------")
    print(" Par quel terme désigne-t-on généralement \n les sciences sociales (sociologie, psychologie…) en opposition aux sciences « exactes » \n comme la physique ou la chimie ?")
    print("-------------------------------------------------------------------")
    print("1--> Les pseudo-sciences.")
    print("2--> Les sciences imparfaites.")
    print("3--> Les sciences alternatives.")
    print("4--> Les sciences molles.")
    rep = input("Entrez votre choix.")
    if rep == "4":
        print("Bravo, c'est la bonne réponse !")
        score_sciences_generales += 1
    else :
        print("Faux. La bonne réponse était les sciences molles.")
    print("-------------------------------------------------------------------")
    print("Quel scientifique prête son nom à l’effet correspondant à \n « un décalage de fréquence d’une onde observée entre l'émission et à la réception à cause du mouvement » ?")
    print("-------------------------------------------------------------------")
    print("1--> Issac Newton.")
    print("2--> Christian Doppler.")
    print("3--> James Prescot Joules.")
    print("4--> Johanes Kepler.")
    rep = input("Entrez votre choix.")
    if rep == "2":
        print("Bravo, c'est la bonne réponse !")
        score_sciences_generales += 1
    else:
        print("Faux. La bonne réponse était Christian Doppler, \n en référence à l'effet Doppler.")

    print("-------------------------------------------------------------------")
    print("Qu'est-ce qu'un quantum d'énergie ?")
    print("-------------------------------------------------------------------")
    print("1--> Une fonction discontinue de l'énergie.")
    print("2--> La plus grande quantité indivisible d'énergie que l'on peut définir.")
    print("3--> La plus petite quantité indivisible d'énergie que l'on peut définir.")
    print("4--> Une fonction continue de l'énergie.")
    rep = input("Entrez votre choix.")
    if rep == "3":
        print("Bravo, c'est la bonne réponse !")
        score_sciences_generales += 1
    else:
        print("Faux. La bonne réponse était La plus petite quantité \n indivisible d'énergie que l'on peut définir.")

    print("-------------------------------------------------------------------")
    print("Quel technique physio-chimique permet de séparer différentes \n substences d'un mélange ?")
    print("-------------------------------------------------------------------")
    print("1--> L'nalyse radiochimie")
    print("2--> Le titrage")
    print("3--> La chromatographie")
    print("4--> L'analyse gravimétrique")
    rep = input("Entrez votre choix.")
    if rep == "3":
        print("Bravo, c'est la bonne réponse !")
        score_sciences_generales += 1
    else:
        print("Faux. La bonne réponse était la chromatographie.")

    print("-------------------------------------------------------------------")
    print("Quel principe consiste en l'adhésion de molécules ou d'atomes \n d'un gaz ou d'un liquide à la surface d'un solide, formant une fine couche de substance ?")
    print("-------------------------------------------------------------------")
    print("1--> La désorption.")
    print("2--> L'absorption.")
    print("3--> La résorption")
    print("4--> L'adsorption.")
    rep = input("Entrez votre choix.")
    if rep == "4":
        print("Bravo, c'est la bonne réponse !")
        score_sciences_generales += 1
    else:
        print("Faux. La bonne réponse était l'adsorption.")

    print("Vous avez fini le quiz sur les sciences générales")
    print(f"votre score est de : {score_sciences_generales}")
    enregistrement_score(written_id,0,score_sciences_generales,0)
    themes()
    return score_sciences_generales


#fonction du Quiz films et séries :


def quiz_films_series(written_id):
    score_films_series = 0
    print("--------------------------------------------------------------------")
    print("Dans la saga, Luke Skywalker et la princesse Leia sont :")
    print("-------------------------------------------------------------------")
    print("1--> En couple.")
    print("2--> Frère et soeur.")
    print("3--> Amis.")
    print("4--> Père et fille.")
    rep = input("Entrez votre choix.")
    if rep == "2":
        print("Bravo, c'est la bonne réponse !")
        score_films_series += 1
    else :
        print("Faux. La bonne réponse était frère et soeur..")

    print("-------------------------------------------------------------------")
    print("Dans le film Retour vers le futur 2, Comment s'appelle \n l'empire pétrolier créé par Biff ?")
    print("-------------------------------------------------------------------")
    print("1--> Texaco.")
    print("2--> Tannenco.")
    print("3--> Biffco.*")
    print("4--> Biffico*")
    rep = input("Entrez votre choix.")
    if rep == "3":
        print("Bravo, c'est la bonne réponse !")
        score_films_series += 1
    else :
        print("Faux. La bonne réponse était Biffco*.")

    print("-------------------------------------------------------------------")
    print("Dans le premoer Termonator, qui est Sarah ?")
    print("-------------------------------------------------------------------")
    print("1--> La sœur de John Connors")
    print("2--> La mère de Kyle Reese")
    print("3--> La mère de John Connor")
    print("4--> Une présentatrice télé.")
    rep = input("Entrez votre choix.")
    if rep == "3":
        print("Bravo, c'est la bonne réponse !")
        score_films_series += 1
    else :
        print("Faux. La bonne réponse était qu'il appartenait qu'elle était \n la  mère de John Connor")

    print("-------------------------------------------------------------------")
    print(" Dans le Bon, la Brute, et le Truan qui dit à Tuco dans \n quel cimetière sont cachés les 200 000 $ ?")
    print("-------------------------------------------------------------------")
    print("1--> Sentenza")
    print("2--> Thomas Larson")
    print("3--> Blondin")
    print("4--> Bill Carson")
    rep = input("Entrez votre choix.")
    if rep == "4":
        print("Bravo, c'est la bonne réponse !")
        score_films_series += 1
    else :
        print("Faux. La bonne réponse était Bill Carson.")

    print("-------------------------------------------------------------------")
    print("Dans le film Jurassic Parc, quel est le métier de Ian Malcolm ?")
    print("-------------------------------------------------------------------")
    print("1--> Mathématicien.")
    print("2--> Paléontologue.")
    print("3--> Archéologue.")
    print("4--> Physicien.")
    rep = input("Entrez votre choix.")
    if rep == "1":
        print("Bravo, c'est la bonne réponse !")
        score_films_series += 1
    else :
        print("Faux. La bonne réponse était qu'il était mathématicien.")

    print("-------------------------------------------------------------------")
    print("Dans la série The Mandalorian, de quel minerai légendaire \n est composé l'armure de Mando dans l'épisode 3 de la saison 1 ?")
    print("-------------------------------------------------------------------")
    print("1--> Zinc.")
    print("2--> Fer Sarrasien.")
    print("3-->  Beskar.")
    print("4--> Argent.")
    rep = input("Entrez votre choix.")
    if rep == "3":
        print("Bravo, c'est la bonne réponse !")
        score_films_series += 1
    else :
        print("Faux. La bonne réponse était en Beskar.")
    print("-------------------------------------------------------------------")
    print("Dans la série Breaking Bad, qui a tué Mike ?")
    print("-------------------------------------------------------------------")
    print("1--> Walter.")
    print("2--> Jesse.")
    print("3--> Marie.")
    print("4--> Gustavo Fring.")
    rep = input("Entrez votre choix.")
    if rep == "1":
        print("Bravo, c'est la bonne réponse !")
        score_films_series += 1
    else:
        print("Faux. La bonne réponse était bien Walter White.")

    print("-------------------------------------------------------------------")
    print("Quel événement a marqué la fin de la Seconde Guerre mondiale ?")
    print("-------------------------------------------------------------------")
    print("1--> La libération de Paris")
    print("2--> La chute de Berlin")
    print("3--> La capitulation du Japon")
    print("4--> Le débarquement en Normandie")
    rep = input("Entrez votre choix.")
    if rep == "3":
        print("Bravo, c'est la bonne réponse !")
        score_films_series += 1
    else:
        print("Faux. La bonne réponse était la capitulation du Japon.")

    print("-------------------------------------------------------------------")
    print("Quel technique physio-chimique permet de séparer différentes \n substences d'un mélange ?")
    print("-------------------------------------------------------------------")
    print("1--> L'nalyse radiochimie")
    print("2--> Le titrage")
    print("3--> La chromatographie")
    print("4--> L'analyse gravimétrique")
    rep = input("Entrez votre choix.")
    if rep == "3":
        print("Bravo, c'est la bonne réponse !")
        score_films_series += 1
    else:
        print("Faux. La bonne réponse était la chromatographie.")

    print("-------------------------------------------------------------------")
    print(" Dans la série Narcos, quel est le nom du cartel de la saison 3 ?")
    print("-------------------------------------------------------------------")
    print("1--> Le cartel de Cali.")
    print("2--> Le cartel Berlin.")
    print("3--> Le cartel de Bogota.")
    print("4--> Le cartel de Medellin.")
    rep = input("Entrez votre choix.")
    if rep == "1":
        print("Bravo, c'est la bonne réponse !")
        score_films_series += 1
    else:
        print("Faux. La bonne réponse était le cartel de Cali.")

    print("Vous avez fini le quiz sur les films et séries")
    print(f"votre score est de : {score_films_series}")
    enregistrement_score(written_id,0,0,score_films_series)
    themes()
    return score_films_series


#**************************** Appel de fonction ********************************
written_id = identification()  # On récupère l'identifiant de l'utilisateur
menu()
