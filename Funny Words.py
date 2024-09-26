findLib = int(input("which number 1 - 4: ").strip())

# small sentances
def Lib1():
  s1l1 = "I need to find a/an" 
  s2l1 = "so I can"
  s3l1 = "and ride a"  
  print(s1l1 + " " + need1 + " " + s2l1 +" " + need2 + " " + s3l1 + " " +need3+".")

def Lib2():
  s1l2 = "I need a/an"
  s2l2 = ", and I must"
  s3l2 = "so I can own a/an" 
  print(s1l2 + " " + need1 + " " + s2l2 +" " + need2 + " " + s3l2 + " " +need3+".")

def Lib3():
  s1l3 = "I want to keep your"
  s2l3 = "so I can"
  s3l3 = "and keep a/an"
  print(s1l3 + " " + need1 + " " + s2l3 +" " + need2 + " " + s3l3 + " " +need3+".") 

# bigger sentances 
def Lib4(): 
  s1l4 = "I need a/an"
  s2l4 = "so I can"
  s3l4 = "on a/an"  
  print(s1l4 + " " + need4 + " " + s2l4 + " " + need5 + " " + need6 + " " + s3l4 + " "+ need7 + " " + need8 + ".")
  

# small sentances variables
need1 = input("give me a noun: ")
need2 = input("give me a verb: ")
need3 = input("give me another noun: ")

# bigger sentances variables
need4 = input("Give me a noun: ")
need5 = input("Give me an adverb: ")
need6 = input("Give me a verb: ")
need7 = input("Give me an adjective: ")
need8 = input("Give me another noun: ") 



# print(s1 + " " + need1 + " " + s2 +" " + need2 + " " + s3 + " " +need3)  
if findLib == 1: 
  Lib1()
elif findLib == 2: 
  Lib2()
elif findLib == 3:
  Lib3()
elif findLib > 4: 
  while True: 
    print("You are bad!!!!!!!!!!!")

elif findLib == 4: 
  Lib4()