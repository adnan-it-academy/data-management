# zadatak10.py

import pickle

# Definicija klase Question
class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def __repr__(self):
        return self.text

# Lista pitanja
questions = []

# Dodavanje novih pitanja

# TODO: Omogućite korisniku da kreira nova pitanja za kviz

# Serijalizacija i čuvanje pitanja u fajl 'quiz.pkl'

# TODO: Serijalizujte listu pitanja i sačuvajte je u fajl

# Učitavanje pitanja i izvođenje kviza

# TODO: Učitajte pitanja iz fajla i omogućite korisniku da rješava kviz

# Ispis rezultata kviza

print(f"\nVaš rezultat: {score}/{len(loaded_questions)}")
