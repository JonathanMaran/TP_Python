# TP ZCasino - Jeu de roulette
import random
import time

bankroll = 1000
game = True

print(" ")
print("Bonjour et bienvenue à la roulette du ZCasino !")
print(" ")

# Tant que le jeu est sur True, on peut jouer
while game:

    # pour pouvoir revenir au début du while
    numero = -1
    while numero < 0 or numero > 50:
        try:
            print("Veuillez choisir un numéro entre 0 et 50 avant de miser:")
            numero = input()
            numero = int(numero)
        except:
            print("Erreur de saisie !")
            print(" ")
            numero = -1
            continue

        if numero < 0:
            print("Il est impossible de choisir un nombre négatif.")
            print(" ")
            numero = -1
        elif numero > 50:
            print("Il est impossible de choisir un nombre supérieur à 50.")
            print(" ")
            numero = -1

    mise = 0
    while mise <= 0 or mise > bankroll:
        try:
            print(" ")
            print("Combien souhaitez-vous miser sur ce numéro {} ?".format(numero))
            mise = input()
            mise = int(mise)
        except:
            print("Erreur de saisie !")
            print(" ")
            mise = 0
            continue

        if mise <= 0:
            print("Il est impossible de miser moins de 1 euros.")
            print(" ")
            mise = 0
        elif mise > bankroll:
            print("Vous ne pouvez pas miser plus que votre bankroll ({} euros).".format(bankroll))
            print(" ")
            mise = 0

    print("Très bien, vous souhaitez donc miser : {} euros !".format(mise))

    print(" ")
    print("Les jeux sont faits, rien va plus...")
    time.sleep(1)
    print("*la bille tourne encore...*")
    time.sleep(1)
    print("*suspense...*")
    time.sleep(1)
    print(" ")

    # Le numéro sur lequel s'arrête la roulette
    roulette = random.randrange(50)
    print(f"La roulette vient de s'arrêter sur le numéro...{roulette} !")
    print(" ")

    if numero == roulette:
        calcul_gain = mise * 50
        print("WAHOU ! BRAVO ! Vous avez misé sur le bon numéro ! Vous empochez donc {} euros !".format(calcul_gain))
        bankroll += calcul_gain
        print("Votre Bankroll est maintenant de {} euros.".format(bankroll))
    elif numero % 2 == roulette % 2:  # savoir si les deux numéros sont paires
        print("Bien, vous n'avez pas trouvé le bon numéro MAIS vous avez la bonne couleur !")
        calcul_gain = mise
        bankroll += calcul_gain
        print("Vous empochez donc {} euros et votre bankroll s'élève maintenant à {} euros !".format(calcul_gain,
                                                                                                     bankroll))
    else:
        print(
            "Dommage, vous n'avez pas trouvé le bon numéro et la roulette ne s'est pas arrêtée sur la même couleur que vous !")
        bankroll -= mise
        print("Vous perdez donc votre mise de {} euros et votre bankroll est maintenant de {} euros.".format(mise,
                                                                                                             bankroll))

    if bankroll == 0:
        game = False
        print(" ")
        print("Vous n'avez plus d'argent...")
    else:
        print("-----------------------")
        reponse_jeu = "x"
        while reponse_jeu != "oui" and reponse_jeu != "non":
            print("Souhaitez-vous continuer à jouer ? oui / non")
            print(" ")
            reponse_jeu = input()
            reponse_jeu = str(reponse_jeu)

        if reponse_jeu == "oui":
            print("Super ! alors continuons !")
            print(" ")
        else:
            print(" ")
            print("Vous repartez avec une somme de {} euros !".format(bankroll))
            game = False

print(" ")
print("Le Casino Z vous remercie, à bientôt !")
