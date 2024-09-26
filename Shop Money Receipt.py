import os

from colorama import init
init()

from colorama import Fore


allItems =[]
totalCost = 0

def checkOutPayment():
  for rows in allItems:
    print(rows)
  print(f"total cost: ${totalCost}")

  typePay = input("Do you want to pay in debit, credit, or gift card?: ")
  print(f"{totalCost} payed in full via {typePay}")
  print("balance = $0")
  print(Fore.GREEN + "THANK YOU FOR SHOPPING WITH US TODAY")
  exit("Have a nice day")


while True:
  os.system("clear")
  print("Press 'n' to end the process and to checkout")
  print("Please scan items to begin: ")
  whatBought = input("Tell me the item name: ")
  if whatBought != "n":
    whatPrice = float(input("What is the price?: "))
    allItems.append([whatBought, whatPrice])
    totalCost = totalCost + whatPrice

  if whatBought == "n":
    checkOutPayment()
  else:
    continue
