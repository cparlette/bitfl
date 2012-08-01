import player, location

class Game:
  def __init__(self,conf_file="game.conf"):
    #Game ID: date string with a random number on the end
    self.game_id = "2012-07-29-01"
    #Read the configuration from the file into a dictionary
    conf = dict()
    lines = [line.strip() for line in open(conf_file)]
    for line in lines:
      if line[0] is '#':
        continue
      entry = line.split('=')
      if len(entry) == 2:
        conf[entry[0].lower()] = entry[1]
      else:
        print "invalid game configuration line: '%s'" % str(line)
    print "conf: "+str(conf)
    #For any values not provided in the conf file, use defaults
    #Max Players
    if 'max_players' in conf:
      self.max_players = int(conf['max_players'])
    else:
      self.max_players = 4
    #Number of time units for each turn
    if 'units_per_turn' in conf:
      self.units_per_turn = int(conf['units_per_turn'])
    else:
      self.units_per_turn  = 5
    self.turn = 0 #Turn number we are currently on
    self.player_list = []
    self.locations = []
  
  def __repr__(self):
    result = "Game ID: "+self.game_id+"\n"
    result += "Players: "
    result += ", ".join(str(player) for player in self.player_list)+"\n"
    result += "Turn: "+str(self.turn)+"\n"
    return result
  
  def debug_string(self):
    result = "---------------------------\n"
    result += "|Game Debug\n"
    result += "|Game ID: "+self.game_id+"\n"
    result += "|Max Players: "+str(self.max_players)+"\n"
    result += "---------------------------\n"
    return result
  
  def game_summary(self):
    result = "Turn "+str(self.turn)
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
    self.turn += 1
    for player in self.player_list:
      player.add_time_units(self.units_per_turn)
    return True
  
  def get_locations(self):
    return self.locations

  def turn_complete(self):
    """Return True if all players have used their time for this turn."""
    for player in self.player_list:
      if player.units > 0:
        return False
    return True
  
  def get_next_player(self):
    """Return the next player that has turns remaining.
    Return None if no players are found.
    If all players are done, then the game moves to the next turn before returning."""
    for player in self.player_list:
      if player.units > 0:
        return player
    return None
  
  
