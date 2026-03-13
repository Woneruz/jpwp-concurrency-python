# Proste logowanie do konsoli dla projektu JPWP.

from datetime import datetime
import threading


def log_message(message: str) -> None:
    # Wyświetla komunikat z czasem i nazwą aktualnego wątku.
    current_time = datetime.now().strftime("%H:%M:%S")
    thread_name = threading.current_thread().name
    print(f"[{current_time}] [{thread_name}] {message}")