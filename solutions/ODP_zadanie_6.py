"""
Zadanie 6: Wykrycie i naprawa deadlocka
Napisz program od zera, ktory pokazuje sytuacje deadlocka: dwa watki probuja
zdobyc dwie blokady w przeciwnej kolejnosci. Nastepnie popraw program tak, aby
deadlock nie wystepowal.
Pokaz, dlaczego kolejnosc zdobywania blokad ma znaczenie i jak mozna uniknac zakleszczenia
Oczekiwany efekt:
W wersji poprawionej oba watki koncza prace i program wraca do terminala.
"""


# slajd 15 (deadlock - dwa watki, locki w przeciwnej kolejnosci)
# slajd 15 (jak unikac: stala kolejnosc, timeout, mniej blokad, Queue)
# slajd 16 (Recepta - ustal globalny porzadek lock_a -> lock_b)
# slajd 16 (kazdy watek bierze locki w tej samej kolejnosci - cykl niemozliwy)


import threading
import time


lock_a = threading.Lock()
lock_b = threading.Lock()


# WERSJA Z DEADLOCKIEM (do demonstracji - zawiesi sie)
def watek_1_deadlock() -> None:
    with lock_a:
        print("Watek 1: zdobyl lock_a, czeka na lock_b")
        time.sleep(0.1)
        with lock_b:
            print("Watek 1: zdobyl lock_b")


def watek_2_deadlock() -> None:
    with lock_b:
        print("Watek 2: zdobyl lock_b, czeka na lock_a")
        time.sleep(0.1)
        with lock_a:
            print("Watek 2: zdobyl lock_a")


# WERSJA POPRAWIONA - stala kolejnosc blokad
# REGULA: ZAWSZE najpierw lock_a, potem lock_b
def watek_1_safe() -> None:
    with lock_a:
        time.sleep(0.1)
        with lock_b:
            print("Watek 1: bezpiecznie wykonuje sekcje krytyczna")


def watek_2_safe() -> None:
    with lock_a:
        time.sleep(0.1)
        with lock_b:
            print("Watek 2: bezpiecznie wykonuje sekcje krytyczna")


def main() -> None:
    print("Wersja poprawiona (stala kolejnosc blokad)")

    t1 = threading.Thread(target=watek_1_safe)
    t2 = threading.Thread(target=watek_2_safe)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Oba watki zakonczyly prace - brak deadlocka.")

    # Aby zobaczyc deadlock, podmien watek_1_safe/watek_2_safe na
    # watek_1_deadlock/watek_2_deadlock - program sie zawiesi.


if __name__ == "__main__":
    main()
