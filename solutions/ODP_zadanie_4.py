"""
Zadanie 4: Producent-konsument z kilkoma workerami
Napisz program od zera. Jeden producent ma utworzyc serie zadan, a kilku
workerow ma rownolegle pobierac je z kolejki i przetwarzac.
Zaimplementuj wzorzec producent-konsument z uzyciem threading.Thread oraz
queue.Queue.Program powinien tworzyc co najmniej 10 zadan,
przetwarza je przez co najmniej 3 watki
robocze i konczy prace bez zawieszenia.
"""


# slajd 13 (graceful shutdown - sygnal konca None)
# slajd 14 (tyle None ile workerow - kazdy odbierze swoj sygnal)
# slajd 14 (consumer wykrywa None i wychodzi z petli)
# slajd 14 (brak daemon=True - workery koncza czysto)
# slajd 14 (q.join w main - czeka az kolejka opustoszeje)


import queue
import threading
import time


TASK_COUNT = 10
WORKER_COUNT = 3
STOP_SIGNAL = None

task_queue: queue.Queue[int | None] = queue.Queue()


def producer() -> None:
    for task_id in range(1, TASK_COUNT + 1):
        task_queue.put(task_id)
        print(f"Producent utworzyl zadanie {task_id}")
        time.sleep(0.05)

    # Sygnal konca - po jednym dla kazdego workera
    for _ in range(WORKER_COUNT):
        task_queue.put(STOP_SIGNAL)


def worker(worker_id: int) -> None:
    while True:
        task = task_queue.get()

        if task is STOP_SIGNAL:
            task_queue.task_done()
            print(f"Worker {worker_id} koncze prace")
            break

        print(f"Worker {worker_id} przetwarza zadanie {task}")
        time.sleep(0.1)
        task_queue.task_done()


def main() -> None:
    workers = [
        threading.Thread(target=worker, args=(worker_id,))
        for worker_id in range(1, WORKER_COUNT + 1)
    ]

    for thread in workers:
        thread.start()

    producer_thread = threading.Thread(target=producer)
    producer_thread.start()

    producer_thread.join()
    task_queue.join()

    for thread in workers:
        thread.join()

    print("Wszystkie zadania zostaly przetworzone.")


if __name__ == "__main__":
    main()
