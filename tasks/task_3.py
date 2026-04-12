"""
Zadanie 3: Komunikacja miedzy watkami przez Queue

Opis problemu:
Producent tworzy zadania, a konsument powinien je odbierac i przetwarzac.
Obecny kod ma przygotowane miejsca TODO, w ktorych trzeba wykorzystac
queue.Queue zamiast zwyklej listy.

Cel:
Uzupelnij program tak, aby producent dodawal zadania do kolejki, a konsument
bezpiecznie je odbieral.

Oczekiwany efekt:
Program wypisuje przetworzenie zadan od 1 do TASK_COUNT i konczy prace bez
zawieszenia.

Wskazowka:
Uzyj metod put(), get(), task_done() oraz join() z klasy Queue.
"""

import queue
import threading
import time


TASK_COUNT = 8
task_queue: queue.Queue[int] = queue.Queue()


def producer() -> None:
    for task_id in range(1, TASK_COUNT + 1):
        # TODO: Dodaj task_id do task_queue.
        print(f"Producent utworzyl zadanie {task_id}")
        time.sleep(0.05)


def consumer() -> None:
    processed = 0

    while processed < TASK_COUNT:
        # TODO: Pobierz zadanie z task_queue.
        task_id = 0
        print(f"Konsument przetwarza zadanie {task_id}")
        time.sleep(0.1)
        processed += 1
        # TODO: Oznacz zadanie jako zakonczone.


def main() -> None:
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    consumer_thread.start()
    producer_thread.start()

    producer_thread.join()
    # TODO: Poczekaj, az kolejka zostanie oprozniona.
    consumer_thread.join()

    print("Wszystkie zadania zostaly przetworzone.")


if __name__ == "__main__":
    main()
