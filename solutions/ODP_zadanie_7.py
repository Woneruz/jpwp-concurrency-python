"""
Zadanie 7: ThreadPoolExecutor
Napisz program od zera, ktory uruchamia wiele niezaleznych zadan z uzyciem
ThreadPoolExecutor zamiast recznego tworzenia watkow.
Pokaz prostszy sposob zarzadzania pula watkow dla zadan, ktore mozna wykonac niezaleznie.
Oczekiwany efekt:
Program przetwarza liste danych wejsciowych rownolegle, zbiera wyniki i
wypisuje je po zakonczeniu pracy.
"""

import time
from concurrent.futures import ThreadPoolExecutor


def przetworz(x: int) -> int:
    # Symulacja zadania I/O-bound (np. zapytanie sieciowe)
    time.sleep(0.5)
    return x * x


def main() -> None:
    dane = list(range(1, 11))

    start = time.time()

    with ThreadPoolExecutor(max_workers=4) as executor:
        wyniki = list(executor.map(przetworz, dane))

    czas = time.time() - start

    print(f"Dane wejsciowe: {dane}")
    print(f"Wyniki:         {wyniki}")
    print(f"Czas wykonania: {czas:.2f}s (sekwencyjnie zajeloby ~{len(dane) * 0.5:.1f}s)")


if __name__ == "__main__":
    main()
