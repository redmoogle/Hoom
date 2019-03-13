#Hoom is 100% not a ripoff of doom in terminal
#Start Import
import random
import sys
#End Import
#Start Default Vars
RNGSelect = ""
Action = ""
CurrentLoc = ""
passkey = ""
HP = 100
PistolAmmo = 30
ShotgunAmmo = 5
Gernades = 3
Bandages = 1
Zombies = 0
SZombies = 0
ZombieHP = 3
ZombieSHP = 15
ZombieDist = 10
ZombieDistS = 15
ZombieClose = 0
ZombieCloseS = 0
AllowMove = 0
_itick = 0
_BulletFindMax = 0
_ShellsFindMax = 0
_BandagesFindMax = 0
#End Default Vars
#Start GameTick
def GameTick():
	global HP
	global AllowMove
	if(True):
		_itick = _itick + 1
		if(_itick >= 3):
			AllowMove = AllowMove + 1
			_itick = 0
			_SZDmg = ZombieCloseS * 2
			_ZDmg = ZombieClose
			_TDmg = _ZDmg + _SZDmg
			HP = HP - _TDmg
			if(HP <= 0):
				print("you've died")
				exit()
#End GameTick
#Start RNG Generators
def RNGCore(RNGSelect):
	global CurrentLoc
	global Zombies
	global SZombies
	global _ShellsFindMax
	global _BulletFindMax
	global _BandagesFindMax
	global ZombieMove
	global ZombieMoveS
	global ZombieDist
	global ZombieDistS
	global ZombieClose
	global ZombieCloseS
	global ShotgunAmmo
	global PistolAmmo
	global Bandages
	global _BulletsFind
	global _ShellsFind
	global _BandagesFind
	global hitdmg
	global ZombieHP
	global ZombieSHP
	if(RNGSelect == "mz"):
		ZombieMove = random.randrange(1, 5, 1)
		ZombieMoveS = random.randrange(1, 5, 1)
		ZombieDist = ZombieDist - ZombieMove
		ZombieDistS = ZombieDistS - ZombieMoveS
		if(ZombieDist <= 1) & (Zombies >= 1):
			ZombieClose = ZombieClose + 1
			ZombieDist = random.randrange(1, 8, 1)
			Zombies = Zombies - 1
		if(ZombieDistS <= 1) & (SZombies >= 1):
			ZombieCloseS = ZombieCloseS + 1
			ZombieDistS = random.randrange(1, 8, 1)
			SZombies = SZombies - 1
	elif(RNGSelect == "loot"):
		_ShellsFind = random.randrange(0, 5, 1)
		_BulletsFind = random.randrange(0, 15, 1)
		_BandagesFind = random.randrange(0, 2, 1)
		_BulletFindMax = _BulletFindMax - _BulletsFind
		_ShellsFindMax = _ShellsFindMax - _ShellsFind
		_BandagesFindMax = _BandagesFindMax - _BandagesFind
		if(_ShellsFindMax >= 0):
			ShotgunAmmo = ShotgunAmmo + _ShellsFind
			print("You've found: " + str(_ShellsFind) + " Shotgun Shells")
		else:
			print("you find no shotgun shells")
		if(_BulletFindMax >= 0):
			PistolAmmo = PistolAmmo + _BulletsFind
			print("You've found: " + str(_BulletsFind) + " Pistol Ammo")
		else:
			print("you find no pistol ammo")
		if(_BandagesFindMax >= 0):
			Bandages = Bandages + _BandagesFind
			print("You've found: " + str(_BandagesFind) + " Bandages")
		else:
			print("you find no bandages")
	elif(RNGSelect == "bullet"):
		bulletRNG = random.randrange(1, 100, 1)
		if(bulletRNG <= 5):
			print("You somehow missed!")
		elif(bulletRNG >= 6) and (bulletRNG <= 15):
			print("You manage to shoot them in the legs!")
			hitdmg = 2
			ZombieHP = ZombieHP - hitdmg
		elif(bulletRNG >= 16) and (bulletRNG <= 70):
			print("You shoot them square in the chest!")
			hitdmg = 4
			ZombieHP = ZombieHP - hitdmg
		elif(bulletRNG >= 71) and (bulletRNG <= 100):
			print("Headshot!")
			hitdmg = 6
			ZombieHP = ZombieHP - hitdmg
		if(ZombieHP <= 0):
			ZombieHP = 3
			ZombieClose = ZombieClose - 1
			print("The weak zombie falls over and dies")
	elif(RNGSelect == "bullets"):
		bulletRNG = random.randrange(1, 100, 1)
		if(bulletRNG <= 5):
			print("You somehow missed!")
		elif(bulletRNG >= 6) and (bulletRNG <= 15):
			print("You manage to shoot them in the legs!")
			hitdmg = 2
		elif(bulletRNG >= 16) and (bulletRNG <= 70):
			print("You shoot them square in the chest!")
			hitdmg = 4
		elif(bulletRNG >= 71) and (bulletRNG <= 100):
			print("Headshot!")
			hitdmg = 6
		ZombieSHP = ZombieSHP - hitdmg
		if(ZombieSHP <= 0):
			ZombieSHP = 15
			ZombieCloseS = ZombieCloseS - 1
			print("The weak zombie falls over and dies")
	elif(RNGSelect == "bulletsgns"):
		for x in range(0, 5):
			bulletRNG = random.randrange(1, 100, 1)
			if(bulletRNG <= 5):
				print("You somehow missed!")
			elif(bulletRNG >= 6) and (bulletRNG <= 15):
				print("You manage to shoot them in the legs!")
				hitdmg = 1
				ZombieSHP = ZombieSHP - hitdmg
			elif(bulletRNG >= 16) and (bulletRNG <= 70):
				print("You shoot them square in the chest!")
				hitdmg = 2
				ZombieSHP = ZombieSHP - hitdmg
			elif(bulletRNG >= 71) and (bulletRNG <= 100):
				print("Headshot!")
				hitdmg = 3
				ZombieSHP = ZombieSHP - hitdmg
		if(ZombieSHP <= 0):
			ZombieSHP = 15
			ZombieCloseS = ZombieCloseS - 1
			print("The strong zombie falls over and dies")
	elif(RNGSelect == "bulletsgn"):
		for x in range(0, 5):
			bulletRNG = random.randrange(1, 100, 1)
			if(bulletRNG <= 5):
				print("You somehow missed!")
			elif(bulletRNG >= 6) and (bulletRNG <= 15):
				print("You manage to shoot them in the legs!")
				hitdmg = 1
				ZombieHP = ZombieHP - hitdmg
			elif(bulletRNG >= 16) and (bulletRNG <= 70):
				print("You shoot them square in the chest!")
				hitdmg = 2
				ZombieHP = ZombieHP - hitdmg
			elif(bulletRNG >= 71) and (bulletRNG <= 100):
				print("Headshot!")
				hitdmg = 3
				ZombieHP = ZombieHP - hitdmg
		if(ZombieHP <= 0):
			ZombieHP = 3
			ZombieClose = ZombieClose - 1
			print("The weak zombie falls over and dies")
	elif(RNGSelect == "ml"):
		Location = random.randrange(1, 100, 1)
		if(Location <= 40):
			_ShellsFindMax = random.randrange(5, 20, 1)
			_BulletFindMax = random.randrange(15, 80, 1)
			_BandagesFindMax = random.randrange(0, 5, 1)
			CurrentLoc = "road"
			Zombies = random.randrange(0, 20, 1)
			SZombies = random.randrange(0, 2, 1)
		elif(Location >= 41) & (Location <= 55):
			_ShellsFindMax = random.randrange(0, 10, 1)
			_BulletFindMax = random.randrange(0, 30, 1)
			_BandagesFindMax = random.randrange(5, 20, 1)
			CurrentLoc = "grocery store"
			Zombies = random.randrange(0, 25, 1)
			SZombies = random.randrange(0, 5, 1)
		elif(Location >= 56) & (Location <= 75):
			_ShellsFindMax = random.randrange(10, 20, 1)
			_BulletFindMax = random.randrange(0, 30, 1)
			_BandagesFindMax = random.randrange(0, 5, 1)
			CurrentLoc = "parking lot"
			Zombies = random.randrange(0, 30, 1)
			SZombies = random.randrange(0, 2, 1)
		elif(Location >= 76) & (Location <= 85):
			_ShellsFindMax = random.randrange(10, 50, 1)
			_BulletFindMax = random.randrange(15, 80, 1)
			_BandagesFindMax = random.randrange(1, 3, 1)
			CurrentLoc = "gun store"
			Zombies = random.randrange(0, 40, 1)
			SZombies = random.randrange(0, 6, 1)
		else:
			_ShellsFindMax = random.randrange(30, 80, 1)
			_BulletFindMax = random.randrange(60, 150, 1)
			_BandagesFindMax = random.randrange(10, 30, 1)
			CurrentLoc = "crashed military helicopter"
			Zombies = random.randrange(0, 70, 1)
			SZombies = random.randrange(0, 20, 1)
	else:
		print("Critical error in RNGCore Selector")
		print(RNGSelect)
