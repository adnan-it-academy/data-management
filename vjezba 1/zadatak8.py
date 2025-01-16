# zadatak8.py

import pickle


activities = []


def ucitaj_aktivnosti():
    try:
        with open('activities.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def spremi_aktivnosti():
    with open('activities.pkl', 'wb') as file:
        pickle.dump(activities, file)


def dodaj_aktivnost():
    time = input("Unesite vrijeme aktivnosti (npr. 08:00): ")
    description = input("Unesite opis aktivnosti: ")
    activity = {"time": time, "description": description}
    activities.append(activity)


if __name__ == "__main__":
    
    activities = ucitaj_aktivnosti()

    while True:
        print("\nOpcije:")
        print("1. Dodaj novu aktivnost")
        print("2. Ispiši dnevne aktivnosti")
        print("3. Izlaz")
        izbor = input("Odaberite opciju (1/2/3): ")

        if izbor == '1':
            dodaj_aktivnost()
        elif izbor == '2':
            print("\nDnevne aktivnosti:")
            if activities:
                for activity in activities:
                    print(f"{activity['time']} - {activity['description']}")
            else:
                print("Nema unesenih aktivnosti.")
        elif izbor == '3':
            break
        else:
            print("Nepoznat izbor. Pokušajte ponovo.")

    
    spremi_aktivnosti()

    print("Program je završio.")
