'''
Notes: finish both dinoAdventure and desert Adventure
'''





def dinoAdventure():
    print("Hello, dinoAdventure is still under construction, please play the desertAdventure game or the wizardAdventure game. If you have already those games, then come back later.")





################################################### WARNING: GAME 2 STARTS HERE!!!!!!! ##################################################################

def desertAdventure(): 
    desertResources = [30, 20, "Map", "item space 1", "item space 2", "item space 3", "Item space 4","Harm space 1", "Harm space 2"]
    def checkResources():
        seeCheck = input("Do you want to see what's in your bag? [y/n]: ").lower()
        if seeCheck == "y":
            print(f"You have {desertResources[0]} water bottles, {desertResources[1]} food packs, {desertResources[2]}, {desertResources[3]}, {desertResources[4]}, {desertResources[5]}, {desertResources[6]}, {desertResources[7]}" )

    def drinkWater():
        toDrink = input("Do you want to drink a bottle of water? [y/n]: ").lower()
        if toDrink == "y":
            if desertResources[0] > 0:
                desertResources[0] = desertResources[0] - 1
                print("You reach into your bag, pull out a water bottle, and take a long, satisfying drink.")
            elif desrtResources[0] == 0:
                print("You reach in to drink some water, but you have run out of water.")

    def eatFood():
        toEat = input("Do you want to drink a bottle of water? [y/n]: ")
        if toEat == "y":
            if desertResources [1] > 0:
                desertResources[1] = desertResources[1] - 1
                print("You reach into your bag, pull out a food pack, and eat.")
            elif resources[1] == 0:
                print("You reach into your bag, but you have run out of food.")

    def modeStay():
        print("You start to look through the wreckage for more resources.")
        print("Eventually, you find a emergency radio (only enough power for 5 uses) and 5 emergency flares. You also find 3 water bottles and 4 food packs")
        desertResources[0] = desertResources[0] + 3
        desertResources[1] = desertResources[0] + 4
        desertResources[3] = 5
        desertResources[4] = 6
        drinkWater()
        eatFood()
        print("You lay down on the ground and go to sleep. When you wake up, a small scorpion is crawling up your arm.")
        scorpionChoice = input("Do you want to brush it off, or let stay still and let it crawl off? [brush or ignore: ]").strip().lower()
        if scorpionChoice == "brush":
            print("You brush the scorpion off, but not before it stings you. You feel the venom flowing though your body.")
            exit("The world suddenly goes dark. YOU HAVE FAILED!")
        elif scorpionChoice == "ignore":
            print("You try to ignore the scorpion. After around 30 minutes, the scorpion crawls off and continues its journey.")

# finish stay code ^


    def modeMove():
        print("After looking at your map, you see that you have crashed in the exact middle of the desert. You set off toward civilization.")

# finish move code ^



    print("You begin your adventure in a desert. As you fly over the desert, you admire the landscape below, suddenly, the plane nosedives down and crashes, luckily, you survive.")
    print("Your adventure begins now.")
    print(desertResources)
    print("Warning: You only have a limited amount of space in your bag, use it wisely. Need to drink 1 bottle and eat 2 food packs a day to survive")
    whatNext_1 = input("Do you want to stay at the crash site and hope someone finds you (you are expected elsewhere in 1 week), or move around and look for civilization? [move or stay]: ")

    '''
    # create new function for moving towards civilization
    if whatNext_1 == "move":
        modeMove()
    '''
    
    # create new function for staying at crash site and waiting for help
    if whatNext_1 == "stay":
        modeStay()





    

################################################### WARNING: GAME 3 STARTS HERE!!!!!!! ##################################################################

