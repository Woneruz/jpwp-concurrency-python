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


# slajd 13 (graceful shutdown - sygnal konca)
# slajd 14 (consumer wykrywa None - task_done + break)
# slajd 14 (tyle None ile workerow)
# slajd 14 (q.join w main)


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

    for task_id in range(1, TASK_COUNT + 1):
        task_queue.put(task_id)

    # Sygnaly konca - po jednym dla kazdego workera
    for _ in range(WORKER_COUNT):
        task_queue.put(STOP_SIGNAL)

    # Czekamy az kolejka opustoszeje
    task_queue.join()

    for thread in workers:
        thread.join()

    print("Program zakonczyl prace.")


if __name__ == "__main__":
    main()
