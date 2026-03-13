# Wspólne zasoby i struktury danych używane przez wiele wątków.

from dataclasses import dataclass
from queue import Queue


@dataclass(frozen=True)
class Task:
    # Pojedyncze zadanie przekazywane między wątkami.
    task_id: int
    producer_name: str
    description: str


STOP_SIGNAL = None


def create_task_queue() -> Queue:
    # Tworzy współdzieloną kolejkę zadań.
    return Queue()