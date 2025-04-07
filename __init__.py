from flask import Flask

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    pyramide = ''
    for i in range(1, valeur + 1):
    
        left_side = ''.join(str(x) for x in range(1, i + 1))
        
        right_side = ''.join(str(x) for x in range(i - 1, 0, -1))
       
        ligne = left_side + right_side
        
        pyramide += ' ' * (valeur - i) + ligne + '<br>'
    return pyramide  

if __name__ == "__main__":
    app.run(debug=True)

