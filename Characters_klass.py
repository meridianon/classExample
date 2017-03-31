import random 
class Character(object):
	"""docstring for Character"""
	hand = ["right","left"]
	head = True 
	Leg = ["right","left"]
	hp = 5000
	# def __init__(self):
	#  	HP = self.hp
	def delteAtr(self):
		t = random.choice(self.hand)
		print("Delete 1 hand", t)
	def Hit(self,weapon):
		if weapon == "Knife" or weapon == "Pistol" or weapon == "Hammer": 
			self.hp -=30
			self.delteAtr()
		elif weapon == "Fist":
			self.hp -=10
		print("Characters hit:",self.hp,"damage")


class Weapon(object):
	"""docstring for Weapon"""
	Weapons = ["Knife","Pistol","Hammer", "Fist"]
	def __init__(self):
		weap = random.choice(self.Weapons) 
		print("Your weapon:",weap)