def calculatrice(x, y, operateur):
    if operateur == "+":
        return x + y
    elif operateur == "-":
        return x - y
    elif operateur == "*":
        return x * y
    elif operateur == "/":
        if y == 0:
            return "Division par 0 impossible"
        else:
            return x / y
    elif operateur == "//":
        if y == 0:
            return "Division par 0 impossible"
        else:
            return x // y
    elif operateur == "%":
        if y == 0:
            return "Division par 0 impossible"
        else:
            return x % y
    elif operateur == "**":
        return x ** y
    else:
        return "Opérateur invalide (opérateurs valides: +, -, *, /, //, %, **)"

memoire = []

while True:
    x = float(input("Entrez un nombre x: "))
    operateur = input("Entrez un opérateur (+, -, *, /, //, %, **):")
    y = float(input("Entrez un nombre y: "))

    resultat = calculatrice(x, y, operateur)
    cal = f"{x} {operateur} {y} = {resultat}"
    print("calcul:", cal)

    affichage = input("Voulez-vous archiver votre calcul? (oui/non/eff): ")

    if affichage == "oui":
        memoire.append(cal)
        print("Résultat archivé.")
    elif affichage == "non":
        pass
    elif affichage == "eff":
        memoire.clear()
        print("Mémoire effacée.")
    else:
        print("Veuillez entrer oui/non/eff.")

    continuer = input("Voulez-vous continuer? (oui/non): ")
    if continuer != "oui":
        print("Bonne journée")
        break

print("Archives calculs", memoire)

