from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

from app.controllers.livro_controller import adicionar_livro, buscar_livro

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user": "password"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

@app.route('/', methods=['GET'])
def index():
    return 'Bem-vindo ao nosso Web Service'

@app.route('/adicionar-livro', methods=['POST'])
@auth.login_required
def adicionar():
    dados = request.json
    adicionar_livro(dados)
    return 'Livro adicionado com sucesso'

@app.route('/buscar-livro', methods=['POST'])
@auth.login_required
def buscar():
    dados = request.json
    resultado = buscar_livro(dados['Nome do livro'])
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
