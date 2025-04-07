# Demander à l'utilisateur de saisir un nombre
n = int(input("Entrez la valeur de n : "))

# Initialiser la somme à 0
somme = 0

# Parcourir les nombres de 1 à n
for i in range(1, n + 1):
    print(f"Nombre en cours : {i}")  # Affichage optionnel pour voir chaque nombre

    # Si le nombre est divisible par 11, on l'ignore
    if i % 11 == 0:
        print(f"{i} est divisible par 11, on le saute.")
        continue

    # Si le nombre est divisible par 5 ou 7, on l'ajoute à la somme
    if i % 5 == 0 or i % 7 == 0:
        somme += i
        print(f"{i} est ajouté à la somme. Nouvelle somme : {somme}")

    # Si la somme dépasse 5000, on arrête la boucle
    if somme > 5000:
        print("La somme a dépassé 5000. Arrêt du programme.")
        break

# Affichage final de la somme
print("Somme finale :", somme)









