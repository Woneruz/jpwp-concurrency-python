# Współbieżność i wielowątkowość w Pythonie

**Mateusz Maślanka, Arkadiusz Baran** | AGH Akademia Górniczo-Hutnicza | Teleinformatyka | JPWP

Repozytorium do projektu z przedmiotu JPWP poświęconego współbieżności i wielowątkowości w Pythonie - od podstaw modułu `threading`, przez synchronizację i komunikację między wątkami, aż po `ThreadPoolExecutor` z `concurrent.futures`.

---

## Zawartość repozytorium

| Katalog | Opis |
|---|---|
| `zadania/` | 7 zadań praktycznych do samodzielnego uzupełnienia |
| `solutions/` | Rozwiązania zadań (TBA) |
| `quiz/` | Pytania teoretyczne sprawdzające zrozumienie tematu |

---

## Zadania

| # | Plik | Temat |
|---|---|---|
| 1 | `zadania/zadanie_1.py` | Race condition - wyścig na wspólnym liczniku |
| 2 | `zadania/zadanie_2.py` | Synchronizacja listy i licznika jednym lockiem |
| 3 | `zadania/zadanie_3.py` | `queue.Queue` - producer-consumer z `task_done()` i `join()` |
| 4 | `zadania/zadanie_4.py` | Wzorzec producer-consumer z wieloma workerami |
| 5 | `zadania/zadanie_5.py` | Graceful shutdown - sygnał `STOP` kończący workery |
| 6 | `zadania/zadanie_6.py` | Deadlock - odtworzenie i naprawa zakleszczenia |
| 7 | `zadania/zadanie_7.py` | `ThreadPoolExecutor` - pula wątków z `concurrent.futures` |

---

## Prezentacja

[Wspolbieznosc_Prezentacja.pdf](Wspolbieznosc_Prezentacja.pdf)

Prezentacja liczy 27 slajdów i obejmuje następujące zagadnienia:

| # | Temat | Opis |
|---|---|---|
| 01 | **Współbieżność vs równoległość** | różnica między naprzemiennym wykonaniem a prawdziwą równoległością |
| 02 | **Wątki, procesy i GIL** | ograniczenia CPython; kiedy wątki pomagają, a kiedy nie |
| 03 | **Tworzenie wątków i ich cykl życia** | `threading.Thread`, stany wątku NEW -> RUNNING -> TERMINATED |
| 04 | **Race condition i synchronizacja** | problem wyścigu, `threading.Lock`, sekcja krytyczna |
| 05 | **Komunikacja przez Queue** | wzorzec producer-consumer, graceful shutdown |
| 06 | **Deadlock i antypatterns** | przyczyny zakleszczenia, naprawa i 5 typowych błędów |
| 07 | **ThreadPoolExecutor** | `concurrent.futures`, obiekt `Future`, `submit()`, `map()` |
| 08 | **Case study i benchmarki** | serwer TCP, porównanie wątki vs procesy vs sekwencyjnie |

---

## Źródła

- Dokumentacja Python - `threading`, `queue`, `concurrent.futures`: https://docs.python.org/3/library/threading.html
- Real Python - *An Intro to Threading in Python*: https://realpython.com/intro-to-python-threading
