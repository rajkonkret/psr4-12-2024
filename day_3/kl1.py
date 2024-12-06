# klasy - szablon, przepis, matryca
# obiket - instacja klasy - element zbudowany z przepisu
# cechy i funkcje obiektu
# hermetyzacja, polimorfizm, dziedziczenie, abstrakcja
import math


class MyFirstClass:
    """
    Klasa w Pythonie opisująca punkty w przestrzeni x i y
    """

    def __init__(self, x=0, y=0):
        """
        Metoda inicjalizująca (konstruktor)
        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        """
        Metoda przesunie punkt w miejsce x, y
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calulate(self, other: "MyFirstClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):  # metoda opisująca obiekt
        return f"{self.x, self.y}"

    def __repr__(self):# reprezentacja obiektu
        return f"Point({self.x, self.y})"

print(MyFirstClass.__doc__)
# #
#     Klasa w Pythonie opisująca punkty w przestrzeni x i y
ob1 = MyFirstClass()
print(ob1.x)
print(ob1.y)
print(ob1)  # <__main__.MyFirstClass object at 0x000002529A148080>
# po nadpisaniu metody __str__
# (0, 0)
ob1.move(100, 456)
print(ob1)  # (100, 456)
ob1.reset()
print(ob1)  # (0, 0)
ob2 = MyFirstClass(45, 89)
print(ob2)  # (45, 89)
print(ob1.calulate(ob2))  # 99.72963451251589

print(ob2)  # (45, 89)
lista = [ob1, ob2]
for i in lista:
    print(i)
# (0, 0)
# (45, 89)
print(lista) # [<__main__.MyFirstClass object at 0x00000272D456A2A0>, <__main__.MyFirstClass object at 0x00000272D456AD50>]
# po nadpisaniu __repr__
# [Point((0, 0)), Point((45, 89))]