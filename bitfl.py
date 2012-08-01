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
import location

class gametime():
    def __init__(self):
        self.day = 0
        self.timeLeft = 16


print "Welcome to Billy in the Fat Lane!"
#Create a game for the player
game = Game()
#Create players
print "Creating players, blank line will stop adding players"
adding = True
while adding:
  player = Player(raw_input("Player Name: "))
  if player.name == '':
    adding = False
  else:
    #Add the player
    game.add_player(player)
if game.start_game():
  print "\n\n************\ngame started\n************"
else:
  print "error starting game"
gametime = gametime()
print game
