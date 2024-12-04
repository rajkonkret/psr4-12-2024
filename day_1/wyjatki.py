# print(5 / "0")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\psr4-12-2024\day_1\wyjatki.py", line 1, in <module>
#     print(5 / "0")
#           ~~^~~~~
# TypeError: unsupported operand type(s) for /: 'int' and 'str'
# wyjątki - błedy działania programu
# należy przechwycić i obsłużyc
try:
    print("12" + 34)
except Exception as e:
    print("Bład", e)
else:
    print('Wykona się gdy nie ma błedu')
finally:
    print('Wykona się zawsze')

print("Program nadal działa")
# Bład can only concatenate str (not "int") to str
# Program nadal działa
