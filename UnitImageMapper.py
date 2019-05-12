from Unit import *


class UnitImageMapper:
	@staticmethod
	def get_path_to_image(unit):
		if isinstance(unit, BritishSwordsman):
			return "img/british_swordsman.png"
		if isinstance(unit, FrenchSwordsman):
			return "img/french_swordsman.png"
		if isinstance(unit, BritishArcher):
			return "img/british_archer.png"
		if isinstance(unit, FrenchArcher):
			return "img/french_archer.png"
		if isinstance(unit, BritishCavalry):
			return "img/british_horseman.png"
		if isinstance(unit, FrenchCavalry):
			return "img/french_horseman.png"

	@staticmethod
	def get_path_to_stroke_image(unit):
		if isinstance(unit, Swordsman):
			return "img/swordsman_stroke.png"
		if isinstance(unit, Archer):
			return "img/archer_stroke.png"
		if isinstance(unit, Cavalry):
			return "img/horseman_stroke.png"
