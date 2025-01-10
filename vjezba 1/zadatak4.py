# zadatak4.py

import pickle

# Definicija klase Score
class Score:
    def __init__(self, username, points):
        self.username = username
        self.points = points

    def __repr__(self):
        return f"{self.username}: {self.points}"

# Lista rezultata
scores = []

# TODO: Omogućite unos rezultata za više korisnika

# Sortiranje rezultata

# TODO: Sortirajte listu rezultata po broju bodova (opadajuće)

# Serijalizacija liste rezultata u fajl 'scores.pkl'

# TODO: Serijalizujte listu rezultata i sačuvajte je u fajl

# Deserijalizacija i ispis rang liste

# TODO: Učitajte rezultate iz fajla i ispišite rang listu

print("Rang lista:")
for score in loaded_scores:
    print(score)
