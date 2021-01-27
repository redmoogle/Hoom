# HOOM REWRITTEN

import random
import sys
import os
import re
import time

def create_multikey_dict(listinput):
    """
    Create a dictonary with muliple keys to one output
    Last item in the list is the output from the keys
    """
    key = '' # thing to map all the keys to
    templist = [] # holder for the tuples
    for associated_list in listinput: # grab each sublist
        key = associated_list[len(associated_list)-1] # grab the last item to associate it to a common value
        associated_list.pop(len(associated_list)-1) # and also remove it
        for associated_input in associated_list: # grab all other values to make the 'key' to common value
            templist.append(tuple([associated_input, key])) # tuples is used to make the dictonary
    return dict(templist) # turn the list of tuples into a dictonary

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
    Game Instance Class
    """
    def __init__(self):
        """
        Self is used, for when multiplayer 'might' come along
        """
        # Converts keywords to one unified output
        self.actions = [
            ['shoot', 'kill', 'shoot'],                 # shoot that zombie
            ['switch', 'swap', 'change', 'switch'],     # change the weapon
            ['use', 'consume', 'use'],                  # use an item
            ['examine', 'look', 'examine'],             # check the area out
            ['loot', 'check', 'loot']                   # gather the good stuff
        ]

        self.hp = 100        # HP of the player
        self.zombies = []    # Holds a list with a reference to the zombie: [Type, Dist, HP, Damage, Speed]
        self.location = {}   # Dictonary related to the location
        self.ammo = {}       # Reference of ammo types
        self.items = {}      # Stuff the player has
        self.__generator()   # generate zombies and a location
        self._actions = create_multikey_dict(self.actions) # create internal actions
        self.selected = None # Selected weapon for better actions

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
            _zombies += zombies[0]
        
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

    def __actionswitch(self, action):
        """
        Switches between action keywords
        """
        # Actions: shoot, switch, use, examine, loot
        if(action == 'shoot'):
            pass
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

    def __shootgun(self, bullets=1, damage=3):
        """
        Calculates damage and removes zombies
        """
        _critchance = 10    # how often bullets land a 'critical hit'
        _itercalc = -1      # for removing from the list
        _rlist = None       # Contains what happened to zombies in a list
        _found = False      # has a zombie been found

        for zombie in self.zombies: # this is used to grab the first closest zombie
            _itercalc += 1
            if(zombie[1] >= 2):
                _found = True # used to make sure we did find the zombie so we dont shoot a null/out of range zombie
                break
        
        if(_found):
            for _ in range(bullets):
                zombie = self.zombies[_itercalc] # 'reference' to the zombie for manipulation
                zombie[2] = max(0, zombie[2]-damage)
            if(zombie[2] <= 0): # <= incase it somehow goes negative
                self.zombies.pop(_itercalc) # Pop goes the zombie!
        else:
            return False

    def handle_input(self):
        """
        Handles the input from the user
        """
        userinput = ((input(f'Avaliable Actions: {format_actions(self.actions)}...\n')).lower()).split()
        action = None # what have they chosen to do
        for split_actions in userinput:
            if(split_actions in self._actions):
                action = self._actions[split_actions]
                break
            return print(f'You have chose something invalid... ({"".join(userinput)})')

        print(f'You have chose to {action}')
        self.__actionswitch(action)
        

Game = Game()
Game.__init__()
Game.handle_input()

