"""
O nosso cliente solicitou uma tabela para armazenar os livros que são comercializados pela
empresa. A solicitação é somente para livros e não há a necessidade de realizar busca em
outras tabelas. Hoje há um funcionário de vendas que tem uma tabela do Excel para guardar
esses registros, mas as buscas estão ficando complexas. Decidiu-se então criar um banco de
dados separado para esse funcionário.
Após a criação da tabela, deveremos entregar algumas queries prontas para que sejam
enviadas para o programador. As queries são as seguintes:
1 – Trazer todos os dados.
2 – Trazer o nome do livro e o nome da editora
3 – Trazer o nome do livro e a UF dos livros publicados por autores do sexo masculino.
4 - Trazer o nome do livro e o número de páginas dos livros publicados por autores do sexo
feminino.
5 – Trazer os valores dos livros das editoras de São Paulo.
6 – Trazer os dados dos autores do sexo masculino que tiveram livros publicados por São
Paulo ou Rio de Janeiro (Questão Desafio).

Banco:	LIVRARIA
Tabela:	LIVROS
Atributos:
NOME DO LIVRO
NOME DO AUTOR
SEXO DO AUTOR
NUMERO DE PÁGINAS
NOME DA EDITORA
VALOR DO LIVRO
ESTADO (UF) DA EDITORA
ANO PUBLICACAO
"""
from tkinter import *

book = None
gender = None
pages_number = None
editor_name = None
book_value = None
editor_uf = None
year_publication = None
autor_name = None
book_store = []


def run():
    global book, gender, editor_name, editor_uf, book_store, autor_name
    autor_name = input("author's name: ")
    book = {autor_name: input("Book : ")}
    gender = {"Gender": input("Mas (M) or Fam (F): ")}
    editor_name = {"Editor name": input("Editorś name: ")}
    editor_uf = {"Editor UF:": input("Editor's UF: ")}

    read_pages()
    read_bookvalue()
    read_year_publication()

    store = [book, gender, pages_number, editor_name, book_value, editor_uf, year_publication]
    book_store.extend(store)

    again()


def read_pages():
    global pages_number
    try:
        pages_number = {"Number of pages": int(input("Input Number of pages: "))}
        return pages_number
    except ValueError:
        print("Please, Input Only Numbers: ")
        read_pages()


def read_bookvalue():
    global book_value
    try:
        book_value = {"Book Value": int(input("Book Value: "))}
        return book_value
    except ValueError:
        print("Please, Input Only Numbers: ")
        read_bookvalue()


def read_year_publication():
    global year_publication
    try:
        year_publication = {"Year of Publication": int(input("Year of Publication: "))}
        return year_publication
    except ValueError:
        print("Please, Input Only Numbers: ")
        read_bookvalue()


def again():
    yes = "yes"
    no = 'no'
    res = input("do you want to do it again? ")
    if res == yes:
        run()
    else:
        print("Good Bye")
        return


run()

print(book_store)

