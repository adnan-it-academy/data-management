# zadatak9.py

import pickle


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} - {self.price}$ ({self.quantity} kom)"


products = []


def ucitaj_proizvode():
    try:
        with open('products.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def spremi_proizvode():
    with open('products.pkl', 'wb') as file:
        pickle.dump(products, file)


def dodaj_proizvod():
    name = input("Unesite naziv proizvoda: ")
    price = float(input("Unesite cijenu proizvoda: "))
    quantity = int(input("Unesite količinu proizvoda: "))
    product = Product(name, price, quantity)
    products.append(product)


def azuriraj_kolicinu():
    name = input("Unesite naziv proizvoda za koji želite ažurirati količinu: ")
    new_quantity = int(input("Unesite novu količinu proizvoda: "))

    found = False
    for product in products:
        if product.name.lower() == name.lower():
            product.quantity = new_quantity
            found = True
            print(f"Količina proizvoda {product.name} ažurirana na {new_quantity}.")
            break

    if not found:
        print(f"Proizvod s nazivom '{name}' nije pronađen.")


if __name__ == "__main__":
    
    products = ucitaj_proizvode()

    while True:
        print("\nOpcije:")
        print("1. Dodaj novi proizvod")
        print("2. Ažuriraj količinu proizvoda")
        print("3. Ispiši trenutni inventar")
        print("4. Izlaz")
        izbor = input("Odaberite opciju (1/2/3/4): ")

        if izbor == '1':
            dodaj_proizvod()
        elif izbor == '2':
            azuriraj_kolicinu()
        elif izbor == '3':
            print("\nTrenutni inventar:")
            if products:
                for product in products:
                    print(product)
            else:
                print("Inventar je prazan.")
        elif izbor == '4':
            break
        else:
            print("Nepoznat izbor. Pokušajte ponovo.")

    
    spremi_proizvode()

    print("\nProgram je završio.")
