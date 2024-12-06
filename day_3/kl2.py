class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f"{self.name} {self.email}"


class Suplier(Contact):
    """
    Klasa Suplier dziedziczy po klasie Contct
    """

    def __init__(self, name, email, phone="000000000"):
        super().__init__(name, email)  # obowiązkowo musimy wywołać konstruktor klasy wyzszej super()
        self.phone = phone

    def order(self, order):
        print(f'{order} zamówienie od {self.name}')

    def __repr__(self):
        return f"{self.name} {self.email} +48{self.phone}"


c1 = Contact("Adam", "admin@wp.pl")
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1)
print(c1.all_contacts)
print(c3.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(Contact.all_contacts)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]

s1 = Suplier("Marek", "marek@o2.pl")
print(s1)
print(s1.all_contacts)
# Marek marek@o2.pl
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@o2.pl]
s2 = Suplier("Zenek", "zenek@wp.pl", "567890123")
print(s2)  # Zenek zenek@wp.pl +48567890123
print(s2.all_contacts)
# [Adam admin@wp.pl,
# Radek radek@wp.pl,
# Tomek tomek@wp.pl,
# Marek marek@o2.pl +48000000000,
# Zenek zenek@wp.pl +48567890123]
s3 = Suplier("Marta", "marta@wp,pl", "321456789")
s3.order("kawa")  # kawa zamówienie od Marta
