# zadatak1.py

import pickle
import random

# Generisanje liste slučajnih brojeva
numbers = []

# TODO: Generišite listu od 10 slučajnih brojeva između 1 i 100
random_numbers = [random.randint(1, 100) for _ in range(10)]
# Serijalizacija liste u fajl 'numbers.pkl'

# TODO: Serijalizujte listu koristeći pickle i upišite u fajl
with open('numbers.pkl', 'wb') as file:
    pickle.dump(random_numbers, file)
# Deserijalizacija i prikaz
with open('numbers.pkl', 'rb') as file:
    loaded_numbers = pickle.load(file)

# TODO: Učitajte listu iz fajla i ispišite je

print("Originalna lista:", numbers)
print("Učitana lista:", loaded_numbers)




