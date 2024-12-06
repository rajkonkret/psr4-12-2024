# wielodziedziczenie
class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(B, A):
    """
    Klasa dziedziczy po klasie A i B
    """


a = A()
a.method()
b = B()
b.method()

c = C()
c.method()  # Metoda z klasy B

print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


class D(A, B):
    """
    Dziedziczy po A i B
    """


d = D()
d.method()  # Metoda z klasy A
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


class E(A, B):
    def method(self):
        print("Metoda z klasy E")


e = E()
e.method()  # Metoda z klasy E
print(E.__mro__)  # (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


class F(A, B):
    def method(self):
        B.method(self)  # Metoda z klasy B


f = F()
f.method()


class G(A, B):
    def method(self):
        super().method()
        # super() - klasa nadrzędna, mozna wywołać
        print("Dopisane")


g = G()
g.method()
# Metoda z klasy A
# Dopisane
print(G.__mro__)  # (<class '__main__.G'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


class H(A, B):
    def method(self):
        super().method()

    def method_B(self):
        B.method(self)
        print("Dopisane")
