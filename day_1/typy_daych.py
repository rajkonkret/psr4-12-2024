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
