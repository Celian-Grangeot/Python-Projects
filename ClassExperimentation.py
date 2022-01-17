class vehicule:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def details(self):
        return (self.name + " " + self.color + " " + str(self.year))


class bus(vehicule):
    pass

Honda = vehicule("Honda", "red", 1999)
print(Honda.details())

schoolbus = bus("Mercedes", "Yellow", 2014)
print(schoolbus.details())