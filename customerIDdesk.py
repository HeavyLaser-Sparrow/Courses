import random

customerIDs = [["zero",123], 
               ["one", 465], 
               ["two", 980],
               ["three", 100], 
               ["four", 101], 
               ["five", 707], 
               ["six", 104], 
               ["seven",657]]

def addCustomer():
    while True:
        newId = random.randint(0,999)
        if newId not in customerIDs:
            customerIDs.append(["temporary", newId])
            print(f"Your new customer ID is {newId}")
            break
        else:
            continue
