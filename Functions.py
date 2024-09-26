# defining functions 

def helloWorld(): 
	print("Hello World!")

helloWorld()

# def functionName(): 
#	block of code (can be anything[if, when, for]) 


# functions with parameters and return values
# area
length1 = 8 
width1 = 3 
areaOne = length1 * width1
 
areaOne

length2 = 10
width2 = 4
area2 = length2 * width2
area2

def computeArea(length, width): 
     area = length * width
     print(area)
 
computeArea(length1, width1)

 
def computeArea(length, width): 
     area = length * width
     return area
 
area1 = computeArea(length1, width1)
 
area1

area2 = computeArea(length2, width2)
 
area2
