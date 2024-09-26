# secret
import os  
my_secret = os.environ['The Hobbit'] 

if my_secret: 
    print("You can start the game now")
else: 
    print("You are not the owner")

# code
stuffHave = ["Wagon", "Ox", 10, "<-- Lb of Food", "Map"]

def know():
  Have = "Do you want to know what you have Y/N: "
  stuff = input(Have)

  if stuff == "Y": 
    print(stuffHave)


def game(): 
# defining parts 
  """
  Lanswer1 = int(input("Choose a number between 1 - 100, and I will try to guess it: "))
  Lanswer2 = int(input("Choose another number from 1 - 600, and multiply it to the first number: "))
  L = Lanswer2 + Lanswer1 
  G = Lanswer2 - Lanswer1
  print("Ha ha, I have tricked you into giving me the things to input into the system.")

# game start part 1
  if G < 200:
    print("Sorry, You can't start right now") 
    exit(1) 

  """
    
# game start 2
# print("")


  print("Hello, you want to travel west to try to strike it rich and/or get yourself a large peice of land. You have a wagon, an ox, a chest of food, and a book with a map. ")

  print("You start driving your ox for a mile or two, when there are 2 paths that fork. One path smells of moldy bread, while the other smells of bison.")  
  theCrossing1 = input("Which path do you choose, bread or bison?: ")

  if theCrossing1 == "bread": 
      print("You walk for about a hundred miles. Your ox has run away and you are left without food. You have failed, so you try to walk back to town.") 
      stuffHave[1] = "No ox" 
      exit(1)
  elif theCrossing1 == "bison": 
      print("You had traveled about 50 miles, when you decided to merge with another party. Together, your party heads west. Good job, you have chosen well.") 
      know() 
  
# game start 3
  print("You and your group have reached another fork in the road. Your group wants to head through the mountains.")
  theCrossing2 = input("Choose, group or own?: ")

  if theCrossing2 == "group": 
      print("You move with the group into the mountains. You are very hungry when you reach the foothills of the mountains in the winter. You wish you hadn't joined the DONNER PARTY! ") 
      exit(1)
  elif theCrossing2 == "own": 
      print("You decide to leave the party and go by yourself on the trail, you live.") 
      stuffHave[2] = 1 
      know()

# game start 4
  print("You have now eaten 9Lb of food. After 50 miles of walking, you see a huge tree. Do you want to pick the fruit or keep moving? Input pick to pick the fruit or input move if you want to keep moving and ignore the fruit.") 
  fruit = input("Pick fruit or keep moving?: ") 

  if fruit == "fruit": 
    print("You pick the fruit and move on, you now have 5Lb of food.")  
    stuffHave[2] = 5 
    know()
  elif fruit == "move": 
    print("You ignore the fruit. After you run out of food, you turn back and try to go home") 
    exit(1) 

# game start 5 
  print("You have know eaten 4Lb of food when you see a huge herd of bison. Do you want to hunt the bison?")
  stuffHave[2] = 1
  bison = input("Y/N: ")
  
  if bison == "Y": 
    print("You hunt and are able to get 50Lb of food.")
    stuffHave[2] = 51 
    know() 
  elif bison == "N": 
    print("You head back home when you go hungry.") 
    exit(1)

# game start 6 
  print("You have now eaten 20Lbs of food after you rest at night. You wake up to the sound of wolves. They have eaten those 20Lbs of food. Do you want to keep going, or do you want to hunt some more for more food?") 
  wolves = input("move, or follow?: ")
  stuffHave[2] = 31 
  if wolves == "follow": 
      print("You now have 60 more Lbs of food. You leave and keep heading to the west.") 
      stuffHave[2] = 91 
      know() 
  elif wolves == "move": 
      print("You leave the plains and keep heading west.")
      stuffHave[2] = 31  
      know()

# forest fire attack 
  def forestFire():
    print("You go to sleep. You wake up to the sound of fire crackling and decimating trees. You rush to your ox. You have all of your stuff with you except your food. How much food do you want to take before you leave?")
    print(stuffHave[2])
    food = int(input()) 

    if food < 40: 
        print("You succeed in getting" + str(food) + "Lbs of food.") 
        stuffHave[2] = food
    else: 
        print("You try to get that much food, but you fail. You now have 5Lbs of food.") 
        stuffHave[2] = 5


# game start 7 
  print("As you keep moving west, you see that the air is drier than normal. Do you want to camp out here, or somewhere else? Input stay, to stay or move, to go somewhere else.") 
  camp = input("Stay, or move?: ")
  if camp == "move": 
    print("You decide to rest somewhere else. At night, some wolves steal 10Lbs of food.")
    stuffHave[2] = stuffHave[2] - 30 
  elif camp == "stay": 
    forestFire() 

# game start 8



game()    
