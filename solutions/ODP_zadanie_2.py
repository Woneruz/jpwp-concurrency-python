"""
Zadanie 2: Synchronizacja dostepu do wspolnej listy
Kilka watkow zapisuje komunikaty do tej samej listy. Dodatkowo program zlicza,
ile komunikatow zostalo dodanych. Lista i licznik powinny byc zmieniane jako
jedna sekcja krytyczna.
Uzupelnij kod tak, aby kazdy zapis do wspolnych danych byl chroniony przez threading.Lock.
Oczekiwany efekt:
Program wypisuje liczbe komunikatow rowna EXPECTED_MESSAGES i nie gubi zadnych
zapisow.
"""

import threading
import time


THREAD_COUNT = 4
MESSAGES_PER_THREAD = 5
EXPECTED_MESSAGES = THREAD_COUNT * MESSAGES_PER_THREAD

messages: list[str] = []
saved_messages = 0
# Do zrobienia: Utworz lock dla wspolnych danych messages i saved_messages.


def save_messages(worker_id: int) -> None:
    global saved_messages

    for message_number in range(1, MESSAGES_PER_THREAD + 1):
        time.sleep(0.05)
        message = f"Worker {worker_id}: komunikat {message_number}"

        # Do zrobienia: Zabezpiecz ponizsze dwie operacje jedna blokada.
        messages.append(message)
        saved_messages += 1


def main() -> None:
    threads = [
        threading.Thread(target=save_messages, args=(worker_id,))
        for worker_id in range(1, THREAD_COUNT + 1)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Zapisane komunikaty: {saved_messages}")
    print(f"Dlugosc listy: {len(messages)}")
    print(f"Oczekiwano: {EXPECTED_MESSAGES}")


if __name__ == "__main__":
    main()
