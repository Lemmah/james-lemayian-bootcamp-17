#!/usr/bin/env python
# encoding: utf-8


class Domestic_Animals:  # Application of class oop concept
    # Corrected, hardcoded values by assigning default values instead.
    def __init__(self, name='Domestic_Animal', species='Mammal'):
        self.name = name
        self.species = species

    def description(self):
        # Just seeing that this class function is inherited
        return 'This is a {} from the {} species'.format(self.name, self.species)


class Cow(Domestic_Animals):  # Inheritance
    def __init__(self, name = 'Cow', species, number_of_legs, sound):
        super().__init__(name, species)
        self.number_of_legs = number_of_legs
        self.sound = sound
        __byproduct = 'Beef'


print(Domestic_Animals('Cow', 'Mammal').description())
print(Cow('Cow', 'Mammal', 4, 'Moow').description())
