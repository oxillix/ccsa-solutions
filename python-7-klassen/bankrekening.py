class BankRekening:
    def __init__(self, naam, reknr, startBedrag=0):
        self.naam = naam
        self.rekenignummer = reknr
        self.bedrag = startBedrag
    
    def __str__(self):
        return f'{self.naam}, {self.rekenignummer}, bedrag: {self.bedrag}'
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.naam}', '{self.rekenignummer}', {self.bedrag})"

    def storten(self, n):
        self.bedrag += n
    
    def afhalen(self, n):
        self.bedrag -= n