"""
Zadanie 5: Poprawne konczenie pracy watkow
Opis problemu:
Worker pobieraja zadania z kolejki w petli nieskonczonej. Bez sygnalu
zakonczenia program moze sie zawiesic, bo watki beda czekaly na kolejne
zadania.Uzupelnij program tak, aby po przetworzeniu wszystkich zadan kazdy worker
otrzymal sygnal STOP_SIGNAL i zakonczyl prace.
Oczekiwany efekt:
Program przetwarza wszystkie zadania, wypisuje komunikaty o zakonczeniu pracy
workerow i wraca do terminala.
"""

import queue
import threading
import time


WORKER_COUNT = 3
TASK_COUNT = 9
STOP_SIGNAL = None

task_queue: queue.Queue[int | None] = queue.Queue()


def worker(worker_id: int) -> None:
    while True:
        task = task_queue.get()

        #Do zrobienia: Jesli task to STOP_SIGNAL, oznacz zadanie jako wykonane i wyjdz z petli.

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

    for task_id in range(1, TASK_COUNT + 1):
        task_queue.put(task_id)

    #Do zrobienia: Dodaj STOP_SIGNAL do kolejki odpowiednia liczbe razy.
    #Do zrobienia: Poczekaj na oproznienie kolejki.

    for thread in workers:
        thread.join()

    print("Program zakonczyl prace.")


if __name__ == "__main__":
    main()
