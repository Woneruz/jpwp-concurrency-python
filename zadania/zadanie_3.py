"""
Zadanie 3: Komunikacja miedzy watkami przez Queue
Producent tworzy zadania, a konsument powinien je odbierac i przetwarzac.
Obecny kod ma przygotowane miejsca w ktorych trzeba wykorzystac queue.Queue zamiast zwyklej listy.
Uzupelnij program tak, aby producent dodawal zadania do kolejki, a konsument
bezpiecznie je odbieral.
Oczekiwany efekt:
Program wypisuje przetworzenie zadan od 1 do TASK_COUNT i konczy prace bez
zawieszenia.
"""

import queue
import threading
import time


TASK_COUNT = 8
task_queue: queue.Queue[int] = queue.Queue()


def producer() -> None:
    for task_id in range(1, TASK_COUNT + 1):
        #Do zrobienia: Dodaj task_id do task_queue.
        print(f"Producent utworzyl zadanie {task_id}")
        time.sleep(0.05)


def consumer() -> None:
    processed = 0

    while processed < TASK_COUNT:
        #Do zrobienia: Pobierz zadanie z task_queue.
        task_id = 0
        print(f"Konsument przetwarza zadanie {task_id}")
        time.sleep(0.1)
        processed += 1
        #Do zrobienia: Oznacz zadanie jako zakonczone.


def main() -> None:
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    consumer_thread.start()
    producer_thread.start()

    producer_thread.join()
    #Do zrobienia: Poczekaj az kolejka zostanie oprozniona.
    consumer_thread.join()

    print("Wszystkie zadania zostaly przetworzone.")


if __name__ == "__main__":
    main()
