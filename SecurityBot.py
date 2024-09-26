knownUsers = {"Tom": "7368", "Bob": "1943", "Dan": "3098", "Tree": "4147", "Port": "1047", "Fred": "4308", "King": "2819", "Carrot": "7612", "Tube": "5932", "Marker": "9720"} 
overideCode = {"LordCanoe": "Tictactoeandtravisstartwiththesameletter"}

# print(len(knownUsers))
print(knownUsers)
while True: 
  x = input("Are you a user? Y/N: ").lower() 
  if x == "y": 
    print("Hello, My name is Travis")
    name = input("What is your name?: ").strip().capitalize()
    if name in knownUsers: 
      print("Hello {}".format(name))  
      numberCode = input("Tell me your code {}: ".format(name))
      
      if numberCode == knownUsers[name]: 
        print("You are all signed in, {}".format(name)) 
        exit("Yay! I did my job") 
      else: 
          while True: 
            print("You are an intruder!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") 
      
    else:
      print("That name isn't stored.") 
      exit("Sorry")
 
  if x == "n": 
    print("Ok")
    shutDown = input("Are you a lord? Y/N: ")
    if shutDown == "Y": 
      Travis = input("What is the username?: ") 
      if Travis in overideCode: 
        Sivart = input("What is the code?: ")

        if Sivart == overideCode[Travis]: 
          print("shutting down") 
          exit("You have shut down Travis forever") 
        else: 
          while True: 
              print("Forget you ever saw anything!!!!!!!!!") 
      else: 
          while True: 
              print("Forget you ever saw anything!!!!!!!!!!!!!!!")

    else: 
      print("Forget you ever saw anything!!!!!!")
