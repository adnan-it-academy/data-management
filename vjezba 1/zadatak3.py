# zadatak3.py

import pickle


tasks = []


def ucitaj_zadatke():
    try:
        with open('tasks.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def spremi_zadatke():
    with open('tasks.pkl', 'wb') as file:
        pickle.dump(tasks, file)


if __name__ == "__main__":
    
    tasks = ucitaj_zadatke()

    
    if tasks:
        print("Postojeći zadaci:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("Nema postojećih zadataka.")

    
    while True:
        task = input("Unesite novi zadatak (ili 'kraj' za izlaz): ")
        if task.lower() == 'kraj':
            break
        tasks.append(task)

    
    spremi_zadatke()

    
    print("Svi zadaci:")
    for task in tasks:
        print(f"- {task}")