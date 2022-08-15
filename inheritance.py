class Player:
    fees = 1000
    def __init__(self, name, age, role):
        self.name = name
        self.role = role
        self.age = age

    def address(self):
        add = f" Name:{self.name}\n Age : {self.age}\n Role: {self.role}\n Fees: {self.fees}" 
        return add  

#inheritance    
class Team(Player):
    fees = 1300
    def __init__(self, name, age, role,year): 
        super().__init__(name, age, role)
        self.year = year

P1 = Team('Hari', 19, 'Fast Bowler',2020)
P2 = Team('Arun', 20, 'Batsman',2019)

print(P1.year)
#print(Team.__mro__)