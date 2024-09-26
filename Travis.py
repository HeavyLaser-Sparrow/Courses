knownUsers = ["Tom", "Bob", "Dan", "Tree", "Port", "Fred", "Harry", "Carrot"]

# print(len(knownUsers))

while True: 
	print("Hello, My name is Travis")
	name = input("What is your name?:").strip().capitalize()
	
	if name in knownUsers: 
		print("Hello {}".format(name)) 
		remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()
		if remove == "y": 
			knownUsers.remove(name)
		elif remove == "n":
			print("No problem, I didn't want you to leave anyway!")
		
	else: 
		print("Hmmm I don't think I have met you yet {}".format(name))
		addMe = input("Would you like to be added to the system(y/n)?:").strip().lower()
		if addMe == "y": 
			knownUsers.append(name) 
		elif addMe == "n":
			print("Ok, come back next time")
		
		
		