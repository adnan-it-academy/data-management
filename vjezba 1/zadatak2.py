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

while input("Unos jos jednog korisnika : (Y/N)") == "Y" :
    users.append(User(input("Unesite korisnicko ime : "), input("Unesite mejl : "), int(input("Unesite godine : "))))
# Serijalizacija liste korisnika u fajl 'users.pkl'
fajl = open("users.pkl", "w")
# TODO: Serijalizujte listu korisnika i sačuvajte u fajl
serijalizovana_lista = pickle.dumps(users)
fajl.write(f"{pickle.dumps(users)}")
# Deserijalizacija i ispis korisnika
users = pickle.loads(serijalizovana_lista)


# TODO: Učitajte korisnike iz fajla i ispišite ih

print("Spremljeni korisnici:")
for user in users:
    print(user)
