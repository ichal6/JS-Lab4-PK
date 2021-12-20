# YOUR CODE HERE
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


class PrzechowywaczMonet:
    def __init__(self, list_of_types):
        self._list_of_types = list_of_types
        self._list_of_coins = []
    
    def add_coin(self, coin):
        if(isinstance(coin, Moneta)):
            if(coin.get_value() in self._list_of_types):
                self._list_of_coins.append(coin)
            else:
                print("Nieznany nominał")
        else:
            print("Przesłany obiekt nie jest monetą")
    
    def get_sum_all_coins(self):
        sum_of_coins = Decimal(0)
        for coin in self._list_of_coins:
            sum_of_coins += coin.get_value()
        return sum_of_coins
    
    def get(self, nominal_of_coins):
        (coin) = [(coin, self._list_of_coins.pop(i)) for i, coin in enumerate(self._list_of_coins) if nominal_of_coins==coin.get_value()]
        return coin
    
    def wszystkieMonety(self):
        sorted_list = self._list_of_coins.copy()
        sorted_list.sort()
        for coin in sorted_list:
            yield coin

class Skarbonka(PrzechowywaczMonet):
    _currency_type = ''
    
    def __init__(self, currency_type):
        self._list_of_coins = []
        Skarbonka._currency_type = currency_type
    
    def add_coin(self, coin):
        if(isinstance(coin, Moneta)):
            if(coin.currency == Skarbonka._currency_type):
                self._list_of_coins.append(coin)
            else:
                print("Nieznana moneta")
        else:
            print("Przesłany obiekt nie jest monetą")
    def get_sum_of_coins(self):
        sum_of_coins = Decimal(0)
        for coin in self._list_of_coins:
            sum_of_coins += coin.get_value()
        return sum_of_coins
    
    def get(self, nominal_of_coin):
        raise NotImplementedError('Nie można wyciągnąć pojedyńczej monety!')

eur = Moneta(0.05, "EUR")        
pln1 = Moneta(0.5, "PLN")
pln2 = Moneta(0.2, "PLN")

sk = Skarbonka("PLN")

possible_values = [Decimal(0.01), Decimal(0.02), Decimal(0.05), Decimal(0.1), Decimal(0.2), Decimal(0.5),
                     Decimal(1), Decimal(2), Decimal(5)]

sk = PrzechowywaczMonet(possible_values)

sk.add_coin(pln1)
sk.add_coin(pln2)

# print(sk.get_sum_of_coins())

g_sk = sk.wszystkieMonety()

for i in g_sk:
    print(i)
        

# raise NotImplementedError()