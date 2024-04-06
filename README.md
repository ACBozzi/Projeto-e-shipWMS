# Web Service de Gerenciamento de Livros

## Funcionalidades

O Web Service oferece as seguintes funcionalidades:

1. Adicionar livro: Permite adicionar novos livros ao sistema.
2. Buscar livro: Permite buscar livros por seu nome.
3. Listar livros: Retorna uma lista com todos os livros cadastrados.
4. Remover livro: Remove um livro do sistema com base no seu nome.

## Premissas

* O Web Service utiliza a biblioteca Flask em Python para lidar com requisições HTTP.
- A autenticação é realizada utilizando HTTP Basic Authentication.
+ Os dados dos livros são persistidos em um arquivo TXT chamado livros.txt.

## Requisitos

* Python 3.x instalado.
- Flask e Flask-HTTPAuth instalados.
+ Postman


## Execução
* python run.py
- O Web Service estará disponível em http://127.0.0.1:5000.

## Endpoints
1. Adicionar Livro: POST /adicionar-livro
   - Exemplo de envio: 
 {
  "livros": [
    {
      "Nome do livro": "O Ladrão De Raios",
      "data de Lançamento": "28-06-2005",
      "ISBN": "9788598078878",
      "Autor": "Rick Riordan"
    }
  ]
}

2. Buscar Livro: POST /buscar-livro
   - Exemplo de envio: 
{
  "Nome do livro": "O Ladrão"
}

3. Listar Livros: GET /listar-livros
4. Remover Livro: DELETE /remover-livro/{nome}

## Autenticação 
* O acesso aos endpoints é protegido por autenticação HTTP Basic Authentication.
- As credenciais padrão são: Usuário: user, Senha: password

## Estrutura
* O projeto segue uma estrutura MVC (Model-View-Controller)

## Dados
* Os dados dos livros são armazenados em um arquivo TXT chamado livros.txt.
- A leitura e escrita dos dados são realizadas utilizando a biblioteca JSON para serialização e desserialização dos objetos.
