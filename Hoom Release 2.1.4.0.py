# Hoom Full Rewrite
# TODO: Add Tkinter Menu & Gameplay based off of Tkinter

"""
MASTER ORG:
HP, Zombies, StrongZombies, Location, PistolAmmo,
ShotgunAmmo, Bandages, ZombiesClose, StrongZombiesClose,
BulletFindMax, ShellsFindMax, BandagesFindMax, ZombieHP,
StrongZombieHP, ZombieDist, StrongZombieDist, Dmg, HealGain, _itick, Actions
"""

import random
import sys
import os
import re
import time
class Core:
    """
    Handles all of the backend functions
    """
    def Menu(self):
        """
        When you first boot up the game this will allow you to play or
        take the tutorial to learn how to read the text/stats
        """
        print("HP: How much health you have")
        print("Zombies: How many zombies are in the area")
        print("Strong Zombies: How many strong zombies are in the area")
        print("Location: What area you are in")
        print("Pistol Ammo: How much ammo you have for your pistol")
        print("Shotgun Ammo: How much ammo you have for you shotgun")
        print("Bandages: How much bandages you have to heal yourself")
        print("Zombies Close: How many zombies can hit you")
        print("Strong Zombies Close: How many strong zombies can hit you")

    def _Init(self):
        """
        This is used to handle initialiszing all of the default vars
        """
        HP = 100
        Zombies = 5
        StrongZombies = 1
        Location = "Road"
        PistolAmmo = 10
        ShotgunAmmo = 0
        Bandages = 1
        ZombiesClose = 1
        StrongZombiesClose = 0
        BulletFindMax = 20
        ShellsFindMax = 5
        BandagesFindMax = 3
        ZombieHP = 3
        StrongZombieHP = 15
        ZombieDist = 20
        StrongZombieDist = 20
        _itick = 0
        Actions = 0

        # For returning values follow this order ex. return [HP, ZombiesClose, StrongZombiesClose] not return [ZombiesClose, HP, StrongZombiesClose] Extra args always last
        return [HP, Zombies, StrongZombies, Location, PistolAmmo, ShotgunAmmo, Bandages, ZombiesClose, StrongZombiesClose, BulletFindMax, ShellsFindMax, BandagesFindMax, ZombieHP, StrongZombieHP, ZombieDist, StrongZombieDist, _itick, Actions]


    def GameTime(self, HP, Zombies, StrongZombies, ZombiesClose, StrongZombiesClose, ZombieHP, StrongZombieHP, ZombieDist, StrongZombieDist, Dmg = 0, _itick = 0, _Target = ""):
        """
        Handles the movement of zombies and calcuating damage to player
        """
        _ZombieMove = random.randint(0, 3)
        _StrongZombieMove = random.randint(0, 8)
        ZombieDist -= _ZombieMove
        StrongZombieDist -= _StrongZombieMove

        if(ZombieDist <= 0) and (Zombies > 0):
            ZombiesClose += 1
            Zombies -= 1
            ZombieDist = 20

        if(StrongZombieDist <= 0) and (StrongZombies > 0):
            StrongZombiesClose += 1
            StrongZombies -= 1
            StrongZombieDist = 20

        if(Dmg != 0) and (_Target == "zombie"):
            ZombieHP -= Dmg
            FarRNG = random.randint(0, 4)

            if(ZombieHP <= 0) and (ZombiesClose >= 1):
                ZombiesClose -= 1
                ZombieHP = 3
                print("The zombie Falls over and dies")
                time.sleep(3)

            elif(ZombieHP <= 0) and (ZombiesClose <= 0) and (FarRNG == 4):
                Zombies -= 1
                HP = 3
                print("The zombie falls over and dies")
                time.sleep(3)

        if(Dmg != 0) and (_Target == "szombie"):
            StrongZombieHP -= Dmg
            print(StrongZombieHP)
            SFarRNG = random.randint(0, 2)

            if(StrongZombieHP <= 0) and (StrongZombiesClose >= 1):
                StrongZombiesClose -= 1
                StrongZombieHP = 15
                print("The strong zombie falls over and dies")
                time.sleep(3)

            elif(StrongZombieHP <= 0) and (StrongZombiesClose <= 0) and (SFarRNG == 2):
                StrongZombies -= 1
                StrongZombieHP = 15
                print("The strong zombie falls over and dies")
                time.sleep(3)

        _itick += 1
        if(_itick == 2):
            _itick = 0
            HP -= ((ZombiesClose) + (StrongZombiesClose * 3))
            if(HP <= 0):
                print("You died")
                exit()

        return [HP, Zombies, StrongZombies, ZombiesClose, StrongZombiesClose, ZombieHP, StrongZombieHP, ZombieDist, StrongZombieDist, _itick]


    def RNG(self):
        """
        Handles generating loc/loot gen
        """
        # List Setup Location: Loc, Max Zombies, Max Strong Zombies,
        # Max Bullets, Max Shells, Max Bandages | Exactly 6 Vals
        Locations = [["Road",10,2,15,5,2],
                     ["Store",30,5,4,10,5],
                     ["Hospital",90,20,10,5,15],
                     ["House",3,1,10,1,1],
                     ["Military base",5,15,40,10,5],
                     ["Military helicopter",2,3,20,5,5]
                    ]

        LocSelect = random.randint(0, 5)
        TempArray = []
        _CurrentLoc = Locations[LocSelect][0]
        TempArray.append(_CurrentLoc)
        for Location in range(1, 5):
            RNG = random.randint(0, Locations[LocSelect][Location])
            TempArray.append(RNG)
            # Return the amount of items/zombies in the area see comment above
        return TempArray

    def RNGLoot(self, interLocalArray):
            # Return how many items are looted
            # LocalArray Org. Max Zomb, Max Strong Zomb, Max Bullets, Max Shells, Max Bandages
            MaxBul = interLocalArray[2]
            MaxShel = interLocalArray[3]
            MaxBand = interLocalArray[4]
            FindBul = random.randint(0, MaxBul)
            FindShel = random.randint(0, MaxShel)
            FindBand = random.randint(0, MaxBand)
            LootArray = [FindBul, FindShel, FindBand]
            print("Found " + str(FindBul) + " Bullets")
            print("Found " + str(FindShel) + " Shotgun Shells")
            print("Found " + str(FindBand) + " Bandages")
            time.sleep(3)
            return LootArray

    def Game(self):
        """
        Anything not covered in other defs
        """
        pass


    def Action(self, PistolAmmo, ShotgunAmmo, Bandages, _LocalArray, Actions):
        Dmg = 0
        _Heal = 0
        """
        Handles player interactions
        Will now be able to easily target
        """
        def Shotgun(Target, ShotgunAmmo):
            # Handles shoutgunning 5 bullets 80% Accuracy
            Hits = 0
            CritHit = 0
            Miss = 0

            if(ShotgunAmmo > 0):
                for h in range(0, 5):
                    HitRNG = random.randint(0, 10)
                    if(HitRNG >= 4) and (HitRNG != 10):
                        Hits += 1
                        print("They get hit by a pellet in the chest!")

                    elif(HitRNG == 10):
                        CritHit += 1
                        print("They get hit by a pellet in the head!")

                    else:
                        Miss += 1
                        print("The pellet misses")
                    # TODO: Do something with the miss var

            else:
                print("Out of ammo!")
                time.sleep(4)

            Damage = (Hits*3) + (CritHit*6)
            time.sleep(4)
            return Damage

        def Pistol(Target, PistolAmmo):
            # Handles pistolling 1 bullet 90% Accuracy
            PHits = 0
            PCritHit = 0
            PMiss = 0
            PHitRng = random.randint(0, 10)
            if(PistolAmmo > 0):
                if(PHitRng >= 1) and (PHitRng <= 9):
                    PHits += 1
                    print("You shoot them missing their head")

                elif(PHits >= 9):
                    PCritHit += 1
                    print("You shoot them hitting them in the head")

                else:
                    PMiss += 1
                    print("You missed")

                Damage = (PHits*2) + (PCritHit*7)
                time.sleep(4)
                return Damage

            else:
                print("Out of ammo!")
                time.sleep(4)


        def Heal():
            # Handles healing 10hp max
            Heal = 0
            Heal = random.randint(0, 10)
            return Heal


        def Move():
            # Handles moving locations every 10 actions
            _HolderValue = Core.RNG()
            print(_HolderValue)
            return _HolderValue


        def Loot(LocalArray):
            # Handles Looting
            _LootPass = Core.RNGLoot(LocalArray)
            return _LootPass


        ZombieKeys = ["zombie", "zombies", "zomb"]
        StrongZombieKeys = ["strong", "s", "s."]
        ShotgunKeys = ["shotty", "shotgun"]
        PistolKeys = ["pistol", "gun", "shoot"]
        HealKeys = ["heal", "cure", "patch", "fix"]
        LootKeys = ["loot", "scavange", "look", "find"]
        MoveKeys = ["move", "go", "drive"]
        ExitKeys = ["quit"]
        Incomplete = True
        _Action = ""
        _Target = ""
        while(Incomplete == True):
            print("Actions: Shoot, pistol, gun :: Shotty, shotgun :: Heal, cure, patch, fix :: Loot, scavange, look, find :: Move, go, drive :: quit")
            print("Targets: strong, s, s. :: zombie, zombies, zomb\n")
            ActionInput = input("Action> ")
            ActionInput = ActionInput.lower()
            ActionList = ActionInput.split(' ')
            Disable = 0
            for Action in ActionList:
                for STarget in StrongZombieKeys:
                    if(STarget == Action):
                        _Target = "szombie"
                        Disable = 1
                for Target in ZombieKeys:
                    if(Target == Action) and (Disable != 1):
                        _Target = "zombie"

                for ShotKey in ShotgunKeys:
                    if(ShotKey == Action):
                        _Action = "shotgun"

                for PistolKey in PistolKeys:
                    if(PistolKey == Action):
                        _Action = "pistol"

                for HealKey in HealKeys:
                    if(HealKey == Action):
                        _Action = "heal"

                for LootKey in LootKeys:
                    if(LootKey == Action):
                        _Action = "loot"

                for MoveKey in MoveKeys:
                    if(MoveKey == Action):
                        _Action = "move"
                for ExitKey in ExitKeys:
                    if(ExitKey == Action):
                        print("Quitting Game")
                        exit()


            if(_Target != "") and (_Action == "shotgun"):
                Incomplete = False

            elif(_Target != "") and (_Action == "pistol"):
                Incomplete = False

            elif(_Action != "shotgun") and (_Action != "pistol") and (_Action != ""):
                Incomplete = False

            else:
                print("Action: " + _Action)
                print("Target: " + _Target)
                print("You have not provided a target or gun please input target, gun or change actions...")

        if(_Action == "shotgun"):
            Dmg = 0
            if(ShotgunAmmo > 0):
                Dmg = Shotgun(_Target, ShotgunAmmo)
                ShotgunAmmo -= 1
            else:
                print("Out of shells!")

            Actions += 1

        elif(_Action == "pistol"):
            Dmg = 0
            if(PistolAmmo > 0):
                Dmg = Pistol(_Target, PistolAmmo)
                PistolAmmo -= 1
            else:
                print("Out of bullets!")

            Actions += 1

        elif(_Action == "heal"):
            _Heal = 0
            Heal = Heal()
            Bandages -= 1
            Actions += 1

        elif(_Action == "loot"):
            _Loot = Loot(_LocalArray)
            MaxBul = _LocalArray[2]
            MaxShel = _LocalArray[3]
            MaxBand = _LocalArray[4]
            SubBul = _Loot[0]
            SubShel = _Loot[1]
            SubBand = _Loot[2]
            _LocalArray = [_LocalArray[0], _LocalArray[1], MaxBul-SubBul, MaxShel-SubShel, MaxBand-SubBand]
            Actions += 1
            PistolAmmo += _Loot[0]
            ShotgunAmmo += _Loot[1]
            Bandages += _Loot[2]
        elif(_Action == "move") and (Actions >= 10):
            Move = Move()
            _LocalArray = Move.copy()
            Actions = 0

        elif(_Action == "move") and (Actions <= 10):
            print("Cannot move actions <= 10")

        else:
            print("Input a valid action")

        return [PistolAmmo, ShotgunAmmo, Bandages, Dmg, _Heal, _LocalArray, _Target, Actions, Move]


