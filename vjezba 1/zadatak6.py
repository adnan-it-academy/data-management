# zadatak6.py

import pickle


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f"'{self.title}' by {self.author} - {self.genre}"


books = []


def ucitaj_knjige():
    try:
        with open('books.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def spremi_knjige():
    with open('books.pkl', 'wb') as file:
        pickle.dump(books, file)


def dodaj_knjigu():
    title = input("Unesite naziv knjige: ")
    author = input("Unesite autora knjige: ")
    genre = input("Unesite žanr knjige: ")
    knjiga = Book(title, author, genre)
    books.append(knjiga)


def pretrazi_knjige():
    print("\nPretraga knjiga")
    print("1. Pretraga po autoru")
    print("2. Pretraga po žanru")
    izbor = input("Odaberite opciju (1/2): ")

    if izbor == '1':
        autor = input("Unesite ime autora: ")
        rezultati = [knjiga for knjiga in books if autor.lower() in knjiga.author.lower()]
    elif izbor == '2':
        zanr = input("Unesite žanr: ")
        rezultati = [knjiga for knjiga in books if zanr.lower() in knjiga.genre.lower()]
    else:
        print("Nepoznat izbor.")
        return []

    return rezultati


if __name__ == "__main__":
    
    books = ucitaj_knjige()

    while True:
        print("\nOpcije:")
        print("1. Dodaj novu knjigu")
        print("2. Pretraga knjiga")
        print("3. Ispiši sve knjige")
        print("4. Izlaz")
        izbor = input("Odaberite opciju (1/2/3/4): ")

        if izbor == '1':
            dodaj_knjigu()
        elif izbor == '2':
            rezultati = pretrazi_knjige()
            if rezultati:
                print("\nRezultati pretrage:")
                for knjiga in rezultati:
                    print(knjiga)
            else:
                print("Nema rezultata pretrage.")
        elif izbor == '3':
            print("\nSvi uneseni podaci:")
            if books:
                for knjiga in books:
                    print(knjiga)
            else:
                print("Nema knjiga u bazi podataka.")
        elif izbor == '4':
            break
        else:
            print("Nepoznat izbor. Pokušajte ponovo.")

    
    spremi_knjige()

    print("Program je završio.")
