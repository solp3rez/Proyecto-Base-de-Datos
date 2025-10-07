from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # permite que React haga peticiones desde otro puerto

# Lista de apuntes en memoria
apuntes = []

@app.route('/')
def home():
    return jsonify({'mensaje': 'Backend conectado correctamente 🚀'})

@app.route('/apuntes', methods=['GET', 'POST'])
def ruta_apuntes():
    if request.method == 'GET':
        return jsonify(apuntes)
    if request.method == 'POST':
        data = request.get_json()
        titulo = data.get('titulo')
        contenido = data.get('contenido')
        if titulo and contenido:
            apuntes.append({'titulo': titulo, 'contenido': contenido})
            return jsonify({'mensaje': 'Apunte agregado correctamente ✅'})
        return jsonify({'error': 'Faltan datos'}), 400

if __name__ == '__main__':
    app.run(debug=True)
