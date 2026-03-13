"""Definicja wątku producenta."""

import threading
import time
from queue import Queue

from logger import log_message
from shared_resources import Task


class ProducerThread(threading.Thread):
    # Wątek odpowiedzialny za generowanie zadań.

    def __init__(
        self,
        producer_id: int,
        task_queue: Queue,
        number_of_tasks: int,
        delay: float = 0.4,
    ) -> None:
        super().__init__(name=f"Producer-{producer_id}")
        self.producer_id = producer_id
        self.task_queue = task_queue
        self.number_of_tasks = number_of_tasks
        self.delay = delay

    def run(self) -> None:
        # Generuje zadania i dodaje je do wspólnej kolejki.
        for local_task_number in range(1, self.number_of_tasks + 1):
            task = Task(
                task_id=self.producer_id * 100 + local_task_number,
                producer_name=self.name,
                description=f"Zdarzenie {local_task_number} od {self.name}",
            )

            self.task_queue.put(task)
            log_message(
                f"Dodano do kolejki zadanie id={task.task_id}: {task.description}"
            )
            time.sleep(self.delay)

        log_message("Zakończono generowanie zadań.")