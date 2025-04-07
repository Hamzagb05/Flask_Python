# Initialiser la somme et la valeur de n
somme = 0
n = 0  # On va l'incrémenter progressivement

# Boucle jusqu'à ce que la somme dépasse 5000
while True:
    n += 1  # On passe au nombre suivant

    # Si le nombre est divisible par 11, on le saute
    if n % 11 == 0:
        continue

    # Si le nombre est divisible par 5 ou 7, on l'ajoute à la somme
    if n % 5 == 0 or n % 7 == 0:
        somme += n

    # Si la somme dépasse 5000, on arrête
    if somme > 5000:
        # On annule le dernier ajout qui a fait dépasser la somme
        somme -= n
        n -= 1
        break

# Afficher le résultat
print("Dernier nombre utilisé :", n)
print("Somme finale :", somme)








