import random, time
import timefunct
class Character(object):
	"""docstring for Character"""
	hand = ["right","left"]
	head = True 
	Leg = ["right","left"]
	hp = 5000
	# def __init__(self):
	#  	HP = self.hp
	def delteAtr(self):
		print(self.hand)
		del self.hand[0]
		if not self.hand:
			return ""
		else:
			return self.hand[0]
	def Imposedebaf(self,arg):
		if (arg == "Knife"):
			if not self.hand:
				print("You dont have hand")
			else:
				dh = self.delteAtr()
				if not dh:
					print("You dont have hand")
				else:
					print("You have only", dh,"hand")
		elif arg == "Hammer":
			t = self.head
			t = False
			print("You contusion")
		else:
			print("You injured")
			if self.hp < 0:
				self.printGameOver()
			else:
				k = 0
				i = 0
				while 1:
					if k == 10:
						break
					else:
						k+=1
						time.sleep(0.1)
						self.hp -= 20
						if self.hp < 0:
							self.printGameOver()
						else:
							print("You loos:", self.hp, "Hp") #- 200 hp with 10 sec
	def Hit(self,weapon):
		if self.hp <0:
			self.printGameOver()
		else:
			if weapon != "Fist": 
				self.hp -=30
				self.Imposedebaf(weapon)
			else:
				self.hp -=10
			if self.hp < 0:
				self.printGameOver()
			else:
				print("Characters :", self.hp ,"damage")
		#sravnenie
	def printGameOver(self):
			print("You died")
			print("GAME OVER")

class Weapon(object):
	"""docstring for Weapon"""
	Weapons = ["Knife","Pistol","Hammer", "Fist"]
	def getWeapon(self):
		t = str(random.choice(self.Weapons))
		print("Your weapon:",t)
		return t