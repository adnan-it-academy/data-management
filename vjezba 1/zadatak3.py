# zadatak3.py

import pickle
import os

# Lista zadataka
tasks = []

# Fajl u kojem će biti sačuvani zadaci
TASKS_FILE = 'tasks.pkl'

# Funkcija za učitavanje zadataka iz fajla
def load_tasks():
    try:
        with open(TASKS_FILE, 'rb') as file:
            tasks = pickle.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Funkcija za čuvanje zadataka u fajl
def save_tasks(tasks):
    with open(TASKS_FILE, 'wb') as file:
        pickle.dump(tasks, file)

# Glavni program
def main():
    tasks = load_tasks()

    # Ispis svih postojećih zadataka
    if tasks:
        print("Trenutni zadaci:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Nemate nijedan zadatak.")
    
    # Omogućavanje dodavanja novih zadataka
    while True:
        new_task = input("\nUnesite novi zadatak (ili pritisnite Enter da biste završili): ")
        if new_task.strip():
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"Zadatak '{new_task}' je dodan.")
        else:
            break
    
    # Ispis poruke o završetku programa
    print("\nKraj programa. Vaši zadaci su sačuvani.")

if __name__ == "__main__":
    main()

# TODO: Učitajte postojeće zadatke iz fajla ako postoji

# Ispis postojećih zadataka
# Funkcija za učitavanje zadataka iz fajla
def load_tasks():
    if os.path.exists(TASKS_FILE):  # Proveravamo da li fajl postoji
        with open(TASKS_FILE, 'rb') as file:
            tasks = pickle.load(file)
    else:
        tasks = []
    return tasks


    # Ispis svih postojećih zadataka
    if tasks:
        print("Trenutni zadaci:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Nemate nijedan zadatak.")

if __name__ == "__main__":
    main()

# TODO: Ispišite sve postojeće zadatke

# Dodavanje novih zadataka

# TODO: Omogućite korisniku da dodaje nove zadatke

# Serijalizacija i čuvanje zadataka u fajl 'tasks.pkl'

# TODO: Serijalizujte listu zadataka i sačuvajte je u fajl
with open(TASKS_FILE, 'wb') as file:
    pickle.dump(tasks, file)

print(f"Lista zadataka je uspešno sačuvana u fajl '{TASKS_FILE}'")
