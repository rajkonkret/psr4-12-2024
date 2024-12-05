# generator - generuje wartości w momencie kiedy je potrzebujemy

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # zwraca wynik dla danego x, zapamietuje x


kwa = kwadrat2(5)
print(kwa)  # <generator object kwadrat2 at 0x000001C4E7953510>
print(type(kwa))  # <class 'generator'>
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
# print(next(kwa)) # StopIteration koniec danych w generatorze

kwa2 = kwadrat2(10)
kwa3 = kwadrat2(10)

print(next(kwa2))
print(next(kwa2))
print(next(kwa3))
print(next(kwa2))
print(next(kwa3))
print(next(kwa2))

for i in kwadrat2(10):
    print(i)

print(list(kwa3))  # [4, 9, 16, 25, 36, 49, 64, 81]
