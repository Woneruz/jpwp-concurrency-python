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


# slajd 12 (API Queue - put dodaje element)
# slajd 12 (API Queue - get pobiera element, blokuje gdy pusta)
# slajd 12 (task_done - sygnalizuje koniec zadania)
# slajd 12 (q.join - czeka az kolejka opustoszeje)


import queue
import threading
import time


TASK_COUNT = 8
task_queue: queue.Queue[int] = queue.Queue()


def producer() -> None:
    for task_id in range(1, TASK_COUNT + 1):
        task_queue.put(task_id)
        print(f"Producent utworzyl zadanie {task_id}")
        time.sleep(0.05)


def consumer() -> None:
    processed = 0

    while processed < TASK_COUNT:
        task_id = task_queue.get()
        print(f"Konsument przetwarza zadanie {task_id}")
        time.sleep(0.1)
        processed += 1
        task_queue.task_done()


def main() -> None:
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    consumer_thread.start()
    producer_thread.start()

    producer_thread.join()
    task_queue.join()
    consumer_thread.join()

    print("Wszystkie zadania zostaly przetworzone.")


if __name__ == "__main__":
    main()
