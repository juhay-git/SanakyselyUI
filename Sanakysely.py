import random

class Sanakysely:
    def __init__(self):
        self.sanasto = {'apina': 'apa', 
           'banaani':'banan',
           'juusto' : 'ost',
           'kakku' : 'kaka',
           'kala' : 'fisk',
           'kirja' : 'bok',
           'lintu' : 'fågel',
           'porkkana' :'morot',
           'punajuuri' :'rödbeta',
           'riisi':'ris'
           }

        self.avaimet = list(self.sanasto.keys())
        self.__oikeat = 0
        self.__vaarat = 0
        self.__sana_nro = 0

    @property
    def oikeat(self):
        return self.__oikeat
    
    @property
    def vaarat(self):
        return self.__vaarat
    
    @property
    def sananro(self):
        return self.__sana_nro

    def nollaa(self):
        self.__oikeat = 0
        self.__vaarat = 0
        self.__sana_nro = 0

    def seuraavaSana(self):
        self.kysyttava_sana = random.choice(self.avaimet)
        self.__sana_nro += 1
        return self.kysyttava_sana
    
    def tarkista(self, vastaus):
        if self.sanasto[self.kysyttava_sana] == vastaus.lower():
            self.__oikeat += 1
        else:
            self.__vaarat += 1