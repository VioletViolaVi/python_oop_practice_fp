from msilib.schema import Class


class Bus():

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.age = 0
        self.passengers = []

    # means we can treat .passenger_count as if it is a piece of information (commonly used in game development)
    @property
    def passenger_count(self):
        return len(self.passengers)

    def get_older(self, years):
        self.age += years

    def collect_passengers(self, name):
        self.passengers.append(name)


bus1 = Bus("Jubilee", 10)
bus2 = Bus("Vauxhall", 50)
print(bus2.name, bus2.age)

print(bus1.name, bus1.age)
bus1.get_older(37)
print(bus1.name, bus1.age)
bus1.collect_passengers("Bonnie")
bus1.collect_passengers("Steve")
bus1.collect_passengers("Holly")
print(bus1.name, bus1.passengers)
