import player

class Game:
  def __init__(self):
    #Game ID: date string with a random number on the end
    self.game_id = "2012-07-29-01"
  
  def add_player(self,player):
    pass
  
  def __repr__(self):
    return "Game ID: "+self.game_id
