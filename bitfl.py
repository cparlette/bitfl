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

def new_game():
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
  return game

def run_game(game):
  done = False
  player = game.get_next_player() #get it started
  while player:
    while not done:
      print game.game_summary()
      print player.player_summary()
      print "\nTurn Menu\n---------"
      print "(U)se time"
      print "(Q)uit"
      choice = raw_input("> ").lower()
      if choice == 'q':
        print "Exiting..."
        return
      if choice == 'u':
        #This is for debugging, to see that turns will proceed
        time = float(raw_input("Time to use: "))
        player.units -= time
        if player.units == 0:
          done = True
    if game.turn_complete():
      print "Proceeding to next turn..."
      game.next_turn() #move this to the Game class?
    player = game.get_next_player()
    done = False

done = False
print "Welcome to Billy in the Fat Lane!"
while not done:
  print "\nMain Menu\n---------"
  print "(N)ew Game"
  print "(Q)uit"
  choice = raw_input("> ").lower()
  if choice == 'n':
    game = new_game()
    print game.debug_string()
    if game.start_game():
      print "\n\n************\ngame started\n************"
    else:
      print "error starting game"
    gametime = gametime()
    run_game(game)
  if choice == 'q':
    done = True
