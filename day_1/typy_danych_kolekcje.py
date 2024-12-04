# kolekcja
# lista, zbiór (set), krotka (tuple), słownik

# lista - doolna ilość danych, rożnego typu na raz,
# zachowuje kolejność przy dodawaniu elementów

lista = []
lista = list()
print(lista)  # []
print(type(lista))  # <class 'list'>

lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Darek")
lista.append("Gerard")
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Darek', 'Gerard']

lista2 = lista  # kopia referencji, adresu w pamięci
lista_copy = lista.copy()
print(type(lista2))
print(lista2)  # ['Radek', 'Tomek', 'Zenek', 'Darek', 'Gerard']
lista.clear()
print(lista2)  # []
print(lista_copy)  # ['Radek', 'Tomek', 'Zenek', 'Darek', 'Gerard']
print(id(lista))
print(id(lista2))
print(id(lista_copy))
# 2404251090880
# 2404251090880
# 2404247738560

# krotka, tuple - niemutowalna kolekcja, tylko do odczytu
# pozwala lepiej zarządzać pamięcią
krotka = tuple(lista_copy)
print(krotka)  # ('Radek', 'Tomek', 'Zenek', 'Darek', 'Gerard')
print(type(krotka))  # <class 'tuple'>
krotka_liczby = 6, 7, 8, 9, 0, 0
print(type(krotka_liczby))
print(krotka_liczby)  # (6, 7, 8, 9, 0, 0)

krotka_jeden = "Radek",
print(krotka_jeden)  # ('Radek',)
# PEP8 zaleca by jednoelementowe krotki tworzyc z nawiasami
krotka_jeden = ("Radek",)
print(krotka_jeden)  # ('Radek',)

print(krotka_liczby.count(9))  # wystepuje 1 raz
print(krotka_liczby.index(9))  # indeks numer 3

# nie można zmieniac
# krotka_liczby[0] = 7 # TypeError: 'tuple' object does not support item assignment
del krotka_jeden  # usunięcie całej krotki
# print(krotka_jeden) # NameError: name 'krotka_jeden' is not defined

# rozpakownie krotki
a, b = 1, 2
print(a, b)
a, *b = 1, 2, 3  # * worek na dane
print(a, b)  # 1 [2, 3]

# zbiór (set) - nie przechowuje duplikatów
# nie posiada indeksu, nie zachowuje kolejności przy dodawaniu elementów
lista = [44, 55, 66, 77, 33, 31, 33, 55, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 11, 44, 77, 55, 31}
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(23)
zbior.add(55)
zbior.add(76)
print(zbior)  # {33, 66, 11, 44, 77, 76, 18, 23, 55, 31}

pusty_zbior = set()
print(pusty_zbior)  # set()

zbior2 = {66, 11, 44, 55, 66, 999, 999, 62}
# suma zbiorów
print(zbior | zbior2)  # {33, 66, 999, 11, 44, 77, 76, 18, 23, 55, 62, 31}
print(zbior.union(zbior2))  # {33, 66, 999, 11, 44, 77, 76, 18, 23, 55, 62, 31}

# częśc wspolna
print(zbior & zbior2)  # {66, 11, 44, 55}
print(zbior.intersection(zbior2))  # {66, 11, 44, 55}

lista = list(zbior)
print(lista)  # [33, 66, 11, 44, 77, 76, 18, 23, 55, 31]

# frozenset() - niemutowalny set
immutable_set = frozenset([1, 2, 3, 4])
print(immutable_set)  # frozenset({1, 2, 3, 4})

nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print(nested_set)  # {frozenset({3, 4}), frozenset({1, 2})}

# słownik
# para klucz-wartość
# {"name":"Radek", "age":89}
# odwzorowanie jsona w pythonie
# klucze nie mogą sie powtarzac
slownik = dict()
print(slownik)  # {} pusty słownik
slownik = {}
print(slownik)  # {}

print(type(slownik))  # <class 'dict'>

slownik['name'] = 'Radek'
slownik['age'] = 90
print(slownik)  # {'name': 'Radek', 'age': 90}

print(slownik.keys())
print(slownik.values())
print(slownik.items())
# dict_keys(['name', 'age'])
# dict_values(['Radek', 90])
# dict_items([('name', 'Radek'), ('age', 90)])

print(slownik['name'])  # Radek
# print(slownik['namE']) # KeyError: 'namE'

print(slownik.get("NAme"))  # klucza nie ma w słowniku, dostalismy None
print(slownik.get("Name", "default"))  # default

lista_duplikaty = [33, 66, 11, 45, 77, 45, 18, 55, 33, 55]
print(dict.fromkeys(lista_duplikaty))
# {33: None, 66: None, 11: None, 45: None, 77: None, 18: None, 55: None}
print(list(dict.fromkeys(lista_duplikaty)))
# [33, 66, 11, 45, 77, 18, 55], usunięte duplikaty, zachowuje kolejnosc
