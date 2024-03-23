from flask import Flask, jsonify, request
from flasgger import Swagger
app = Flask(__name__)
Swagger(app)
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
    """
    Incluir um novo usuário.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            cpf:
              type: integer
              description: CPF do usuário
            nome:
              type: string
              description: Nome do usuário
            datanascimento:
              type: string
              format: date
              description: Data de nascimento do usuário (YYYY-MM-DD)
    responses:
      201:
        description: Usuário criado
    """
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)
    return jsonify(usuarios), 201

@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    """
    Obter lista de usuários.
    ---
    responses:
      200:
        description: Lista de usuários
    """
    return jsonify(usuarios), 200

if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)
