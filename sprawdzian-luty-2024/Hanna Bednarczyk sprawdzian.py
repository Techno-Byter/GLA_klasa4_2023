import re

#A

def draw_spruce(x): #x is the number of layers
    spaces = x - 1 # number of spaces before first star of the layer
    stars = 1 # number of stars on given layer
    output = ""
    while spaces >= 0:
        output += (" " * spaces) + ("*" * stars) + "\n"
        stars += 2
        spaces -= 1
    output += (" " * (x-1)) + "|" + "\n"
    return output

print(draw_spruce(8))

#B

with open("numery.txt", "r") as file:
    lines = file.readlines()
data_t = []
data = []
for line in lines:
    line = line.split()
    data_t.append(line)
for a in data_t:
    data.append(a[0])
#print(data)
#search for three+ consecutive chars
counter_triple = 0
for a in data:
    x = re.search(r"(\d)\1\1",a) #r = raw (uproszcza przeszukiwanie); \d = dowolna cyfra; \1\1 = jak znajdziesz cyfrę, to sprawdź czy za nią są jeszcze 2 takie same
    if x:
        counter_triple += 1
print(counter_triple)

Families = {}

for a in data:
    family = len(a)
    if family in Families:
        Families[family] += 1
    else:
        Families[family] = 1
Sorted_Families = dict(sorted(Families.items()))
print(len(Sorted_Families.keys()))

#C

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount
    def get_balance(self):
        print(self.balance)

dziunia = BankAccount("Jakas Dziunia", 0)
dziunia.deposit(1500100900)
dziunia.withdraw(1)
dziunia.get_balance()

zenek = BankAccount("jakis zenek", -1)

class Bank:
    def __init__(self):
        self.accounts = []
    def add_account(self,account):
        self.accounts.append(account)
    def get_total_balance(self):
        sum = 0
        for a in self.accounts:
            sum += a.balance
        print(sum)
    def display(self):
        for a in self.accounts:
            print(a.owner)

bank = Bank()

bank.add_account(dziunia)
bank.add_account(zenek)
bank.display()
bank.get_total_balance()
