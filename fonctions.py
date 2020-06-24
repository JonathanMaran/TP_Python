from random import choice

from donnees import liste_mots


def recup_lettre():
    """Cette fonction récupère une lettre saisie par
        l'utilisateur. Si la chaîne récupérée n'est pas une lettre,
        on appelle récursivement la fonction jusqu'à obtenir une lettre"""

    lettre = input("Choisissez une lettre: ")
    lettre = lettre.lower()
    if len(lettre) > 1 or not lettre.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return recup_lettre()
    else:
        return lettre


def choisir_mot():
    return choice(liste_mots)


def recup_mot_masque(mot_complet, lettres_trouvees):
    """Cette fonction renvoie un mot masqué tout ou en partie, en fonction :
      - du mot d'origine (type str)
      - des lettres déjà trouvées (type list)

      On renvoie le mot d'origine avec des * remplaçant les lettres que l'on
      n'a pas encore trouvées."""
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque
