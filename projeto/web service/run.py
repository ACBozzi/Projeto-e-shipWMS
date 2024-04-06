# run.py
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
    try:
        dados = request.json
        for livro in dados["livros"]:
            adicionar_livro(livro)
        return 'Livros adicionados com sucesso'
    except Exception as e:
        return str(e), 400

@app.route('/buscar-livro', methods=['GET', 'POST'])
@auth.login_required
def buscar():
    if request.method == 'GET':
        dados = request.json
        resultado = buscar_livro(dados['Nome do livro'])
        return jsonify(resultado)
    else:
        return jsonify({'message': 'Endpoint para buscar livros. Use um método POST com o corpo da solicitação contendo o nome do livro.'})

if __name__ == '__main__':
    app.run(debug=True)
