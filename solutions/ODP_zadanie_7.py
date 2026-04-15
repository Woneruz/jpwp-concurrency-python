"""
Zadanie 7: ThreadPoolExecutor
Napisz program od zera, ktory uruchamia wiele niezaleznych zadan z uzyciem
ThreadPoolExecutor zamiast recznego tworzenia watkow.
Pokaz prostszy sposob zarzadzania pula watkow dla zadan, ktore mozna wykonac niezaleznie.
Oczekiwany efekt:
Program przetwarza liste danych wejsciowych rownolegle, zbiera wyniki i
wypisuje je po zakonczeniu pracy.
"""


# slajd 4 (watki idealne dla zadan I/O-bound - GIL zwalniany)
# slajd 17 (ThreadPoolExecutor - with automatycznie uruchamia i konczy watki)
# slajd 17 (max_workers - ograniczenie rownoleglosci)
# slajd 17 (executor.map - wygodna dla listy zadan tego samego typu)
# slajd 21 (benchmark - watki przyspieszaja I/O ~10x vs sekwencyjnie)


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
