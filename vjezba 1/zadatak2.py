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

def unos_korisnika():
    username = input("Unesite korisničko ime: ")
    email = input("Unesite email: ")
    age = int(input("Unesite godine: "))
    return User(username, email, age)

# Serijalizacija liste korisnika u fajl 'users.pkl'

def spremi_korisnike(korisnici):
    with open('users.pkl', 'wb') as file:
        pickle.dump(korisnici, file)

# TODO: Serijalizujte listu korisnika i sačuvajte u fajl

def ucitaj_korisnike():
    try:
        with open('users.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    
# Deserijalizacija i ispis korisnika

if __name__ == "__main__":
    # Unos novih korisnika
    nastavak = 'da'
    while nastavak.lower() == 'da':
        korisnik = unos_korisnika()
        users.append(korisnik)
        nastavak = input("Želite li unijeti još korisnika? (da/ne): ")

# TODO: Učitajte korisnike iz fajla i ispišite ih
    spremi_korisnike(users)

   
    loaded_users = ucitaj_korisnike()

print("Spremljeni korisnici:")
for user in loaded_users:
    print(user)
