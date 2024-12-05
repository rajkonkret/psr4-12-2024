# dekorator - funkcja, która jako argument przyjmuje funkcję
# dodaje, modyfikuje
# wykorzystuje mechanizm funkcji wewnętrznej
def dekor(fun):
    def wew():
        print("Dekorator. Dodatkowy napis")
        return fun()

    return wew

@dekor
def nasza_funkcja():
    print("Funkcja do udekorowania")


nasza_funkcja()  # Funkcja do udekorowania

# po uzyciu dekoratora
# Dekorator. Dodatkowy napis
# Funkcja do udekorowania