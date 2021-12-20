# YOUR CODE HERE
# !!!Przerobic kod!!!
import random 
from decimal import *

class Moneta:
    possible_values = [Decimal(0.01), Decimal(0.02), Decimal(0.05), Decimal(0.1), Decimal(0.2), Decimal(0.5),
             Decimal(1), Decimal(2), Decimal(5)]
    def __init__(self, value, currency):
        self.currency = currency
        self.value = 0
        for v in  Moneta.possible_values:
            if v == value:
                self.value = v
                return
        raise ZlyNominalException(value="Zły nominał", lista_monet=[])
    
    def get_value(self):
        return self.value
    
    def __str__(self):
        return f"Moneta o walucie {self.currency} i wartości {self.value}"
    def __repr__(self):
        return f"Moneta({self.value}, {self.currency})"
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value

def JednorekiBandyta(ile:float):
    tablicaWartosci=[0.01, 0.02]
    suma = 0.0
    while round(suma, 2) < round(ile, 2):
        x=random.choice(tablicaWartosci)
        if x <= ile - suma:
            yield Moneta(x, "PLN")
        else:
            x = 0.01
            yield Moneta(x, "PLN")
        suma+=x


y=JednorekiBandyta(100)

suma = 0

for x in y:
    #print(round(x.value, 2))
    suma+=x.value

print(suma)