# walrus operator -> operator morsa
# :=

name = "Radek"
if name == "Radek":
    print("Radek")

if name := "Radek":
    print("Radek")

tekst = "Radek Radek"
a = len(tekst)
if a > 3:
    print(tekst, a)

if (a := len(tekst)) > 3:
    print(tekst, a)  # Radek Radek 11