#End RNG Generators
#Start Game Core
def GameCore(passkey):
	#Start Health Subsystem
	print("Stats:\nShotgun Shells: " + str(ShotgunAmmo) + "\tPistol Ammo: " + str(PistolAmmo) + "\nGernades: " + str(Gernades) + "\tBandages: " + str(Bandages) + "\nHealth: " + str(HP))
	print("You find yourself at a " + CurrentLoc + ", and you see " + str(Zombies) + " zombies along with " + str(SZombies) + " tough looking zombies\nThere is " + str(ZombieClose) + " Zombies nearby and " + str(ZombieCloseS) + " Strong Zombies nearby.\n\n")
	print(passkey)
	if(AllowMove >= 5):
		print("you can now move to a new location!")
	Actions()
#End Game Core
#Start Actions
def Actions():
	global passkey
	global HP
	global Bandages
	global ZombieClose
	global ZombieCloseS
	global PistolAmmo
	global ShotgunAmmo
	global AllowMove
	print("Valid Actions: 'wait', 'loot', 'heal', 'shoot', 'gernade', and 'exit'")
	if(AllowMove >= 5):
		print("Special action: 'move'")
	_ActInp = raw_input("Action: ")
	if(_ActInp.lower() == "wait"):
		RNGSelect = "mz"
		RNGCore(RNGSelect)
		GameTick()
	elif(_ActInp.lower() == "loot"):
		RNGSelect = "loot"
		RNGCore(RNGSelect)
		RNGSelect = "mz"
		RNGCore(RNGSelect)
		GameTick()
	elif(_ActInp.lower() == "heal"):
		if(HP <= 90):
			Bandages = Bandages - 1
			HP = HP + 10
			passkey = "Healed for 10 HP"
			GameTick()
		else:
			passkey = "There is no use to heal right now"
	elif(_ActInp.lower() == "gernade"):
		if(ZombieClose >= 1) or (ZombieCloseS >= 1):
			_kill = random.randrange(1, 10, 1)
			_skill = random.randrange(1, 3, 1)
			ZombieClose = ZombieClose - _kill
			ZombieCloseS = ZombieCloseS - _skill
			passkey = "You kill some zombies with the gernade"
			while(ZombieClose <= 0):
				ZombieClose = 0
			while(ZombieCloseS <= 0):
				ZombieCloseS = 0
		else:
			passkey = "There are no zombies to explode"
	elif(_ActInp.lower() == "shoot"):
		_ActInpSht = raw_input("Shoot With? ('shotgun' or 'pistol') ")
		if(_ActInpSht.lower() == "pistol"):
			_ActInpShtPstl = raw_input("Shoot 'Strong' or 'Weak' Zombies? ")
			if(_ActInpShtPstl.lower() == "strong"):
				if(ZombieCloseS >= 1):
					RNGSelect = "bullets"
					RNGCore(RNGSelect)
					PistolAmmo = PistolAmmo - 1
					ZombieSHP = ZombieSHP - hitdmg
					GameTick()
				else:
					passkey = "There is nothing to shoot"
			if(_ActInpShtPstl.lower() == "weak"):
				if(ZombieClose >= 1):
					RNGSelect = "bullet"
					RNGCore(RNGSelect)
					PistolAmmo = PistolAmmo - 1
					GameTick()
				else:
					passkey = "There is nothing to shoot"
		elif(_ActInpSht.lower() == "shotgun"):
			_ActInpShtSgn = raw_input("Shoot 'Strong' or 'Weak' Zombies? ")
			if(_ActInpShtSgn.lower() == "strong"):
				if(ZombieCloseS >= 1):
					RNGSelect = "bulletsgns"
					RNGCore(RNGSelect)
					ShotgunAmmo = ShotgunAmmo - 1
					GameTick()
				else:
					passkey = "There is nothing to shoot"
			if(_ActInpShtSgn.lower() == "weak"):
				if(ZombieClose >= 1):
					RNGSelect = "bulletsgn"
					RNGCore(RNGSelect)
					ShotgunAmmo = ShotgunAmmo - 1
					GameTick()
				else:
					passkey = "There is nothing to shoot"
	elif(_ActInp.lower() == "move"):
		if(AllowMove >= 5):
			RNGSelect = "ml"
			RNGCore(RNGSelect)
			passkey = "You move on"
			AllowMove = 0
	elif(_ActInp.lower() == "exit"):
		exit()
	else:
		passkey = "Invalid Input"
#End Actions
#Startup Runtime
if(True):
	RNGSelect = "ml"
	RNGCore(RNGSelect)
	GameCore(passkey)
while(True):
	GameCore(passkey)