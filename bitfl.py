"""
Another attempt at Billy in the Fat Lane

Author:
Chris Parlette

Contributors:
Matt Parlette

July 11 2012 - Began work
"""

from player import Player
from game import Game

class gametime():
    def __init__(self):
        self.day = 0
        self.timeLeft = 16


print "Welcome to Billy in the Fat Lane!"
#Create a player
player1 = Player()
#Create a game for the player
game = Game()
#Add the player
game.add_player(player1)
gametime = gametime()
print game
