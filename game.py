import player, location

class Game:
  def __init__(self):
    #Game ID: date string with a random number on the end
    self.game_id = "2012-07-29-01"
    self.max_players = 4
    self.player_list = []
    self.units_per_turn  = 5 #Number of time units for each turn
    self.turn = 0 #Turn number we are currently on
  
  def __repr__(self):
    result = "Game ID: "+self.game_id+"\n"
    result += "Players: "
    result += ", ".join(str(player) for player in self.player_list)+"\n"
    result += "Turn: "+str(self.turn)+"\n"
    return result
  
  def add_player(self,player):
    """Add the given player to the game if there is room.
    If the user is added to the game, it returns True. If not, it returns False."""
    if len(self.player_list) < self.max_players:
      self.player_list.append(player)
      return True
    else:
      return False
  
  def start_game(self):
    """Start the game with the current players."""
    if len(self.player_list) == 0:
      return False
    
    #Start game
    return self.next_turn()
  
  def next_turn(self):
    for player in self.player_list:
      player.add_time_units(self.units_per_turn)
    self.turn += 1
    return True
