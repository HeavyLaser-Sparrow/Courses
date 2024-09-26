import os

from StoreInventory import inventory

from Money import account

from CustomerAccount import bankAccount2

from customerIDdesk import addCustomer

from customerIDdesk import customerIDs


store = account(1000)

zero = bankAccount2(100)
one = bankAccount2(100)
two = bankAccount2(100)
three = bankAccount2(100)
four = bankAccount2(100)
five = bankAccount2(100)
six = bankAccount2(100)
seven = bankAccount2(100)
temporary = bankAccount2(100)

totalCost = 0
totalBought = []

blueberry = inventory(1, "blueberry", 3)
strawberry = inventory(2, "strawberry", 4)
apple = inventory(3, "apple", 5)
phone = inventory(4, "phone", 100)
blanket = inventory(5, "blanket", 23)
car = inventory(6, "car", 1000)
ramen = inventory(7, "ramen", 1)
cookies = inventory(8, "cookies", 10)
darkChocolate = inventory(9, "dark chocolate", 1)
box = inventory(10, "box", 1)

print(f"{blueberry}\n{strawberry}\n{apple}\n{phone}\n{blanket}\n{car}\n{ramen}\n{cookies}\n{darkChocolate}\n{box}")

whichCustomer = int(input("Input your customer ID to begin (enter '000' to get a new one): "))

if whichCustomer in customerIDs:
    pass
elif whichCustomer == 000:
    addCustomer()
else:
    print("Invalid customer ID")
    exit("Please go to the desk to get your customer ID")

while True:
    os.system("clear")
    print(f"{blueberry}\n{strawberry}\n{apple}\n{phone}\n{blanket}\n{car}\n{ramen}\n{cookies}\n{darkChocolate}\n{box}")

    askCustomer = input("What do you want to buy? (press 'n' to checkout): ")
    if askCustomer == "n":
        break
    elif totalCost > 100:
        exit("You do not have enough money to complete the purchases. Please try again later.")
    else:
        continue

    if askCustomer == "blueberry":
        totalCost += blueberry.price
        totalBought.append(askCustomer)
    elif askCustomer == "strawberry":
        totalCost += strawberry.price
        totalBought.append(askCustomer)
    elif askCustomer == "apple":
        totalCost += apple.price
        totalBought.append(askCustomer)
    elif askCustomer == "phone":
        totalCost += phone.price
        totalBought.append(askCustomer)
    elif askCustomer == "blanket":
        totalCost += blanket.price
        totalBought.append(askCustomer)
    elif askCustomer == "car":
        totalCost += car.price
        totalBought.append(askCustomer)
    elif askCustomer == "ramen":
        totalCost += ramen.price
        totalBought.append(askCustomer)
    elif askCustomer == "cookies":
        totalCost += cookies.price
        totalBought.append(cookies)
    elif askCustomer == "dark chocolate":
        totalCost += darkChocolate.price
        totalBought.append(askCustomer)
    elif askCustomer == "box":
        totalCost += askCustomer.price
        totalBought.append(askCustomer)
    else:
        print("Invalid Choice")

        
for row in totalBought:
    print(totalBought[row])

print(f"Balance: {totalCost}")

if askCustomer == 123:
    zero.withdraw(totalCost)
elif askCustomer == 465:
    one.withdraw(totalCost)
elif askCustomer == 980:
    two.withdraw(totalCost)
elif askCustomer == 100:
    three.withdraw(totalCost)
elif askCustomer == 101:
    four.withdraw(totalCost)
elif askCustomer == 707:
    five.withdraw(totalCost)
elif askCustomer == 104:
    six.withdraw(totalCost)
elif askCustomer == 657:
    seven.withdraw(totalCost)
else:
    temporary.withdraw(totalCost)


store.deposit(totalCost)