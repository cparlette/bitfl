"""
Another attempt at Billy in the Fat Lane

Author:
Chris Parlette

July 11 2012 - Began work
"""

class player():
	def __init__(self):
		self.money = 100
		self.education = 0
		self.happiness = 0
		self.inventory = []
	
	def printStatus(self):
	    print "Your current money is", player.money
	    print "Your education level is", player.education
	    print "Your happiness level is", player.happiness
	    print "You currently own:\n", player.inventory

class gametime():
    def __init__(self):
        self.day = 0
        self.timeLeft = 16


print "Welcome to Billy in the Fat Lane!"
player = player()
gametime = gametime()
player.printStatus()
