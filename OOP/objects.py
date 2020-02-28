

# parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg


class Human(Organism):
    name = "Dave"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth"

    def daveiscool(self):
        msg = "\nDave is super cool, I like Dave, nice guy."
        return msg


class Dog(Organism):
    name = "Roxy"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bark(self):
        msg = "\nBark BArk bark bark bark bark ruff"
        return msg


class Bacteria(Organism):
    name = "CoranaVirus"
    species = "Deadly Flu"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "China"

    def cough(self):
        msg = "\nCough cough cough cough cough cough cough\ncough cough cough cough cough!"
        return msg


if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.daveiscool())

    dog = Dog()
    print(dog.information())
    print(dog.bark())

    bact = Bacteria()
    print(bact.information())
    print(bact.cough())