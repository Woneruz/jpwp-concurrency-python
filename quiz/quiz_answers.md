# Test ABCD - Współbieżność w Pythonie - Odpowiedzi
---

## Pytanie 1 - pojedynczy wybór

**Który z opisów najlepiej oddaje różnicę między współbieżnością a równoległością?**

a) Współbieżność i równoległość to synonimy - oba oznaczają wykonywanie zadań dokładnie w tym samym momencie

b) Współbieżność wymaga wielu rdzeni CPU, a równoległość może działać na jednym rdzeniu

c) Współbieżność to zarządzanie wieloma zadaniami naraz (przełączanie kontekstu), a równoległość to ich faktyczne jednoczesne wykonywanie na wielu rdzeniach

d) Współbieżność działa tylko w językach kompilowanych, a równoległość tylko w interpretowanych

**Poprawna odpowiedź: c**

> *Wyjaśnienie:* Współbieżność (concurrency) to model, w którym zadania są przeplatane w czasie - mogą dzielić jeden rdzeń. Równoległość (parallelism) wymaga fizycznie wielu rdzeni i faktycznego wykonywania kilku zadań w tej samej chwili. Program może być współbieżny bez bycia równoległym.

---

## Pytanie 2 - wielokrotny wybór

**Które stwierdzenia o `threading.Lock` są prawdziwe? (zaznacz wszystkie poprawne)**

a) Lock zapewnia, że tylko jeden wątek naraz wykonuje kod w sekcji krytycznej

b) Konstrukcja `with lock:` gwarantuje zwolnienie blokady nawet jeśli w środku wystąpi wyjątek

c) Lock automatycznie wykrywa deadlock i przerywa jeden z wątków

d) Zwykły `Lock` jest *reentrant* - ten sam wątek może go zablokować wielokrotnie bez zakleszczenia

**Poprawne odpowiedzi: a, b**

> *Wyjaśnienie:*
> - **a** - to definicja Locka
> - **b** - menedżer kontekstu `with` woła `release()` w bloku `finally`
> - **c** - Python nie wykrywa deadlocków automatycznie; trzeba im zapobiegać (stała kolejność, timeout)
> - **d** - zwykły `Lock` **nie jest** reentrant. Ponowne `acquire()` z tego samego wątku zakleszczy go. Do rekurencji służy `RLock`

---

## Pytanie 3 - wielokrotny wybór

**Które stwierdzenia o `queue.Queue` są prawdziwe?**

a) `queue.Queue` jest wątkowo bezpieczna "z pudełka" - nie trzeba jej owijać w `Lock`

b) `put()` blokuje wątek, gdy kolejka jest pełna (przy ustawionym `maxsize`)

c) `task_done()` sygnalizuje kolejce, że pobrany element został w pełni przetworzony

d) `queue.Queue` jest strukturą LIFO - ostatni element włożony jest pierwszy do pobrania

**Poprawne odpowiedzi: a, b, c**

> *Wyjaśnienie:*
> - **a** - wszystkie operacje na `Queue` są wewnętrznie synchronizowane
> - **b** - `put()` blokuje do momentu, aż ktoś zrobi miejsce `get()`-em
> - **c** - razem z `join()` pozwala producentowi czekać aż wszystko zostanie przetworzone
> - **d** - `queue.Queue` jest **FIFO** (First In, First Out). Do LIFO służy `queue.LifoQueue`, a do kolejki priorytetowej `queue.PriorityQueue`

---

## Pytanie 4 - pojedynczy wybór

**Wątek 1 próbuje zdobyć blokady w kolejności `lock_A -> lock_B`, a wątek 2 w kolejności `lock_B -> lock_A`. Co się stanie?**

a) Program wykona się szybciej, bo wątki pracują na różnych zasobach

b) Może wystąpić *deadlock* - oba wątki będą wzajemnie czekać na siebie w nieskończoność

c) Python automatycznie wykryje problem i przerwie jeden z wątków rzucając wyjątek

d) `threading.Lock` jest na tyle inteligentny, że sam zapobiegnie zakleszczeniu

**Poprawna odpowiedź: b**

> *Wyjaśnienie:* To klasyczny scenariusz deadlocka. Jeśli wątek 1 zdobędzie `lock_A` a wątek 2 w tym samym momencie `lock_B`, każdy będzie czekał na drugą blokadę, której ten drugi nie zwolni. Python **nie** wykrywa deadlocków - programista musi im zapobiegać (ustalając jedną, stałą kolejność akwizycji blokad we wszystkich wątkach albo stosując `acquire(timeout=...)`).

---

## Pytanie 5 - pojedynczy wybór

**Masz program, który wykonuje intensywne obliczenia numeryczne (CPU-bound). Które rozwiązanie da najlepsze przyspieszenie na maszynie wielordzeniowej?**

a) `threading.Thread` - klasyczne wątki systemowe

b) `concurrent.futures.ThreadPoolExecutor` - pula wątków

c) `multiprocessing.Process` - procesy systemowe

d) `asyncio` - programowanie asynchroniczne z event loopem

**Poprawna odpowiedź: c**

> *Wyjaśnienie:* GIL (Global Interpreter Lock) w CPython zapobiega równoczesnemu wykonywaniu bytecode'u Pythona przez wiele wątków - **dlatego wątki nie przyspieszają zadań CPU-bound**, niezależnie czy używasz `threading` czy `ThreadPoolExecutor`. `asyncio` jest przeznaczony do zadań I/O-bound (sieć, pliki), nie obliczeń.
>
> **Procesy** z modułu `multiprocessing` omijają GIL, bo każdy proces ma **własny interpreter Pythona i własny GIL** - mogą faktycznie działać równolegle na różnych rdzeniach CPU.

---