def wizardAdventure():
    import random
    Items = ["Staff", 50, "<-- Gold Coins", "Magic Book V1", "Map", "item space 1", "item space 2", "item space 3", "harm space 1", "harm space 2"]
    shopItems = {
      "Finding stick": 10, 
      "Healing water": 20, 
      "Magic Book V2": 30, 
      "Wood Sword": 100, 
      "Metal Sword": 40}

    def know(): 
      knowNow = input("Do you want to know what you have in your inventory? y/n: ") 
      if knowNow == "y": 
        print(Items)
      else: 
        print("ok")

    # didn't finish
    # attack by monster
    def throughMountain(): 
      print("You steel your resolve and start walking through the narrow path that snakes through the mountain. As you walk down the path, you hear a growl. Your curiosity urges you to go towards the monster, but your common sense tells you to stay away.")
      scaryGrowl = input("Do you want to go 'towards' the monster, or 'away' from the monster?: ")
      if scaryGrowl == "towards": 
        print("Afraid, you walk towards the sound. Eventually, you reach the source. It is a huge sleeping dragon. Its scales glimmer in the faint sunlight. You can make out its green saliva, sharp teeth, bat-like wings, and short horns. Do you want to fight it or befriend it.")
        dragonChoice = input("'Fight' it or 'befriend' it?: ").lower()
        if dragonChoice == "befriend": 
          print("You try to befriend it. You extend your arm out for it to smell. The dragon comes closer. You sense that it means no harm.")
          exit("The Dragon suddenly lashes out and bites your arm off.")
        elif dragonChoice == "fight": 
          print("You start fighting the dragon. After a long battle, you are both tired. Now, you look at the dragon in admiration of iits courage, and the dragon does the same thing. Then, the dragon turns into a gem, and says, 'I will come and help you in any battle, but only one battle.'")
          Items[7] = "dragon gem"
          know()    
          print("You continue on your way and pass the mountain.")
      elif scaryGrowl == "away": 
        print("You decide to run away quickly. As you run, you hear the sound getting louder. You look behind you and you see a huge dragon. It catches up to you and tackles you.")
        exit("You were eaten by the dragon")
        

    # rockslide happens
    def aroundMountain():
      print("You decide to take the safe path and move around the mountain. You steel your resolve and walk around the mountain, keeping close to its steep slopes. Soon, you are halfway around the mountain. You hear a rumble. Suddenly, 50 large rocks come barrelling towards you.")
      if Items[5] == "conch": 
        print("You pull out the conch and blow in it. The sound is so loud, that it breaks the rocks into millions of tiny peices. Seeing you are safe from danger, you put the conch away and continue on your journey.")
      elif Items[1] == 150: 
        exit("You have no magic items. You only have gold. Gold can't save you now. You are crushed by the landslide.")
      elif Items[5] == "Finding Stick": 
        print("You are crushed by the boulders.")
        exit("GAME OVER")
      elif Items[5] == "Metal Sword" or "Magic Book V2": 
        print("You use the power of the Magic Book V2 or Metal Sword to stop the onslaught of boulders comming at you. Once you have dealt with that, you continue on your journey.")
      elif Items[5] == "Healing Water": 
        print("You are crushed by the onslaught of boulders. A boulder smashes into your pouch and breaks the Healing Water's container. Then, the Healing Water reivigorates you. You continue on your quest with a limp.")
        Items[5] == "item space 1"
        Items[8] == "limp"

    print("You have recently been called on by your king. To you, he is a very kind person, but he has been betrayed many times. As you walk through the hall leading to the throne room, you wonder why you called you. You walk into the throne room.")
    print("The king says, 'Anorack, you have proven yourself worthy of going on a quest. Choose which quest you would like to go on.' You decide to go on the forbidden stone quest. With the forbidden stone, you could protect the entire kingdom. You walk away, but you don't see the king's darker interests.")
    print("Very little is known about the forbidden stone. A historian walks up to you and gives you hundreds of scrolls to familiarize yourself with. You take the scrolls cautiously and walk away. You read the scrolls. A long time ago, an old powerful wizard and his apprentice went on an adventure to find the forbidden crystal. A crystal that helps grant the heart's wish. While on the journey, the apprentice was secretly given a powerful stone. It was given to him by an old man who had attached it to the hilt of a sword. Once the master and the apprentice found the crystal, the master attached the gem to his staff. He suddenly became all powerful, so powerful that the master decided to destroy his apprentice. However, the apprentice swung his sword and trapped the power of the old wizard, his staff, and his magic crystal. Then, the apprentice hid the sword in his grave. Your mission is to find the sword and give it to the king, so he can use its power to protect the kingdom, ")
    # easter egg: Enlightenment
    egg = input("and use his powers for good: ")
    if egg == "?": 
      print("This would have been a very not-Montesquieu thing to do, and also unEnlightenment. This is seen in Monetesque's Spirit of the Laws.")

    print("You walk out of the city walls. The only items you have are your staff, 50 gold coins, a map, and a book of spells. Eventually, you find an old cottage-like shop. An old person says, 'Hello, would you like to buy anything from my shop?: '")
    shop = input("Do you want to buy anyting from his shop? (V = version) y/n: ").lower()
    if shop == "y": 
      print(shopItems)
      buy = input("what would you like to buy(1): ").lower()
      if buy == "finding stick": 
        Items[1] = Items[1] - 10 
        Items[5] = "finding stick"
        print("You have" + str(Items[1]) + "gold coins       left")
      elif buy == "healing water":
        Items[1] = Items[1] - 20 
        Items[5] = "healing water"
        print("You have" + str(Items[1]) + "gold coins left")
      elif buy == "magic book v2": 
        Items[1] = Items[1] - 30 
        Items[5] = "magic book v2"
        print("You have" + str(Items[1]) + "gold coins left")
      elif buy == "wood sword":
        Items[1] = Items[1] + 100
        Items[5] = "you have gained 100 gold coins, you have used this space for that much gold"
        print("You have" + str(Items[1]) + "gold coins left")
      elif buy == "metal sword": 
        Items[1] = Items[1] - 40
        Items[5] = "metal sword"
        print("You have" + str(Items[1]) + "gold coins left")
      elif buy == "piggy" or "ralph" or "jack": 
        print("You say you won't buy anything. He smiles and gives you a conch.")
        Items[5] = "conch"
      else: 
        exit("You failed because you didn't answer and the old man attacked you with his           stick")
    elif shop == "n": 
      print("You answer no, and the old man flies     into a rage and hits you with his stick.")
      exit("You failed")

    print("The old man thanks you for buying an item from his shop. He gives you a small, thin ring. You accept it and thank it. You add it to your backpack.")
    Items[6] = "mysterious ring"

    know()

    print("You continue on your journey. You continue walking towards your goal. Eventually, you reach a huge mountain. Which do you choose?")
    mountainChoice = input("Do you want to go 'around' the mountain, or 'through' the mountain: ").lower() 
    if mountainChoice == "around": 
      aroundMountain()
    elif mountainChoice == "through":
      throughMountain()

    print("You successfully get past this mountain.")

    def Hangman():
      print("Let us play the brain/monster version of Hangman!")
      print("In here, guess random letters, and put all of your answers together to  make a final answer")
      print("You have 12 lives") 
      
      DictionaryOfWords = ["wait", "fire", "wood","wire", "what", "case", "tore", "bait", "acid", "area", "away", "that", "this", "tote", "hole", "worm", "lamb", "mane", "main", "lion", "mule", "akin", "bear", "need", "bind", "thou", "aged", "awry", "also", "ball", "base", "bird", "boat", "belt", "bond", "stat", "burn", "call", "city", "coat", "come", "cope", "cash", "club", "dawn", "diet", "coke", "days", "data", "debt", "desk", "does", "dose", "crew", "does", "done", "fast", "feed", "fine", "fish", "five", "fort", "gold", "glad", "golf", "gift", "gave", "half", "hair", "hare", "head", "held", "hear", "hold", "hope", "kick", "home", "host", "jack", "item", "king", "know", "knee", "lake", "laid", "logo", "lord", "lost", "feif", "list", "loss", "lost", "luck", "mood", "moon", "must", "near", "navy", "need", "mode", "more", "milk", "mine", "move", "poll", "plot", "rail", "race", "rose", "root", "roof", "sake", "said", "seen", "seed", "sent", "tank", "task", "sole", "team", "tend", "suit", "surf", "tech", "tape", "text", "tree", "tone", "tool", "pace"]
      
      # word
      randomWord = random.choice(DictionaryOfWords)
      # print(randomWord) 
      
      # word's lines
      wordCount = len(randomWord)
      
      
      underscores = "_" * wordCount   
      print(underscores)
      
      # game start
      def startGame(): 
        
        game = 12 
        while game > 0: 
          choice = input("\nMake a choice: ").lower()
      
          A = randomWord[0]
          B = randomWord[1] 
          C = randomWord[2]
          D = randomWord[3] 
      
          if choice == randomWord: 
            print("Good job")  
            break
          
          elif choice != randomWord:
            game -= 1
            print(f"Sorry, {game} lives left") 
            if game == 0: 
              print(randomWord)
              youLost = input("Sorry, You lost")
              if youLost == "The bunnies command me.": 
                print("The voice says, 'You can go on, because the bunnies command you'")
              else:
                exit("You are destroyed.")
          
          
          if choice == A: 
              print(A + "___")  
          if choice == B: 
              print("_" + B +"__")
          if choice == C: 
              print("__" + C + "_") 
          if choice == D:
              print("___" + D)
          
          if choice == A + D: 
              print(A + "__" + D) 
          if choice == A + B: 
              print(A + B + "__") 
          if choice == A + C: 
              print(A + "_" + C +"_")
          if choice == B + C: 
              print("_" + B + C + "_")
          if choice == B + D: 
              print("_" + B + "_" + D)
          if choice == C + D: 
              print("__" + C + D)
      
          if choice == A + B + C: 
              print(A + B + C + "_") 
          if choice == A + C + D: 
              print(A + "_" + C + D)
          if choice == A + C + D: 
              print(A + "_" + C + D)
          if choice == B + C + D: 
              print("_" + B + C + D)
          
      
             
      startGame()
        
        # random_word = random.choice(DictionaryOfWords)
        # print(random_word)

    print("You continue through the path until you get to a large cave. You slowly venture inside. You hear a booming voice say, 'I challenge you to hangman'")
    hangmanDecision = input("Do you want to play hangman with the voice? y/n: ")
    if hangmanDecision == "n": 
      exit("You say no and you are destroyed by a lightning bolt.")
    elif hangmanDecision == "y":
      Hangman()

    print("Having successfully completed the challenge, you continue your quest.")

    def superTrail(): 
      # code
      stuffHave = ["Wagon", "Ox", 10, "<-- Lb of Food", "Map"] 
      
      def noFood(): 
        if stuffHave[2] == 0: 
          exit("You have no more food, sorry")
      
      def know():
        Have = "Do you want to know what you have Y/N: "
        stuff = input(Have).upper()
      
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
            noFood()
            know()
      
      # game start 4
        print("You have now eaten 9Lb of food. After 50 miles of walking, you see a huge tree. Do you want to pick the fruit or keep moving? Input pick to pick the fruit or input move if you want to keep moving and ignore the fruit.") 
        fruit = input("Pick fruit or keep moving?: ") 
      
        if fruit == "pick": 
          print("You pick the fruit and move on, you now have 5Lb of food.")  
          stuffHave[2] = 5 
          know()
          noFood()
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
          noFood() 
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
          print("YOu have", stuffHave[2], "Lbs of food")
          food = int(input())
      
          if food < 40: 
              print("You succeed in getting " + str(food) + "Lbs of food.") 
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
          noFood()
        elif camp == "stay": 
          forestFire() 
          noFood()
          know()
      
        # game start 8 
        print("You have", stuffHave[2], "of food.")
        print("You finally arive at your destination. You  get an infinite amount of gold and land, you have surived, good for you.")
        exit("Game has ended, YOU WIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    print("You continue walking until you reach a tomb. As soon as you touch it, you are transported into another world. You hear a booming voice. 'You must traverse this realm and get the treasure. Good bye.'")

    superTrail()

    print("You exit the realm. Two large stone doors appear in front of you and grind open. You look into the dark hall they lead into.")

    def terrifyingGame():
      board = [" " for i in range(9)]
      
      print("|1| |2| |3|")
      print("|4| |5| |6|")
      print("|7| |8| |9|")
      
      def printBoard(): 
            row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
            row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
            row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
            
            print()
            print(row1)
            print(row2)
            print(row3)
            print()
            
      def playerMove(icon):
      
            if icon == "X": 
                    number = 1
            elif icon == "O":
                    number = 2
            
            print("Your turn player {}".format(number))
            
            choice = int(input("Enter your move (1-9): ").strip())
            if board[choice-1] ==" ": 
                    board[choice-1] = icon
            else: 
                    print()
                    print("That space is taken!")
                    
      def isVictory(icon): 
            if(board[0] == icon and board[1] == icon and board[2] == icon) or\
              (board[3] == icon and board[4] == icon and board[5] == icon) or\
              (board[6] == icon and board[7] == icon and board[8] == icon) or\
              (board[0] == icon and board[3] == icon and board[6] == icon) or\
              (board[1] == icon and board[4] == icon and board[7] == icon) or\
              (board[2] == icon and board[5] == icon and board[8] == icon) or\
              (board[0] == icon and board[4] == icon and board[8] == icon) or\
              (board[2] == icon and board[4] == icon and board[6] == icon): 
                    return True
            else: 
                    return False
                    
      def isDraw(): 
            if" " not in board: 
                    return True
            else: 
                    return False
      
      while True: 
            printBoard()
            playerMove("X")
            printBoard()
            if isVictory("X"): 
                    exit("X wins! The snake eats you")
            elif isDraw(): 
                    print("It's a draw!")
                    break
            playerMove("O")
            if isVictory("O"):
                    printBoard
                    exit("O wins! The snake eats you")




    print("You slowly walk through the doorway. You look down and see a huge chasm. Infront of you a large space and then a floor, but you can't see what's infront of it.")
    creepyChoice = input("Do you choose chasm, or floor?: ").lower()
    if creepyChoice == "floor":
      print("You take a running leap and land onto the floor. You look forward. You see a huge monster with swivelling teeth, green eyes, and a glowing tongue.")
      exit("The monster eats you")
    elif creepyChoice == "chasm": 
      print("You jump into the chasm an land on you feet a few seconds later. Apparantly, someone painted the floor black. You walk forward. You are met with a huge snake. It says, 'Find another player and play tic-tac-toe. And tie, or I will eat you!")
      terrifyingGame()

    print("After you tie the game, the snake says, 'I said I wouldn't eat you, not that I would let you pass. Translate this into pig latin, and I will let you pass: 'I need to eat food, or I will go hungry, and I do not want to be hungry.'")
    def platinHelper(): 
      # get sentence from user

      original = input("Please enter a sentence(whithout punctuation): ").strip().lower() 
      
      # split sentence into words
      
      words = original.split()
      print(words)
      
      # loop through words and convert into pig latin
      
      newWords = [] 
            
      for word in words: 
            if word[0] in "aeiou":
                    newWord= word+"yay"
                    newWords.append(newWord)  
            else: 
                    vowelPos = 0 
                    for letter in word: 
                            if letter not in "aeiou": 
                                    vowelPos = vowelPos + 1
                            else: 
                                    break
                    cons = word[:vowelPos]
                    theRest = word[vowelPos:]
                    newWord = theRest+cons+"ay"
                    newWords.append(newWord)
                            
      
      # stick words back together
      output = " ".join(newWords) 
      
      # output final string
      print(output)

    help = input("You think about it:")
    if help == "The bunnies are my lords": 
      print("Use the translator to help you. Fix the translation up and tell it to the snake.")
      platinHelper()

    snakeAnswer = input("What is your answer?: ")
    if snakeAnswer == "iyay eednay otay eatyay ood fay, oryay iyay illway ogay ungryhay, andyay iyay oday otnay antway otay ogay ungryhay":
      print("The snake says, 'You have said the right answer, so I will let you pass.'")
      print("You go past the snake. You walk through a hall and reach a pedastal with a large gem.")
      exit("YOU HAVE COMPLETED PT.1 OF YOUR QUEST!!!!!!!!!")
    else: 
      print("The snake says, 'You have said the wrong answer, and I must eat you.'")
      exit("The snake eats you.")

################################################### WARNING: GAME START Begins HERE!!!!!!! #############################################################

toStart = input("Will you come on an adventure? [y/n]: ").lower()
if toStart == "y":
    print("Welcome to the wonderful world of Ruune")
    scaryAdventure = input("Which adventure would you like to begin? The desert, the ancient wizard lair, or the dinosaur park? [wizard or desert or dinosaur]: ").lower()
    if scaryAdventure == "desert":
        desertAdventure()
        # finish desertAdventure
    elif scaryAdventure == "wizard":
        wizardAdventure()
    elif scaryAdventure == "dinosaur":
        dinoAdventure()
        # finish dinoAdventure
        
else toStart == "n":
    exit("YOU ARE NOT WORTHY!!!!!!!!!!!!!")




