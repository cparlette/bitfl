class Player():
	def __init__(self):
		self.money = 100
		self.education = 20 #scale of 0 to 100, start at 20
		self.happiness = 20 #scale of 0 to 100, start at 20
		self.inventory = []
	
	def printStatus(self):
	    print "Your current money is", player.money
	    print "Your education level is", player.education
	    print "Your happiness level is", player.happiness
	    print "You currently own:\n", player.inventory
  
  def __repr__(self):
    result = "Your current money is", player.money
    result += "Your education level is", player.education
	  result += "Your happiness level is", player.happiness
	  result += "You currently own:\n", player.inventory
    return result
