class Player():
  def __init__(self,name):
    self.money = 100
    self.education = 20 #scale of self.scale_min to self.scale_max, start at 20
    self.happiness = 20 #scale of self.scale_min to self.scale_max, start at 20
    self.inventory = []
    self.name = name
    self.scale_min = 0
    self.scale_max = 100
    self.units = 0.0 #Time units this player currently has
  
  def __repr__(self):
    return self.name
  
  def printStatus(self):
    status = "Your current money is" + self.get_money
    status += "Your education level is" + self.get_education
    status += "Your happiness level is" + self.get_happiness
    status += "You currently own:\n" + self.get_inventory
    return status
  
  def get_inventory(self):
    return self.inventory
  
  def get_education(self):
    return self.education
  
  def get_happiness(self):
    return self.happiness
  
  def get_money(self):
    return self.money
  
  def add_education(self,points):
    """Add education points for this player. This can be a negative value."""
    if self.education + points < self.scale_max and self.eductaion + points > self.scale_min:
      self.education += points
      return True
    return False
  
  def add_happiness(self,points):
    """Add happiness points for this player. This can be a negative value."""
    if self.happiness + points < self.scale_max and self.happiness + points > self.scale_min:
      self.happiness += points
      return True
    return False
  
  def add_time_units(self,units):
    self.units += units
