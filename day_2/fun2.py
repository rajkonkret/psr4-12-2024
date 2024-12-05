# funkcja wewnętrzna
# dekorator - fukcja która jako argument przyjmie inną funkcje i dodaje nową funkcjonalność do niej
# wykorzystuje zasady funkcji wew
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun 2")

    return fun2


fun1()
print(fun1())  # <function fun1.<locals>.fun2 at 0x000001C3C7C95BC0>
print(type(fun1()))  # <class 'function'>
funkcja = fun1()
funkcja()  # To jest fun 2


# arg - zapis, odczyt
def plik(arg):
    print("Sprawdzam czy plik istnieje")

    def zapis():
        print("Zapisałem do pliku")

    def odczyt():
        print("Odczytałem z pliku")

    if arg == 'zapis':
        return zapis  # zwracamy adres funkcji
    else:
        return odczyt


zapis_pliku = plik('zapis')
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()
odczyt_pliku = plik("odczyt")
odczyt_pliku()
# Sprawdzam czy plik istnieje
# Zapisałem do pliku
# Zapisałem do plikumo
# Zapisałem do pliku
# Zapisałem do pliku
# Zapisałem do pliku
# Sprawdzam czy plik istnieje
# Odczytałem z pliku

fh = open('test.txt', 'w')
fh.write("Zapisano\n")
fh.close()
