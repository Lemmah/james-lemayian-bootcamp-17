#!/usr/bin/env python
# encoding: utf-8

class Domestic_Animals(object): # Application of class oop concept
	def __init__(self, name, species): 
		self.name = 'Domestic Animal'
		self.species = 'Mammal'

class Cow(Domestic_Animals): # Inheritance
	__byproduct = 'Beef' # Encapsulation

	def description(self, animal_name, number_of_legs, sound):
		self.animal_name = 'Cow'
		self.number_of_legs = 4
		self.sound = 'Moow'
		print('I am a %s' % (animal_name))

class Chicken(Domestic_Animals):
	__byproduct = 'Eggs' 

	def description(self, animal_name, number_of_legs, sound):
		self.animal_name = 'Chicken'
		self.number_of_legs = 2
		self.sound = 'Crock'
		print('I am a %s' % (animal_name))


def get_description(self): # Polymorphism demonstrated
	return self.description()
	
