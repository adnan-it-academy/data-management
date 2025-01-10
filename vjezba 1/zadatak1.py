# zadatak1.py

import pickle
import random

# Generisanje liste slučajnih brojeva
numbers = []

# TODO: Generišite listu od 10 slučajnih brojeva između 1 i 100
numbers = [random.randint(1, 100) for _ in range(10)]
    

# Serijalizacija liste u fajl 'numbers.pkl'
with open('numbers.pkl', 'wb') as f:
    pickle.dump(numbers, f)

print("Lista je serijalizovana u fajl 'numbers.pkl'")

# TODO: Serijalizujte listu koristeći pickle i upišite u fajl

# Deserijalizacija i prikaz

# TODO: Učitajte listu iz fajla i ispišite je
with open('numbers.pkl', 'rb') as file:
    loaded_numbers = pickle.load(file)

# Ispis učitane lista

print("Originalna lista:", numbers)
print("Učitana lista:", loaded_numbers)
