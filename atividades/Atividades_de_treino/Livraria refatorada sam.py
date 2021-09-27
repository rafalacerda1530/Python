# -*- coding: utf-8 -*-
from tkinter import *


book_store = []

'''
    Book store is a collection of book!
'''


def run():
    global book_store

    book = {}  # empty dict!

    book["title"] = input("Book title: ")
    book["autor_name"] = input("author's name: ")
    book["gender"] = input("Mas (M) or Fam (F): ")
    book["publisher_name"] = input("Publisher name: ")
    book["editor_uf"] = input("Editor's UF: ")

    book["pages_number"] = read_pages()
    book["book_value"] = read_bookvalue()
    book["year_publication"] = read_year_publication()

    book_store.append(book)
    print(book_store)
    again()
    question()


def read_pages():
    try:
        pages_number = int(input("Input Number of pages: "))
        return pages_number
    except ValueError:
        print("Please, Input Only Numbers: ")
        read_pages()


def read_bookvalue():
    try:
        book_value = int(input("Book Value: "))
        return book_value
    except ValueError:
        print("Please, Input Only Numbers: ")
        read_bookvalue()


def read_year_publication():
    try:
        year_publication = int(input("Year of Publication: "))
        return year_publication
    except ValueError:
        print("Please, Input Only Numbers: ")
        read_bookvalue()


def search_by_author_name(autor_name):
    '''
        Search books by author's name.

        returns: The book if it was found or empty dict when not found.
    '''
    global book_store

    for book in book_store:
        if book['autor_name'] == autor_name:
            root = Tk()
            root.title('search by author name')
            var = StringVar()
            label = Label(root, font=("Arial", 17), bg="white", fg="black", textvariable=var, relief=RAISED,
                          width=50, height=10)

            var.set(f"The author {book['autor_name']} owns the books: {book['title']}")
            label.pack()
            root.mainloop()
            return

    return {}


def again():
    yes = "yes"
    no = 'no'
    res = input("do you want to do it again, yes or no ? ")
    if res == yes:
        run()
    else:
        print("Good Bye")
        return


def question():
    yes = "yes"
    no = 'no'
    res = input("Do you want to search for a book, yes or no ?: ")
    if res == yes:
        print(search_by_author_name(input("Enter the author's name: ")))
        question()
    else:
        print("Good Bye")
        return


if __name__ == "__main__":
    run()
