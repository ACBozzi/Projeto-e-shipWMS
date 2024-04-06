# app/controllers/livro_controller.py
from app.models.livro import Livro

livros = []

def adicionar_livro(dados):
    livro = Livro(dados['Nome do livro'], dados['data de Lançamento'], dados['ISBN'], dados['Autor'])
    livros.append(livro)

def buscar_livro(nome):
    resultado = [livro.__dict__ for livro in livros if nome.lower() in livro.nome.lower()]
    return resultado