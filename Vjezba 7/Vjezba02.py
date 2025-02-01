import multiprocessing as mp
import time

def posao():
    print("Proces je pokrenut")
    time.sleep(2)
    print("Proces završen")

if __name__ == '__main__':
    p = mp.Process(target=posao)
    p.start()
    p.join()