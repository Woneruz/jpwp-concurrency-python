"""
Zadanie 7: ThreadPoolExecutor

Opis problemu:
Napisz program od zera, ktory uruchamia wiele niezaleznych zadan z uzyciem
ThreadPoolExecutor zamiast recznego tworzenia watkow.

Cel:
Pokazac prostszy sposob zarzadzania pula watkow dla zadan, ktore mozna
wykonac niezaleznie.

Oczekiwany efekt:
Program przetwarza liste danych wejsciowych rownolegle, zbiera wyniki i
wypisuje je po zakonczeniu pracy.

Wskazowka:
Uzyj concurrent.futures.ThreadPoolExecutor oraz metody map() albo submit().
"""

from concurrent.futures import ThreadPoolExecutor


def main() -> None:
    pass


if __name__ == "__main__":
    main()
