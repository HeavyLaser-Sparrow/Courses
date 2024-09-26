totalMoney = 0

class inventory():
    
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    
    def __len__(self, price):
        global totalMoney
        totalMoney = totalMoney + self.price
        return totalMoney
    
    def __str__(self):
        return f"{self.id} {self.name} {self.price}"



"""
print(blueberry)
print(strawberry)
print(apple)
print(phone)
"""