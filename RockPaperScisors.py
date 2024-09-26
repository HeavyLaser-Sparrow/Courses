import random 
shapes = ["Rock", "Paper", "Scissors"]

def goAgain(): 
  print("Do you want to go again? Y/N: ")
  if goAgain == "Y": 
    RockPaperScissors()
  else: 
    exit("Ok")

def RockPaperScissors():
  compChoice = random.choice(shapes) 
  #print(compChoice)
  pChoice = input("Choose Rock, Paper, or Scissors: ")
   
  if compChoice == pChoice: 
    print(compChoice)
    print("We tied")
  
  elif compChoice == "Rock" and pChoice == "Paper": 
    print(compChoice)
    print("You won")
  elif compChoice == "Paper" and pChoice == "Rock": 
    print(compChoice)
    print("I won")
  
  elif compChoice == "Rock" and pChoice == "Scissors": 
    print(compChoice)
    print("I won")
  elif compChoice == "Scissors" and pChoice == "Rock": 
    print(compChoice)
    print("You won")

  elif compChoice == "Paper" and pChoice == "Scissors": 
    print(compChoice)
    print("You won")
  elif compChoice == "Scissors" and pChoice == "Paper": 
    print(compChoice)
    print("I won")

while True:
  RockPaperScissors()