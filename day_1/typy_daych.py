import sys

print("Nazywam się Radek")
print('Nazywam się Radek')
# Nazywam się Radek
# Nazywam się Radek
# ctrl / - komentarz
print(type("Radek"))  # <class 'str'>, string, tekstowe

print(39)
print(type(39))  # <class 'int'>, liczba całkowita
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)
print("93")
print(type("93"))

print("93" + "93")  # konkatenacja, łaczennie stringów, 9393
print(93 + 93)  # 186
print(5 * "98")  # 9898989898
print(5 * "*")  # *****

# silne typowanie - nie zamimenia typów danych
# print("93" + 93) # TypeError: can only concatenate str (not "int") to str

print(int("93") + 93)  # int() - rzutowanie, zamiana na int, 186
print("93" + str(93))  # 9393, str() - rzutowani, zamiana na str

# zmienna - pudełko na dane, przechowuje jedną wartość
# PEP8 zaleca z małej litery, snake_case
# nazwa powinna podpowiadac co przechowuje

# typowanie dynamiczne
name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>

name = 90
print(name)  # 90
print(type(name))  # <class 'int'>

# to są podpowiedzi typów !!!
name: str = "Tomek"
print(name)  # Tomek
name = 90
print(name)  # 90

wiek = 47
rok = 2024
temp = 36.6
print(type(temp))  # <class 'float'>, liczby zmiennoprzecinkowe
print(temp)  # 36.6
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(0.1 + 0.5)  # 0.6
print(0.1 + 0.7)  # 0.7999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.4)  # 0.5
# float - bład zaokrąglenia
# For
# example, in a
# floating - point
# arithmetic
# with five base-ten digits, the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal - typ danych do przechowywania pieniedzy, omija problem zaokrąglenia

print(wiek + rok)  # 2071
print(wiek - rok)  # -1977
print(wiek * rok)  # 95128
print(wiek / rok)  # 0.023221343873517788
# ctrl d - powielanie linii

print(rok // wiek)  # cześć całkowita dzielenia, 43
print(rok % wiek)  # modulo, reszta z dzielenia, 3
print(10 % 3)  # 3 całe, reszta 1

print(wiek ** rok)  # potęgowanie
print(len(str(wiek ** rok)))  # 3385 długość
# print(wiek ** rok ** 2)
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(50 - 5 * 43 / 2 + 4 / 2)  # -55.5
print(50 - 5 * 43 / (2 + 4) / 2)  # 32.08333333333333

wersja = 3.90001
# f - fstring, sformatowany tekst
print(f"Uzywamy wersji Pythona {wersja}")  # Uzywamy wersji Pythona 3.90001
print(f"Uzywamy wersji Pythona {wersja:.1f}")  # Uzywamy wersji Pythona 3.9
print(f"Uzywamy wersji Pythona {wersja:.2f}")  # Uzywamy wersji Pythona 3.90
print(f"Uzywamy wersji Pythona {wersja:.0f}")  # Uzywamy wersji Pythona 4 zaokrągla
print("Wersja", wersja)  # Wersja 3.90001

wersja_zaokrąglona = round(wersja)
print("Zaokrąglone", wersja_zaokrąglona)  # Zaokrąglone 4

liczba = 3.8676
print(round(liczba, 2))  # 3.87
print(f"{wersja:^25}")# "         3.90001         "
print(f"{wersja:<25}")# "3.90001                  "
print(f"{wersja:>25}")# "                  3.90001"
print(f"{wersja:.>25}")# "..................3.90001"

# ten sposób weryfikuje typr
print("Uzywamy %f" % wersja) # Uzywamy 3.900010
print("Uzywamy %s" % wersja) # Uzywamy 3.900010
# print("Uzywamy %d" % "Radek") # TypeError: %d format: a real number is required, not str
