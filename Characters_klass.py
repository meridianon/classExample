import random, time
import timefunct
class Character(object):
	"""docstring for Character"""
	hand = ["right","left"]
	head = True 
	Leg = ["right","left"]
	hp = 5000
	CoolectionTarget = [hand,head,Leg]
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
				self.TimerLooseHp(10,0.1)
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
	def TimerLooseHp(self,arg1,arg2):
		k = 0
		count = arg1
		delay = arg2
		while 1:
			if k == count:
				break
			else:
				k+=1
				time.sleep(delay)
				self.hp -= 20
				if self.hp < 0:
					self.printGameOver()
				else:
					print("You lost:", self.hp, "Hp") #- 200 hp with 10 sec

class MissCharacters(Character):
	hp = 10500

	# def __init__(self):
	# 		self.Regeneration()

	def Hit(self,weapon):
		r = random.randint(0, 1)
		if self.hp <0:
			self.printGameOver()
		elif r == 1:
			self.MissHit()
		elif r == 0:
			if weapon != "Fist": 
				self.hp -=30
				self.Imposedebaf(weapon)
			else:
				self.hp -=10
			if self.hp < 0:
				self.printGameOver()
			else:
				print("Characters :", self.hp ,"damage")
	def TimerLooseHp(self,arg1,arg2):
		k = 0
		count = arg1
		delay = arg2
		while 1:
			if k == count:
				break
			else:
				k+=1
				time.sleep(delay)
				self.hp -= 14
				if self.hp < 0:
					self.printGameOver()
				else:
					print("You lost:", self.hp, "Hp") #- 200 hp with 10 sec	

	def MissHit(self):
		print("miss")
	def Regeneration(self):

		while 1:
			if self.hp >= 10500:
				self.hp = 10500
			else:
				self.hp += 5
				print("regen", self.hp)

	def useBonus(self,arg):
			self.hp += int(arg)
			if self.hp >= 10500:
				self.hp = 10500
				print("You use med kit = ", arg)
				print("You hp =", self.hp)
			else:
				print("You use med kit = ", arg)
				print("You hp =", self.hp)
		
class Weapon(object):
	"""docstring for Weapon"""
	Weapons = ["Knife","Pistol","Hammer", "Fist"]
	def getWeapon(self):
		t = str(random.choice(self.Weapons))
		print("Your weapon:",t)
		return t

class BonusHP(object):
	firstaid_kit_default = 200
	firstaid_kit_max = 1000
	firstaid_kit_min = 20
	fak = [firstaid_kit_default, firstaid_kit_max, firstaid_kit_min]
	def getBonus(self):
		g = str(random.choice(self.fak))
		return g
		
		