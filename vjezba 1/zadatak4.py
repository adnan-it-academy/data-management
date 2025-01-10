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


def unos_rezultata():
    username = input("Unesite korisničko ime: ")
    points = int(input("Unesite broj bodova: "))
    return Score(username, points)


def spremi_rezultate():
    with open('scores.pkl', 'wb') as file:
        pickle.dump(scores, file)


def ucitaj_rezultate():
    try:
        with open('scores.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    
    scores = ucitaj_rezultate()

    
    nastavak = 'da'
    while nastavak.lower() == 'da':
        rezultat = unos_rezultata()
        scores.append(rezultat)
        nastavak = input("Želite li unijeti još rezultata? (da/ne): ")

    
    scores.sort(key=lambda x: x.points, reverse=True)

    
    spremi_rezultate()

print("Rang lista:")
for score in scores:
    print(score)
