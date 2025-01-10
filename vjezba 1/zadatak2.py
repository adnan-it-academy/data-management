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

# Omogućavanje unosa korisničkih podataka
while True:
    # Unos podataka o korisniku
    username = input("Unesite korisničko ime: ")
    email = input("Unesite email adresu: ")
    age = int(input("Unesite godine korisnika: "))
    
    # Dodavanje korisnika u listu
    users.append(User(username, email, age))
    
    # Pitanje korisniku da li želi dodati još korisnika
    more_users = input("Želite li dodati još korisnika? (Y/N): ").strip().upper()
    if more_users != "Y":
        break

# Ispis svih korisnika
print("\nLista korisnika:")
for user in users:
    print(user)

# Serijalizacija liste korisnika u fajl 'users.pkl'

# TODO: Serijalizujte listu korisnika i sačuvajte u fajl
with open('users.pkl', 'wb') as file:
    pickle.dump(users, file)

print("Lista korisnika je serijalizovana i upisana u fajl 'users.pkl'")

# Deserijalizacija i ispis korisnika

# TODO: Učitajte korisnike iz fajla i ispišite ih
with open('users.pkl', 'rb') as file:
    users = pickle.load(file)

# Ispis svih korisnika
print("\nLista korisnika:")
for user in users:
    print(user)

print("Spremljeni korisnici:")
for user in users:
    print(user)
