# store orignal given money 
print("How much money was given?")
moneyGiven = float(input())
print("How much money did you use?")
Expenses = float(input())

extraMoney = moneyGiven - Expenses

if extraMoney < 0:
	print("please make sure that your money given is more than money used")

print(extraMoney) 