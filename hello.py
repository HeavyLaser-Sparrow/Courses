# ask for your name

name = input("What is your name?:")

# ask user for age

age = input("How old are you?:")

# ask user for city

city = input("Where do you live in?:")

# ask user what they enjoy

enjoy = input("What do you enjoy doing?:")

# print(name)
# print(age)
# print(city)
# print(enjoy)

# Creat output text

string = "Your name is {} and you are {} years old. You live in {} and enjoy {}"
output = string.format(name, age, city, enjoy)

# print output to screen
print(output)