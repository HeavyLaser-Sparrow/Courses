import random
# begin
print("Let us play the brain/monster version of Hangman!")
print("In here, guess random letters, and put all of your answers together to  make a final answer")
print("You have 10 lives") 

DictionaryOfWords = ["wait", "fire", "wood","wire", "what", "case", "tore", "bait", "acid", "area", "away", "that", "this", "tote", "hole", "worm", "lamb", "mane", "main", "lion", "mule", "akin", "bear", "need", "bind", "thou", "aged", "awry", "also", "ball", "base", "bird", "boat", "belt", "bond", "stat", "burn", "call", "city", "coat", "come", "cope", "cash", "club", "dawn", "diet", "coke", "days", "data", "debt", "desk", "does", "dose", "crew", "does", "done", "fast", "feed", "fine", "fish", "five", "fort", "gold", "glad", "golf", "gift", "gave", "half", "hair", "hare", "head", "held", "hear", "hold", "hope", "kick", "home", "host", "jack", "item", "king", "know", "knee", "lake", "laid", "logo", "lord", "lost", "feif", "list", "loss", "lost", "luck", "mood", "moon", "must", "near", "navy", "need", "mode", "more", "milk", "mine", "move", "poll", "plot", "rail", "race", "rose", "root", "roof", "sake", "said", "seen", "seed", "sent", "tank", "task", "sole", "team", "tend", "suit", "surf", "tech", "tape", "text", "tree", "tone", "tool"]

# word
randomWord = random.choice(DictionaryOfWords)
# print(randomWord) 

# word's lines
wordCount = len(randomWord)


underscores = "_" * wordCount   
print(underscores)

# game start
def startGame(): 
  
  game = 10 
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
        restart = input("Sorry, you lost. If you want to try again,restart the program, or put 'Y': ").strip() 
        print("Sorry, You lost")
        if restart == "Y": 
          startGame()
    
    
    
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
    

while True:         
  startGame()
  
  # random_word = random.choice(DictionaryOfWords)
  # print(random_word)