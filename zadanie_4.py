"""
Zadanie 4: Producent-konsument z kilkoma workerami

Opis problemu:
Napisz program od zera. Jeden producent ma utworzyc serie zadan, a kilku
workerow ma rownolegle pobierac je z kolejki i przetwarzac.

Cel:
Zaimplementuj wzorzec producent-konsument z uzyciem threading.Thread oraz
queue.Queue.

Oczekiwany efekt:
Program tworzy co najmniej 10 zadan, przetwarza je przez co najmniej 3 watki
robocze i konczy prace bez zawieszenia.

Wskazowka:
Zacznij od funkcji producer(), worker() i main(). Do synchronizacji przeplywu
zadan wykorzystaj Queue.
"""

import queue
import threading


def main() -> None:
    pass


if __name__ == "__main__":
    main()
