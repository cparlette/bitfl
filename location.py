import player

class Service:
  def __init__(self,name):
    self.name = name
    #The base cost per unit of service
    #  we may add an economy later
    self.base_cost = 0.0
    #Time used per unit of service
    self.time_used = 0.0
    #The variables below are the affects of this service
    #  for example, to increase or decrease education a number of points
    self.inc_education = 0
    self.dec_education = 0
    self.inc_happiness = 0
    self.dec_happiness = 0
  
  def __repr__(self):
    return self.name
  
  def purchase_units(self,units,player):
    """If the player has enough money and time, then money will be taken from the player and
    the services will be rendered on the player."""
    total_cost = units * self.base_cost
    total_time = units * self.time_used
    if player.money >= total_cost:
      #need to add time check
      player.money -= total_cost
      #render services

class Job:
  def __init__(self,name):
    self.name = name
    self.available = False #Is this job available?
    self.employee = None #Player object who is currently employed
    self.pay = 0.0 #Pay per time unit
  
  def __repr__(self):
    return self.name
  
  def is_available(self):
    return self.available
  
  def requirements_check(self,player):
    """Returns True if the player fulfills the requirements for this job.
    If it does not fulfill the requirements, then a string is returned with a reason."""
    if self.available:
      return True
    else:
      return "This job is not available"
  
  def hire_player(self,player):
    """Assign the given player to this job, making it unavailable for others.
    This function will verify that the player has the job requirements."""
    verify = requirements_check(player)
    if verify:
      self.available = False
      self.employee = player
    else:
      return verify
  
  def fire_player(self,player):
    """Remove the player from this job. This could happen from a firing or if the player quits."""
    self.available = True
    self.employee = None

class Location:
  def __init__(self,name):
    self.location_id = "1" #Internal identifier
    self.name = name #Friendly name
    self.services = [] #List of services offered here
    self.goods = [] #List of goods offered here
    self.jobs = [] #List of jobs available here
    
  def __repr__(self):
    return self.name
  
  def add_service(self,service):
    """Add a service to the services list for this location."""
    if service in self.services:
      pass #service already exists
    else:
      self.services.append(service)
  
  def del_service(self,service):
    """Remove a service from the services list for this location."""
    if service in self.services:
      self.services.remove(service)
    else:
      pass #couldn't find the service
  
  def add_item(self,item,quantity = 1):
    """Add a number of items to the goods list for this location."""
    if item in self.goods:
      pass #add more inventory
    else:
      self.goods.append(item)
  
  def del_item(self,item,quantity = 1):
    """Remove a number of items from the goods list for this location."""
    if item in self.goods:
      pass #remove quantity from goods
    else:
      pass #couldn't find that item in inventory
  
  def add_job(self,job):
    """Add a job to the jobs list for this location."""
    if job in self.jobs:
      pass #job already exists, set it available?
    else:
      self.jobs.append(job)
  
  def del_job(self,job):
    """Remove a job from the jobs list for this location."""
    if job in self.jobs:
      self.jobs.remove(job)
    else:
      pass #job not found
  
  def available_jobs(self):
    """Return a list of the available jobs for this location."""
    available_jobs = []
    for job in jobs:
      if job.is_available():
        available_jobs.append(job)
    return available_jobs
  
  def apply_for_job(self,player,job):
    """Try to give this player the job if it satisfies all requirements.
    Return True if it was successful, or a string with a reason if not."""
    return job.hire_player(player)
