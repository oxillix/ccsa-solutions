# https://dodona.ugent.be/nl/courses/399/series/8796/activities/936085588


class QueueList:

  class knoop:

    def __init__(self,data=None, volgende = None):
      self.data = data
      self.volgende = volgende

  def __init__(self):
      self.kop=None
      self.staart = None

  def empty(self): 
    return self.kop is None
    
  def enqueue(self,x):
    hulp = self.knoop(x)
    hulp.data = x
    if self.kop is not None:
        self.staart.volgende = hulp
    else:
          self.kop = hulp
    self.staart = hulp

  def dequeue(self):
      x = self.kop.data
      self.kop = self.kop.volgende
      if self.kop is None:
        self.staart = None
      return x
  def front(self):
      return self.kop.data
 
  def invert(self):
    vorig = None
    volgende = None
    huidig = self.kop

    while huidig is not None:
      volgende = huidig.volgende
      huidig.volgende =vorig
      vorig = huidig
      huidig = volgende
    self.kop,self.staart = self.staart,self.kop  

  