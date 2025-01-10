# zadatak9.py

import pickle

# Definicija klase Product
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} - {self.price}$ ({self.quantity} kom)"

# Lista proizvoda
products = []

# TODO: Učitajte postojeće proizvode iz fajla ako postoji

# Dodavanje novih proizvoda

# TODO: Omogućite korisniku da dodaje nove proizvode

# Ažuriranje količine proizvoda

# TODO: Omogućite korisniku da ažurira količinu postojećih proizvoda

# Serijalizacija i čuvanje proizvoda u fajl 'products.pkl'

# TODO: Serijalizujte listu proizvoda i sačuvajte je u fajl

# Ispis trenutnog inventara

print("\nTrenutni inventar:")
for product in products:
    print(product)
