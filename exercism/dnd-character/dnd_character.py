import random
import math

def modifier(constitution_score):
	score = ((constitution_score - 10) // 2 )
	return score


class Character:

	def __init__(self):
		self.strength = self.ability()
		self.dexterity = self.ability()
		self.constitution = self.ability()
		self.intelligence = self.ability()
		self.wisdom = self.ability()
		self.charisma = self.ability()
		self.hitpoints = 10 + modifier(self.constitution)

	def ability(self):
		result = []
		for e in range(0,4):
			a = random.randint(1,6)
			result.append(a)
		result.sort()
		return sum(result[1:])


