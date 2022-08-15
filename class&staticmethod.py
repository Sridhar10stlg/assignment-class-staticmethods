from zoneinfo import available_timezones

from urllib3 import Retry


class Player:
    fees = 1000
    def __init__(self, name, age, role):
        self.name = name
        self.role = role
        self.age = age

    def address(self):
        add = f" Name:{self.name}\n Age : {self.age}\n Role: {self.role}\n Fees: {self.fees}" 
        return add  
    
    def pay_fees(self, amount):
        self.fees = self.fees-amount
    
    #classmethod
    def change_fees(cls, amount):
        cls.fees = amount

    #classmethod
    def player_data(cls, data):
        name, age, role = data.split(",")
        return cls(name, age, role)

    #static method
    def category(ctgy):
        avail_category = ['Batsman','Bowler','All-rounder']
        if ctgy in avail_category:
            return True
        return False

P1 = Player('Hari', 20, 'Fast Bowler')
P2 = Player('Arun', 20, 'Batsman')

P1.change_fees(1300)


print(P1.fees)

data = 'vijay, 22, Batsman'
P3 = Player.player_data(data)

print(P3.name)
print(P2.category('Batsman'))