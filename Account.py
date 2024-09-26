allAccountNames = {143: "Joe", 674: "Asdf", 718: "NotPhoney"}

class vault():
    
    def __init__(self, id, money):
        self.id = id
        self.money = money

    def deposit(self, money, amount):
        self.money = self.money + amount

    def withdraw(self, money, amount):
        self.money = self.money - amount

    def __str__(self):
        return f"ID: {self.id}, Money: {self.money}"

def changeMoney(remId):
    realName = allAccountNames[remId]

    ask = input("Do you want to change the amount? [y/n]: ").lower()

    if ask == "n":
        print("Ok, have a good day")
        exit()
    else:
        pass

    signAge = input("Do you want to add or subtract the amount?[+/-]: ")
    if signAge == "+":
        amount = int(input("How much money do you want to deposit?: "))
        realName.deposit(amount)
    elif signAge == "-":
        amount = int(input("How much money do you want to withdraw?: "))
        realName.withdraw(amount)
    else:
        print("Sorry, I did not understand.")
        print("Please try again later")
