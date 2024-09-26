#check which among the two numbers is bigger.

def findMaximum(firstNumber, secondNumber): 
	if firstNumber > secondNumber: 
		print("The first number is greater than the second number")
		return firstNumber
	elif secondNumber > firstNumber: 
		print("The second number is greater than the first number")
		return secondNumber
	else: 
		print("Both of your numbers are equal, neither is greater than the other")
		return firstNumber

print("Enter the first number: ")
firstNumber = float(input()) 
print("Enter the second number: ")
secondNumber = float(input())




maximumNumber = findMaximum(firstNumber, secondNumber)

print("Maximum number = {}".format(maximumNumber))

