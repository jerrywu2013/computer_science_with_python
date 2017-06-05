# L-16 MCS 260 Wed 18 Feb 2015 : a library
"""
We demonstrate the use of files with a simple model
of a library.
"""

from bkform import pack, get_key, get_title, get_status

def show_menu():
    "shows the menu and prompts for a choice"
    print("Welcome to our library!  Choose:")
    print("  0. leave the program")
    print("  1. show all books in the collection")
    print("  2. add a new book to the collection")
    print("  3. check out a book of the library")
    print("  4. return a book to the library")
    choice = input("Type 0, 1, 2, 3, or 4 : ")
    return choice

def number_of_books():
    "returns the number of books in the collection"
    lib = open('books', 'r')
    collection = lib.readlines()
    result = len(collection)
    lib.close()
    return result

def show_books():
    "shows the books currently in the collection"
    lib = open('books', 'r')
    collection = lib.readlines()
    for book in collection:
        abook = ' ' + str(get_key(book))
        abook += ' ' + get_title(book)
        if get_status(book):
            print(abook + ' available')
        else:
            print(abook + ' checked out')
    lib.close()

def add_book():
    "adds a book to the collection"
    numb = number_of_books()
    title = input('Give title : ')
    newbook = pack(numb+1, 1, title)
    lib = open('books', 'a')
    lib.write(newbook)
    lib.close()

def checkout():
    "checks out a book"
    show_books()
    k = int(input('give book number : '))
    lib = open('books', 'r')
    collection = lib.readlines()
    lib.close()
    lib = open('books', 'w')
    for book in collection:
        if get_key(book) == k:
            if not get_status(book):
                print(get_title(book) + ' is unavailable')
                lib.write(book)
            else:
                lib.write(pack(k, 0, get_title(book)))
        else:
            lib.write(book)
    lib.close()

def checkin():
    "return a book to the library"
    k = int(input('give book number : '))
    lib = open('books', 'r')
    collection = lib.readlines()
    lib.close()
    lib = open('books', 'w')
    for book in collection:
        if get_key(book) == k:
            kbook = pack(k, 1, get_title(book))
            lib.write(kbook)
        else:
            lib.write(book)
    lib.close()

def main():
    "handles menu selection"
    while True:
        choice = show_menu()
        if choice == '0':
            break
        elif choice == '1':
            show_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            checkout()
        elif choice == '4':
            checkin()

main()
