"""Definicja wątku roboczego przetwarzającego zadania."""

import threading
import time
from queue import Queue

from logger import log_message
from shared_resources import STOP_SIGNAL, Task


class WorkerThread(threading.Thread):
    """Wątek pobierający zadania z kolejki i je przetwarzający."""

    def __init__(
        self,
        worker_id: int,
        task_queue: Queue,
        processing_time: float = 0.8,
    ) -> None:
        super().__init__(name=f"Worker-{worker_id}")
        self.worker_id = worker_id
        self.task_queue = task_queue
        self.processing_time = processing_time

    def run(self) -> None:
        """Pobiera zadania z kolejki aż do otrzymania sygnału stop."""
        while True:
            task = self.task_queue.get()

            if task is STOP_SIGNAL:
                log_message("Otrzymano sygnał STOP. Kończenie pracy.")
                self.task_queue.task_done()
                break

            log_message(
                f"Rozpoczęto przetwarzanie zadania id={task.task_id} "
                f"({task.description})"
            )
            time.sleep(self.processing_time)
            log_message(f"Zakończono zadanie id={task.task_id}")

            self.task_queue.task_done()