"""
Zadanie 1: Race condition na wspolnym liczniku
Opis problemu:
Kilka watkow zwieksza ten sam licznik. Program wyglada niewinnie, ale wynik
moze byc mniejszy niz oczekiwany poniewaz operacja zwiekszania licznika nie
jest atomowa.
Cel:
Uruchom program, zaobserwuj problem i uzupelnij oznaczone miejsca tak, aby
wynik koncowy zawsze byl rowny EXPECTED_TOTAL.
Oczekiwany efekt:
Program wypisuje wartosc licznika rowna EXPECTED_TOTAL.
Wskazowka:
Do ochrony fragmentu kodu, ktory czyta i zapisuje wspolna zmienna, uzyj
threading.Lock.
"""

import threading
import time

THREAD_COUNT = 5
INCREMENTS_PER_THREAD = 1000
EXPECTED_TOTAL = THREAD_COUNT * INCREMENTS_PER_THREAD

counter = 0
#TODO: Utworz blokade, ktora zabezpieczy dostep do counter.


def increment_counter() -> None:
    global counter

    for _ in range(INCREMENTS_PER_THREAD):
        current_value = counter
        time.sleep(0.0001)
        counter = current_value + 1
        #TODO: Przenies sekcje krytyczna pod blokade.


def main() -> None:
    threads = [
        threading.Thread(target=increment_counter)
        for _ in range(THREAD_COUNT)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Wynik: {counter}")
    print(f"Oczekiwano: {EXPECTED_TOTAL}")


if __name__ == "__main__":
    main()
