"""
Zadanie 6: Wykrycie i naprawa deadlocka

Opis problemu:
Napisz program od zera, ktory pokazuje sytuacje deadlocka: dwa watki probuja
zdobyc dwie blokady w przeciwnej kolejnosci. Nastepnie popraw program tak, aby
deadlock nie wystepowal.

Cel:
Pokazac, dlaczego kolejnosc zdobywania blokad ma znaczenie i jak mozna uniknac
zakleszczenia.

Oczekiwany efekt:
W wersji poprawionej oba watki koncza prace i program wraca do terminala.

Wskazowka:
Najprostsza poprawa to ustalenie jednej, stalej kolejnosci zdobywania lock_a i
lock_b we wszystkich watkach.
"""

import threading


def main() -> None:
    pass


if __name__ == "__main__":
    main()
