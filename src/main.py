# Główny plik uruchamiający demonstrację współbieżności i wielowątkowości.

from logger import log_message
from producers import ProducerThread
from shared_resources import STOP_SIGNAL, create_task_queue
from workers import WorkerThread

NUMBER_OF_PRODUCERS = 2
NUMBER_OF_WORKERS = 2
TASKS_PER_PRODUCER = 4


def main() -> None:

    # Uruchamia prostą demonstrację producentów i workerów.

    log_message("Start programu.")

    task_queue = create_task_queue()

    producers = [
        ProducerThread(
            producer_id=producer_number,
            task_queue=task_queue,
            number_of_tasks=TASKS_PER_PRODUCER,
        )
        for producer_number in range(1, NUMBER_OF_PRODUCERS + 1)
    ]

    workers = [
        WorkerThread(worker_id=worker_number, task_queue=task_queue)
        for worker_number in range(1, NUMBER_OF_WORKERS + 1)
    ]

    for worker in workers:
        worker.start()

    for producer in producers:
        producer.start()

    for producer in producers:
        producer.join()

    log_message("Wszyscy producenci zakończyli pracę.")

    for _ in workers:
        task_queue.put(STOP_SIGNAL)

    task_queue.join()

    for worker in workers:
        worker.join()

    log_message("Wszyscy workerzy zakończyli pracę.")
    log_message("Koniec programu.")


if __name__ == "__main__":
    main()