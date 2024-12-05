# funkcja - fragment kodu, który możemy wywołać w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# wywołanie funkcji, uruchamia funkcje

a = 10
b = 90


# nie zwracaj wyniku
def dodaj():
    print(a + b)


def dodaj2(a, b):  # obowiazkowe argumenty a i b
    print(a + b)


# symulowanie przeciązania funkcji liczbą argumentów
def odejmij(a, b, c=0):
    print(a - b - c)


# zwraca wynik, return
# to jest podpowiedz typów
def mnozenie(a: int, b: int) -> int:
    """

    :param a:
    :param b:
    :return:
    """
    return a * b


def mnozenie2(a, b):
    return a, b, a * b


dodaj()  # 100
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(56, 89)  # 145

odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4
print(dodaj())  # None

print(mnozenie(5, 9))  # 45
wynik = mnozenie(6, 9)
print(wynik)

print(mnozenie(2.5, 6))  # 15.0

print(mnozenie2(6, 8))
# (6, 8, 48)
x, y, z = mnozenie2(6, 9)
print(f'Wynik działania {x} * {y} = {z}')
# Wynik działania 6 * 9 = 54

# argumenty po nazwie
odejmij(b=9, c=9, a=6)  # -12
odejmij(b=7, a=67)  # 60

# mieszane
odejmij(1, c=9, b=89)  # -97

# najpierw muszą byc pozycyjne
# odejmij(c=9, 1, 2)  # SyntaxError: positional argument follows keyword argument

# print(dodaj() + dodaj2(5, 7)) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
print(mnozenie(89, 76) + mnozenie(6, 8))  # 6812
