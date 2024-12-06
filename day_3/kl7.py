class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print("Kolor", self.kolor)


class Samochod(Pojazd):
    def __init__(self, kolor, marka):
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        super().info()
        print('Marka', self.marka)


poj = Pojazd("czerwony")
sam = Samochod("zielony", "Ferrari")

lista = [poj, sam]

# obiekty róznych kals mają wspólną metodę wynikajaća z klasy głównej
# można w  tym zakresie traktowac je jako obiekty tej samej klasy
# polimorfizm
for i in lista:
    i.info()
