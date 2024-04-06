from app.models.livro import Livro
import json
import os

# Função para carregar livros do arquivo TXT
def carregar_livros_arquivo():
    # Verifica se o arquivo existe
    if os.path.exists('livros.txt'):
        try:
            with open('livros.txt', 'r') as arquivo:
                return [Livro(**livro) for livro in json.load(arquivo)]
        except json.decoder.JSONDecodeError:
            # Caso o arquivo esteja vazio ou não seja um JSON válido
            return []
    else:
        # Se o arquivo não existir, cria um arquivo vazio
        with open('livros.txt', 'w'):
            pass
        return []

# Função para salvar livros no arquivo TXT
def salvar_livros_arquivo(livros):
    with open('livros.txt', 'w') as arquivo:
        json.dump([livro.__dict__ for livro in livros], arquivo)

livros = carregar_livros_arquivo()

def adicionar_livro(dados):
    livro = Livro(dados['Nome do livro'], dados['data de Lançamento'], dados['ISBN'], dados['Autor'])
    livros.append(livro)
    salvar_livros_arquivo(livros)

def buscar_livro(nome):
    resultado = [livro.__dict__ for livro in livros if nome.lower() in livro.nome.lower()]
    return resultado

def listar_livros():
    return [livro.__dict__ for livro in livros]

def remover_livro(nome):
    livros = carregar_livros_arquivo()
    livros = [livro for livro in livros if livro.nome != nome]
    salvar_livros_arquivo(livros)
