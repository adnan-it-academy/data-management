import multiprocessing as mp
import math

rezultati = []

def napravi_kalkulacije(broj, rezultat):
    for br in broj:
        rezultat.append(math.sqrt(br**3))

if __name__ == '__main__':
    brojevi_liste = list(range(1_000_000))
    p1 = mp.Process(target=napravi_kalkulacije, args=(brojevi_liste, rezultati))
    p1.start()
    p1.join()
    print("Obrada završena 1")

    brojevi_liste = list(range(1_000_000))
    p2 = mp.Process(target=napravi_kalkulacije, args=(brojevi_liste, rezultati))
    p2.start()
    p2.join()
    print("Obrada završena 2")