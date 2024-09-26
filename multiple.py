print ("Enter a number: ")
number = int (input())
if number % 3 is 0: 
    print("Number is a multiple of 3") 
    if number % 7 is 0:  
        print("Number is also a multiple of 7")
    else:
        print("Number is a multiple of 3, but not a multiple of 7")
