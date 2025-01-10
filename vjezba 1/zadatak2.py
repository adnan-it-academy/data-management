# zadatak2.py

import pickle

# Definicija klase User
class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def __repr__(self):
        return f"User(username={self.username}, email={self.email}, age={self.age})"

# Lista korisnika
users = []

# TODO: Omogućite unos podataka o korisnicima i dodajte ih u listu

# Serijalizacija liste korisnika u fajl 'users.pkl'

# TODO: Serijalizujte listu korisnika i sačuvajte u fajl

# Deserijalizacija i ispis korisnika

# TODO: Učitajte korisnike iz fajla i ispišite ih

print("Spremljeni korisnici:")
for user in loaded_users:
    print(user)
