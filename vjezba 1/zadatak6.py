# zadatak6.py

import pickle

# Definicija klase Book
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f"'{self.title}' by {self.author} - {self.genre}"

# Lista knjiga
books = []

# TODO: Učitajte postojeće knjige iz fajla ako postoji

# Dodavanje novih knjiga

# TODO: Omogućite korisniku da dodaje nove knjige

# Pretraga knjiga po autoru ili žanru

# TODO: Omogućite korisniku pretragu knjiga i ispišite rezultate

# Serijalizacija i čuvanje knjiga u fajl 'books.pkl'

# TODO: Serijalizujte listu knjiga i sačuvajte je u fajl
