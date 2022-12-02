# https://dodona.ugent.be/nl/courses/399/series/8796/activities/2064046031

class StackList:

    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende

    def __init__(self):
        self.top = None

    def empty(self):
        return self.top is None 

    def push(self, data):
        hulp = self.Knoop(data)
        hulp.volgende = self.top
        self.top = hulp
    def peek(self):
        return self.top.data

    def pop(self):
        x = self.top
        self.top = x.volgende
        return x.data

        



    
