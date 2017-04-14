import Characters_klass as ck
from tkinter import *
import time
Weapon = ck.Weapon()
med_kit = ck.BonusHP()
Peny = ck.Character()
Charly = ck.MissCharacters()
Charly.Hit(Weapon.getWeapon())
Charly.useBonus(med_kit.getBonus())
Charly.Hit(Weapon.getWeapon())
Charly.Hit(Weapon.getWeapon())
Charly.useBonus(med_kit.getBonus())
Charly.useBonus(med_kit.getBonus())
Charly.Hit("Pistol",)
Charly.useBonus(med_kit.getBonus())
print("_______________________")