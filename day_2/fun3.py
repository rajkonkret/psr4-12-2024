# lambda - skrócony zapis funkcji
# podstawowym zastosowaniem lambdy jest funkcja anonimowa
# mozłiwość uzycia w miejscu deklaracji
# lambda ma return
from functools import reduce, lru_cache


def liczymy(x, y):
    return x * y


print(liczymy(56, 90))  # 5040
liczymy2 = lambda x, y: x * y
print(liczymy2(9, 7))  # 63

# mapowanie danych
lista = [1, 2, 6, 15, 67, 78, 90, 100, 200]

lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)

print(lista_wyn)  # [2, 4, 12, 30, 134, 156, 180, 200, 400]

print([i * 2 for i in lista])  # [2, 4, 12, 30, 134, 156, 180, 200, 400]


def zmien(x):
    return x * 2


for i in lista:
    lista_wyn.append(zmien(i))

print(lista_wyn)
# [2, 4, 12, 30, 134, 156, 180, 200, 400, 2, 4, 12, 30, 134, 156, 180, 200, 400]

# funkcja wyzszego rzedu
# map()
print(f"Zastosowanie map: {list(map(zmien, lista))}")
# Zastosowanie map: [2, 4, 12, 30, 134, 156, 180, 200, 400]

# zastosowanie lambdy jako funkcja anonimowa
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map: {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map: {list(map(lambda x: x * 3, lista))}")
print(f"Zastosowanie map: {list(map(lambda x: x * 12, lista))}")
# Zastosowanie map: [2, 4, 12, 30, 134, 156, 180, 200, 400]
# Zastosowanie map: [2, 4, 12, 30, 134, 156, 180, 200, 400]
# Zastosowanie map: [4, 8, 24, 60, 268, 312, 360, 400, 800]
# Zastosowanie map: [3, 6, 18, 45, 201, 234, 270, 300, 600]
# Zastosowanie map: [12, 24, 72, 180, 804, 936, 1080, 1200, 2400]


# filtrowanie danych
for i in lista:
    if i < 10:
        print(i)

# filter() - filtruje dane, zwraca spęłniające warunek

print(f"Uzycie filter() {list(filter(lambda x: x < 10, lista))}")  # Uzycie filter() [1, 2, 6]
print(f"Uzycie filter() {list(filter(lambda x: x < 1, lista))}")  # Uzycie filter() []
print(f"Uzycie filter() {list(filter(lambda x: x > 50, lista))}")  # Uzycie filter() [67, 78, 90, 100, 200]
print(f"Uzycie filter() {list(filter(lambda x: x < 10, lista))}")  # Uzycie filter() [1, 2, 6]
print(f"Uzycie filter() {list(filter(lambda x: x > 10 and x < 200, lista))}")  # Uzycie filter() [15, 67, 78, 90, 100]
print(f"Uzycie filter() {list(filter(lambda x: 10 < x < 200, lista))}")  # Uzycie filter() [15, 67, 78, 90, 100]

# reduce()
"""
    reduce(function, iterable[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of an iterable, from left to right.

    This effectively reduces the iterable to a single value.  If initial is present,
    it is placed before the items of the iterable in the calculation, and serves as
    a default when the iterable is empty.

    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
    calculates ((((1 + 2) + 3) + 4) + 5).
    """
liczby = [1, 2, 3, 4, 5]
wynik = reduce(lambda a, b: a + b, liczby)
print("Wynik reduce", wynik)  # Wynik reduce 15, ((((1 + 2) + 3) + 4) + 5).

wynik_mn = reduce(lambda a, b: a * b, liczby)
print("Wynik reduce, mnozenie", wynik_mn)  # Wynik reduce, mnozenie 120, ((((1 * 2) * 3) * 4) * 5)


@lru_cache(maxsize=1000)
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


print(fib_cached(10))  # 55
print(fib_cached.cache_info())
# CacheInfo(hits=8, misses=11, maxsize=1000, currsize=11)
print(fib_cached(5))
print(fib_cached.cache_info())  # CacheInfo(hits=9, misses=11, maxsize=1000, currsize=11)
# hits - ile razy uzyskał wynik nie musząc wykonać obliczeń
# misses - ile razy wykonał obliczenia
fib_cached.cache_clear()
print(fib_cached.cache_info())  # CacheInfo(hits=0, misses=0, maxsize=1000, currsize=0)

r0 = {'miasto': "Kielce"}
r1 = {'miasto': "Kielce", "ZIP": "25-900"}

print(r0['miasto'])
print(r1['miasto'])
# Kielce
# Kielce

print(r1["ZIP"])  # 25-900
# print(r0["ZIP"])  # KeyError: 'ZIP'

print(r0.get("ZIP", "00-000"))  # 00-000

d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))
# 00-000
# 25-900
print(r0)
print(r1)
# {'miasto': 'Kielce', 'ZIP': '00-000'}
# {'miasto': 'Kielce', 'ZIP': '25-900'}
