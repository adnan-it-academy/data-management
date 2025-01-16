# zadatak1.py

import pickle
import random

# Generisanje liste slučajnih brojeva
numbers = []
# TODO: Generišite listu od 10 slučajnih brojeva između 1 i 100
numbers = [random.randint(1, 100) for x in range(10)]
# Serijalizacija liste u fajl 'numbers.pkl'
fajl = open("numbers.pkl","w")
serijalizovana_lista = pickle.dumps(numbers)
# TODO: Serijalizujte listu koristeći pickle i upišite u fajl
fajl.write(f"{pickle.dumps(numbers)}")
# Deserijalizacija i prikaz
numbers = pickle.loads(serijalizovana_lista)
# TODO: Učitajte listu iz fajla i ispišite je
print("Originalna lista:", numbers)
#print("Učitana lista:", loaded_numbers)
fajl.close()
