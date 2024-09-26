print("Tell me your name")
name = input() 

while len(name) >= 8: 
	print("Your name is too long. Let's change your name to dragon")
	
while len(name) < 7: 
	print("Your name is short. Let's change your name to television ")
	
while len(name) == 8: 
	print("You are smart") 