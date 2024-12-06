class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


# raise KeyError # KeyError
# raise MyException("") # MyException

try:
    x = int(input("Podaj liczbę calkowitą"))
    if x <= 0:
        raise MyException("Liczba musi być większa od zera")
except MyException as e:
    print("Wartość musi być większa od zera", e)
except Exception as e:
    print("Bład", e)
else:
    print("Podana wartość prawidłowa:", x)
finally:
    print("koniec")

# Podaj liczbę calkowitą-10
# Wartość musi być większa od zera Liczba musi być większa od zera
# Podaj liczbę calkowitą10
# Podana wartość prawidłowa: 10
# Podaj liczbę calkowitąa
# Bład invalid literal for int() with base 10: 'a'
# koniec
