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
        fichier_lecture()
    elif choix == "2":
        creation()
    else :
        print("La valeur entrée est incorrecte")
        identification_menu()



#fonction d'identification : l'utilisateur entre son mdp et id pour s'identifier


def identification():
    written_id=input("entrez votre identifiant")
    fichier_lecture()
    written_password=input("entrez votre mot de passe")
    fichier_lecture()


#fonction de création d'identifiant et mot de passe:

def creation():
    name=input('Entrez un identifiant à créer')
    mdp=input('entrer un mot de passe à créer')
    with open('identifiants.txt','a') as f:
        f.write('id')
        f.write(';;')
        f.write(mdp)
        f.write('\n')


#créer un fichier lecture : vérifie si les mots de passe et un mot de passe existe ou pas.


def fichier_lecture():

    with open('identifiants.txt','r') as f:
        dico = {}
        for ligne in f:
            ligne = ligne.replace("\n","")
            ligne = ligne.split(";;")
            dico[ligne[0]] = ligne[-1]
        if id not in dico:
            print("Identifiant incorrect, réessayez.")
            identification()
        elif dico[id]==mdp:
            print("Vous avez réussi à vous identifier.")
            print("Bienvenue {id}")
        else:
            print("mot de passe incorrecte")
            identification()


        #print(dico)
        return dico





#La fonction menu : sélection des options.

def menu():
    print("Que voulez vous faire ?")
    print("1 --> Afficher l'aide")
    print("2 --> Lancer le Quizz")
    print("3 --> Quitter le programme")
    reponse=input("choisissez un nombre entre 1 et 3") #demander que faire et choisir un nombre
    if reponse == "1": #sélection de l'aide
        print("votre choix :")
        print("Vous avez choisi aide")
        aide()
    elif reponse == "2": #sélection du jeu
        print("votre choix :")
        print("vous avez choisi partie")
        partie()
    elif reponse == "3": #sélection de l'option se déconnecter
        print("votre choix")
        print("vous avez choisi de vous déconnecter")
        identification()

    else :
        print("La valeur choisie est incorrecte, veuillez réessayer")
        menu()

#La fonction du menue de sélection du Quizz:

'''
La fonction partie correspond au Quizz en lui même. Après avoir choisi l'option
jeu, c'est ici que l'utilisateur est redirigé. En effet, cette fonction va non
seulement indiquer si la réponse entrée à chaque question est juste ou fausse
mais va aussi compter le score et le donner enfin de partie.
'''


def menu_selection_de_jeu():
    print("                                                                   ")
    print("                     BIENVENUE DANS LE QUIZZ                       ")
    print("                                                                   ")
    print("        Vous avez différentes options ci-dessous veuillez          ")
    print("             Choisir ce que vous souhaiez faire.                   ")
    print("               Voici les différentes options :                     ")
    print("                                                                   ")
    print("1--> choisir un thème")
    print("2--> retour en arrière")
    choix_utilisateur = input("Faîte votre choix.")
    if choix=="1":
        themes()


#Fonction theme : Liste de tous les thèmes mis à disposition du joueur.

def themes():
    print("Vous voilà dans la sélection de thèmes, vous avez l'embarras du choix")
    print("                 1--> Histoire et géographie                       ")
    print("                 2--> Sciences générale                            ")
    print("                 3--> Films et séries                              ")
    print("                 4--> Musiques                                     ")
    print("                 5--> Jeux vidéos                                  ")
    selection=input("Sélectionnez votre thèmes")
    if selection == "1":
        print("Vous avez choisi le Quizz sur l'Histoire et la Géographie")
        quizz_histoire_geo()
    elif selection == "2":
        ("Vous avez choisi le Quizz sur Les siences générale")
        quizz_science_generale()
    elif selection =="3":
        ("Vous avez choisi le Quizz sur les films et séries")
        quizz_films_&_series()
    elif selection =="4":
        print("Vous avez choisie le Quizz sur les musiques")






# Fonction du Quizz Histoire Géographie :
'''
def quizz_histoire_geo():
'''
# Fonction du Quizz sicence générale :

'''
def quizz_science_generale():
'''

#fonction du Quizz films et séries :

'''
quizz_films_&_series()
'''

#**************************** Appel de fonction ********************************
identification_menu()
menu()
