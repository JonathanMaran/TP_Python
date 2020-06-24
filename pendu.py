# Le jeu du pendu
import time
from random import choice
import string
from donnees import nb_chances_autorisées, liste_mots
from fonctions import *

continuer_partie = "oui"

while continuer_partie == "oui":
    print(" ")
    print("--- Nouvelle partie ---")
    print(" ")
    mot_mystere = choisir_mot().upper()
    lettres_trouvees = []
    mot_trouve = recup_mot_masque(mot_mystere, lettres_trouvees)
    print(f"Voici le mot à trouver : {mot_trouve}")

    while mot_mystere != mot_trouve and nb_chances_autorisées > 0:

        lettre = recup_lettre().upper()
        if lettre in lettres_trouvees:
            print("Vous avez déjà trouvé cette lettre !")
            print(" ")
        elif lettre in mot_mystere:
            lettres_trouvees.append(lettre)
            print("Bien joué !")
            print(" ")
        else:
            nb_chances_autorisées -= 1
            print("Aie... cette lettre ne se trouve pas le mot !")
            print(" ")

        mot_trouve = recup_mot_masque(mot_mystere, lettres_trouvees)
        print(f"Voici le mot à trouver : {mot_trouve}")

    if mot_trouve == mot_mystere:
        print(" ")
        print("BRAVO ! C'est gagné !")
    else:
        print(" ")
        print("PENDU ! Vous avez perdu...")

    print(" ")

    continuer_partie = input("Souahitez-vous faire une nouvelle partie ? oui / non").lower()
    while continuer_partie != "oui" and continuer_partie != "non":
        continuer_partie = input("Veuillez choisir si 'oui' ou 'non' vous souhaitez jouer une autre partie").lower()
    nb_chances_autorisées = 8

print(" ")
print("Merci d'avoir joué, à bientôt !")














