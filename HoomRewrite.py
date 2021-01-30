# HOOM REWRITTEN

import random
import sys
import os
import re
import time
from multi_key_dict import multi_key_dict

def format_actions(listinput):
    """
    Converts the actions from self.action into a into a neat string.
    Grabs from the first element in each sublist
    """
    _counter = 0    # for formatting actions
    _formatted = ''
    for unformatted in listinput:
        _counter += 1
        _formatted += f'{unformatted[0]}'
        if(_counter+1 <= int(len(listinput))):
            _formatted += ", "
    return _formatted

class Game:
    """
    Holds all the variables and functions related to controlling the game
    """
    def __init__(self):
        """
        Self is used, for when multiplayer 'might' come along
        """
        # Converts keywords to one unified output first is the one that others get converted to
        self.actions = [
            ['shoot', 'kill'],      # shoot that zombie
            ['switch', 'swap'],     # change the weapon
            ['use', 'consume'],     # use an item
            ['examine', 'look'],    # check the area out
            ['loot', 'check']       # gather the good stuff
        ]

        self.hp = 100               # HP of the player
        self.zombies = []           # Holds a list with a reference to the zombie: [Type, Dist, HP, Damage, Speed]
        self.location = {}          # Dictonary related to the location
        self.ammo = {}              # Reference of ammo types
        self.__generator()          # generate zombies and a location

        # Reference of ammo types
        self.ammo = {'9mm': 20, 'buckshot': 10}
        # Stuff the player has
        # Weapons List: [name, bullets per shot, damage, ammotype]
        self.items = {'Weapons': [['Tokchiva 9mm', 1, 7, '9mm'], ['Lanska Buckshotgun', 5, 3, 'buckshot']]}
        # Selected weapon for better actions
        self.selected = ['Tokchiva 9mm', 1, 3]

        self.actionsdict = multi_key_dict() # generate the assosative list
        for action in self.actions: # loop through the action list above
            self.actionsdict[action] = action[0] # insert the keyword converter list

    def __zombiegen(self, amount):
        """
        Generate some zombies
        """
        _zombies = [] # Used for returning the new zombies
        zombies = [
            ['Normal Zombie', 5, 10, 2, 2],
            ['Strong Zombie', 5, 15, 4, 2],
            ['Brute Zombie', 5, 20, 5, 1],
            ['Fast Zombie', 5, 8, 1, 4]
        ]
        for _ in range(amount):
            random.shuffle(zombies)
            _zombies.append(zombies[0])
        
        return _zombies


    def __ticker(self):
        """
        Handles internally ticking over zombies and other related things
        """
        _movechance = 20 # 20% to move closer
        for zombie in self.zombies:
            _rng = random.randint(0, 100)
            if(_rng <= _movechance): # Move the zombie up
                zombie[1] = max(0, zombie[1] - zombie[4]) # anti negative check

    def __generator(self):
        """
        Generates zombies and location data
        """
        locations = ['Store', 'Hospital', 'Military Base', 'Mall'] # fluff for now
        random.shuffle(locations)
        self.location['location'] = locations[0]
        self.location['low-cal'] = random.randint(0, 20)
        self.location['high-cal'] = random.randint(0, 10)
        self.zombies = self.__zombiegen(random.randint(0, 10)) # Empty it before generating

    def __shootgun(self):
        """
        Calculates damage and removes zombies
        """
        _critchance = 10    # how often bullets land a 'critical hit'
        _itercalc = -1      # for removing from the list
        _rlist = None       # Contains what happened to zombies in a list
        _found = False      # has a zombie been found
        if(self.ammo[self.selected[3]] <= 0):
            return f'You do not have enough {self.selected[3]} ammo'
        # use one bullet(for now)
        self.ammo[self.selected[3]] -= 1
        for zombie in self.zombies: # this is used to grab the first closest zombie
            _itercalc += 1
            print(zombie)
            if(zombie[1] <= 3):
                _found = True # used to make sure we did find the zombie so we dont shoot a null/out of range zombie
                break
            else:
                return 'You try to find something to shoot but you dont see anything close enough'
        
        for _ in range(self.selected[1]):
            zombie = self.zombies[_itercalc] # 'reference' to the zombie for manipulation
            zombie[2] = max(0, zombie[2]-self.selected[2])
        if(zombie[2] <= 0): # <= incase it somehow goes negative
            self.zombies.pop(_itercalc) # Pop goes the zombie!
            return f'The {zombie[0]} falls over on to the ground...'
        return f'You hit the {zombie[0]} {self.selected[1]} times, dealing {self.selected[1]*self.selected[2]} damage to them'

    def handle_input(self):
        """
        Handles the input from the user
        """
        userinput = ((input(f'Avaliable Actions: {format_actions(self.actions)}...\n')).lower()).split()
        action = None # what have they chosen to do
        for split_actions in userinput:
            if(split_actions in self.actionsdict):
                action = self.actionsdict[split_actions]
                break
            return print(f'You have chose something invalid... ({"".join(userinput)})')

        print(f'You have chose to {action}')
        self.__actionswitch(action)

    def __actionswitch(self, action):
        """
        Switches between action keywords
        """
        # Actions: shoot, switch, use, examine, loot
        result = False # used for comparing to see if something happened
        if(action == 'shoot'):
            result = self.__shootgun()
        elif(action == 'switch'):
            pass
        elif(action == 'use'):
            pass
        elif(action == 'examine'):
            pass
        elif(action == 'loot'):
            pass
        else:
            raise Exception('Non-Switch Word provided')

        if(result is not False):
            print(result)
        else:
            print('nothing happened')

Game = Game()
Game.__init__()
while(True):
    Game.handle_input()

