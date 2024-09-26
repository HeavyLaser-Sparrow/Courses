# x = 0

# lock = input("What is the password?: ").strip().capitalize()
# password = "Trees"

# if lock == password: 
#	print("Hello")  
# else: 
# 	x = x + 1 
	
# while x > 0: 
# 	print("Intruder!")


# variables
y = 0

username1 = "Waterbottle"
username2 = "Apples" 

password1 = "Water"
password2 = "Seeds" 

# inputs
usernameinput = input("What is the username?: ").strip().capitalize()

# ifs
if usernameinput == username1: 
	passwordinput = input("What is the password?: ").strip().capitalize()
	if passwordinput == password1: 
		print("hello")
	else: 
		y > 0
elif usernameinput == username2: 
	passwordinput = input("What is the password?: ").strip().capitalize
	if passwordinput == password2: 
		print("hello")
	else: 
		y > 0
else: 
	print("Sorry, there is no username for that") 
	

# saftey mechanism
while y > 0: 
	print("Incorrect, You are an intruder")