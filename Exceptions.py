>>> 10 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
try: 
     length = 10
     width = 0
     length / width
except Exception: 
    print("Division by 0 is invalid! Please change your input")

Division by 0 is invalid! Please change your input
 
del(width)

width
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'width' is not defined
try: 
    length / width
except Exception: 
            print("Division by 0 is invalid! change your input")

Division by 0 is invalid! change your input

try: 
    length / width
except NameError:
            print("variable has been used before defining it")

variable has been used before defining it