Core = Core()


def RunGame():
    """
    The skin of the game itself useless without this
    """
    print("Welcome to HOOM v2.1.2\n\nOptions: Play\tTutorial\tExit")
    MenuInput = input("Menu> ")
    if(MenuInput.lower() == "play"):
        """
        Start the game loop
        """
        Vars = Core._Init()
        while(True):
            """
            MASTER ORG:
            HP, Zombies, StrongZombies, Location, PistolAmmo,
            ShotgunAmmo, Bandages, ZombiesClose, StrongZombiesClose,
            BulletFindMax, ShellsFindMax, BandagesFindMax, ZombieHP,
            StrongZombieHP, ZombieDist, StrongZombieDist, Dmg, HealGain, _itick, Actions
            """
            # NOTE: Vars = 18 val array [0, 17]
            os.system('cls' if os.name=='nt' else 'clear')
            print("HOOM v2.1.4.0 -- MAIN\n\n\n\n\nHP: " + str(Vars[0]) + "\t\t\tLocation: " + str(Vars[3]) + "\nBullets: " + str(Vars[4]) + "\t\tShells: " + str(Vars[5]) + "\nZombies: " + str(Vars[1]) + "\t\tStrong Zombies: " + str(Vars[2]) + "\nZombies Close: " + str(Vars[7]) + "\tStrong Zombies Close: " + str(Vars[8]) + "\nBandages: " + str(Vars[6]) + "\n\n\n")
            LocArray = [0, 0, Vars[9], Vars[10], Vars[11]]
            ActOut = Core.Action(Vars[4], Vars[5], Vars[6], LocArray, Vars[17])
            GameOut = Core.GameTime(Vars[0], Vars[1], Vars[2], Vars[7], Vars[8], Vars[12], Vars[13], Vars[14], Vars[15], ActOut[3], Vars[16], ActOut[6])
            # Replace Vars updated by GameTime() and ActOut()
            HPGain = 0
            if(Vars[0] != 100):
                HPGainPart = 100 - Vars[0]
                if(HPGainPart <= 90):
                    #Full Heal
                    HPGain = ActOut[4]

                else:
                    _MaxHeal = ActOut[0]
                    while(HPGainPart != 100) and (_MaxHeal != 0):
                        HPGain += 1
                        HPGainPart += 1
                        _MaxHeal -= 1

            # Var 3 will always error before being called and after being called(but not during the call)
            try:
                Vars = [GameOut[0]+HPGain, GameOut[1], GameOut[2], ActOut[8][0], ActOut[0], ActOut[1], ActOut[2], GameOut[3], GameOut[4], ActOut[5][2], ActOut[5][3], ActOut[5][4], GameOut[5], GameOut[6], GameOut[7], GameOut[8], GameOut[9], ActOut[7]]
            except:
                Vars = [GameOut[0]+HPGain, GameOut[1], GameOut[2], Vars[3], ActOut[0], ActOut[1], ActOut[2], GameOut[3], GameOut[4], ActOut[5][2], ActOut[5][3], ActOut[5][4], GameOut[5], GameOut[6], GameOut[7], GameOut[8], GameOut[9], ActOut[7]]
    elif(MenuInput.lower() == "tutorial"):
        """
        Teach the player how to play the game
        """
        Core.Menu()
    elif(MenuInput.lower() == "exit"):
        exit()
    else:
        print("Enter a valid input")

while(True):
    RunGame()
