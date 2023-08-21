from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {
        'cpf': 11111111111,
        'nome': 'Felipe',
        'datanascimento': '2023-08-20'
    },
    {
        'cpf': 22222222222,
        'nome': 'Maria',
        'datanascimento': '2023-08-20'
    },
    {
        'cpf': 33333333333,
        'nome': 'Pedro',
        'datanascimento': '2023-08-20'   
    }
]

@app.route('/usuarios', methods=['POST'])
def incluir_novo_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)
    return jsonify(usuarios), 201

@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    return jsonify(usuarios), 200

if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)