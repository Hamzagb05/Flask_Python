from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def fibonacci(n):
    # Initialiser la variable avec le premier terme
    U = 0
    suite = []

    # Utiliser une seule variable pour générer la suite
    for i in range(n):
        if i == 0:
            suite.append(U)  # Ajouter le premier terme
        elif i == 1:
            U = 1  # Deuxième terme
            suite.append(U)
        else:
            # Calculer le terme suivant en utilisant la variable U
            U = suite[i - 1] + suite[i - 2]
            suite.append(U)

    return ', '.join(map(str, suite))  # Retourner la suite sous forme de chaîne

if __name__ == "__main__":
    app.run(debug=True)






