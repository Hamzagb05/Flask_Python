from flask import Flask

app = Flask(__name__)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    # Convertir la chaîne de caractères en une liste d'entiers
    liste_nombres = valeurs.split('/')
    liste_nombres = [int(n) for n in liste_nombres]

    # Initialiser la valeur maximale et une liste pour les indices
    max_val = liste_nombres[0]
    max_indices = [0]

    # Parcourir la liste pour trouver les valeurs maximales et leurs indices
    for i in range(1, len(liste_nombres)):
        if liste_nombres[i] > max_val:
            max_val = liste_nombres[i]
            max_indices = [i]  # Réinitialiser la liste des indices
        elif liste_nombres[i] == max_val:
            max_indices.append(i)

    # Retourner le résultat avec la valeur maximale et tous ses indices
    indices_str = ', '.join(map(str, max_indices))  # Convertir les indices en chaîne
    return f"Le plus grand nombre est : {max_val}, à l'indice(s) : {indices_str}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')










