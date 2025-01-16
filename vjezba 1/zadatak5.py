# zadatak5.py

import pickle

# Lista operacija
operations = []


def ucitaj_operacije():
    try:
        with open('operations.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def spremi_operacije():
    with open('operations.pkl', 'wb') as file:
        pickle.dump(operations, file)


def izvrsi_operaciju():
    print("\nOdaberite operaciju:")
    print("1. Zbir")
    print("2. Razlika")
    print("3. Produkt")
    print("4. Kvocijent")

    izbor = input("Unesite broj operacije (1/2/3/4): ")

    try:
        broj1 = float(input("Unesite prvi broj: "))
        broj2 = float(input("Unesite drugi broj: "))

        if izbor == '1':
            rezultat = broj1 + broj2
            operacija = f"{broj1} + {broj2} = {rezultat}"
        elif izbor == '2':
            rezultat = broj1 - broj2
            operacija = f"{broj1} - {broj2} = {rezultat}"
        elif izbor == '3':
            rezultat = broj1 * broj2
            operacija = f"{broj1} * {broj2} = {rezultat}"
        elif izbor == '4':
            if broj2 == 0:
                print("Greška: Dijeljenje s nulom nije dopušteno!")
                return None
            rezultat = broj1 / broj2
            operacija = f"{broj1} / {broj2} = {rezultat}"
        else:
            print("Nepoznat izbor. Pokušajte ponovo.")
            return None

        
        operations.append(operacija)
        return rezultat

    except ValueError:
        print("Greška: Molimo unesite važeće brojeve.")
        return None


if __name__ == "__main__":
    
    operations = ucitaj_operacije()

    while True:
        
        rezultat = izvrsi_operaciju()
        if rezultat is not None:
            print(f"Rezultat: {rezultat}")

        
        nastavak = input("\nŽelite li izvršiti još operaciju? (da/ne): ")
        if nastavak.lower() != 'da':
            break

    
    spremi_operacije()

    
    print("\nPrethodne operacije:")
    for operacija in operations:
        print(operacija)


