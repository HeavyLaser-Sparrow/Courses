# films dictionary [age, tickets left]

films = { 
	"Finding Nemo": [3,5], 
	"Trees": [2,10],
	"Fish": [10,20],
	"Water": [3,12],
	}
	
print(films)

while True: 
	
	choice = input("What film would you like to watch?:").strip().title
	
	if choice in films:
		age = int(input("How old are you?:").strip())
		
		# check user age
		
		if age >= films[choice][0]: 
			# check enough seats
			numSeats = films[choice][1]
			if  numSeats > 0:
				print("Enjoy the film") 
				films[choice][1] = films[choice][1]-1
			else: 
				print("Sorry, there are no more tickets for this movie")
				
		else: 
			print("You are too young to watch that film")
			
	else: 
		print("Sorry, we don't have that film")
		
		
		