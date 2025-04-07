from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def fibonacci(n):
    # Initialiser les deux premiers termes
    a, b = 2, 5
    suite = []

    # Générer la suite jusqu'au terme n
    for _ in range(n):
        suite.append(a)
        a, b = b, a + b  # Mise à jour des valeurs

    return ', '.join(map(str, suite))  # Retourner la suite sous forme de chaîne

if __name__ == "__main__":
    app.run(debug=True)



