for i in range(10):  # od 0 do 9
    print(i)

for i in range(1, 10, 2):  # start, stop, krok
    print(i)

for i in range(10):
    for j in range(10):
        print(f"{i} + {j} = {i + j}")
# 9 + 6 = 15
# 9 + 7 = 16
# 9 + 8 = 17
# 9 + 9 = 18

# list comprehensions
lista2 = [j for j in range(10)]
print(lista2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for c in lista2:
    print(c)

# petla while - sterowana warunkiem
licznik = 0
while licznik < 10:
    licznik += 1
    print(licznik)

print(licznik)  # 10

lista2.append(55)
lista2.append(55)
lista2.append(55)
print(lista2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 55, 55, 55]
while 55 in lista2:
    lista2.remove(55)
print(lista2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# warunki
logiczna = True
logiczna = ""
if logiczna:
    print("Prawda")
    print("Prawda")
    print("Prawda")
    print("Prawda")
else:
    print("Fałsz")

odp = "Raadek"
if odp == "Radek":
    print("Radek")
elif odp == "Tomek":
    print("Tomek")
else:
    print("Nie znam Cię")
# Nie znam Cię

# od pythona 3.10
# match case

odp = input("Podaj imię")  # odczytuje dane, str

match odp.casefold().capitalize().strip():
    case "Radek":
        print("Ok")
    case "Tomek":
        print("Ok")
    case _:  # odpowiednik else
        print("Nie znam")

# Podaj imięradek
# Ok
