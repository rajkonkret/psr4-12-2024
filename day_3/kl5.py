class Boat:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__speed = 0  # pole prywatne, zahermetyzowane

    def sail(self):
        self.__speed += 10

    def speedometer(self):
        print(f"Prędkość wynosi {self.__speed} knots")


boat = Boat("Sportina", 2024)
boat.sail()
boat.sail()
boat.sail()
boat.sail()
boat.sail()
# print(boat.__speed)  # 50, AttributeError: 'Boat' object has no attribute '__speed'
boat.speedometer()  # Prędkość wynosi 50 knots
boat.__speed = 10  # pole globalne o tej samej nazwie
boat.speedometer()
# enkapsulacja - hermetyzowanie pól, wystawianie deedykowanych metod do odczytu i zapisu tych pól
