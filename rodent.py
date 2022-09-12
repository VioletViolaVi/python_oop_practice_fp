class Rodent():

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def bite(self, target):
        print(f"{self.name} chomps on the {target}")


class FlyingSquirrel(Rodent):

    scientific_name = "Flyus Squirrelus"

    # @staticmethod # use if you want to pass in more info # or...
    # @classmethod # also needs a 'cls' (cls is convention) passed through as param
    # @property
    def get_most_common_habitat(cls):
        return "South America"

    def __init__(self, name):
        super().__init__(name, "Flying Squirrel")

    # these are instance methods
    def glide(self, distance):
        print(f"{self.name} soars for {distance} miles through the air.")


wilbur = Rodent("Wilbur", "mole")
clarice = Rodent("Clarice", "capybara")
natalie = FlyingSquirrel("Natalie")

wilbur.bite("worm")
clarice.bite("shrub")
natalie.bite("wood")
natalie.glide(300)
print(natalie.get_most_common_habitat)
