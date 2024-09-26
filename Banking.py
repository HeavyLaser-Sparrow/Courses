instructions = input("Welcome to the bank. Are you a user Y/N?: ") 

bankUsersCode = {"Tom": "3097", "Ted": "5862", "Bob": "2726", "Pencil": "2908"}
bankUsersMoney = {"Tom": 3497, "Ted": 980, "Bob": 2800, "Pencil": 6475849} 

print(bankUsersCode)

def Security(): 
  print("Hello, My name is Travis")
  name = input("What is your name?: ").strip().capitalize()
  
  if name in bankUsersCode: 
    print("Hello {}".format(name))  
    numberCode = input("Tell me your code {}: ".format(name))
      
    if numberCode == bankUsersCode[name]: 
      print("You are all signed in, {}".format(name)) 
    else: 
      while True: 
        print("You are an intruder!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") 
      
  else:
    print("That name isn't stored.") 
    exit("Sorry") 

def Bank(): 
  username = input("What is your name again?: ")
  print("You have {} dollars".format(bankUsersMoney[username]))
  given = input("Would you like to take away or add money? Y/N and take/add: ") 
  
  if given == "Y, take": 
    take = float(input("How much money would you like to take?: ")) 
    newTake = bankUsersMoney[username] - take
    if newTake > 0: 
      print("You now have {} dollars".format(newTake))
    elif newTake == 0: 
      print("You now have {} dollars".format(newTake))
    else: 
      print("You don't have that much money. You are now signed out")
    exit("Come back soon.")
  elif given == "Y, add": 
    add = float(input("How much money would you like to add?: "))
    newAdd = bankUsersMoney[username] + add 
    print("You now have {} dollars".format(newAdd))
    exit("Come back soon.")
  elif given == "N": 
    exit("Ok, come back soon")
    


if instructions == "Y":
  Security()
  Bank()
else: 
  print("Ok, come back next time") 
  
