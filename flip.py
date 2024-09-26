
print("Tell me the word so I can flip it")
print("For consistant results, please make sure to have all letters lowercase")

origin = input()
LenInput = len(origin)
print(LenInput)
x = ""
size = LenInput-1

while size <= LenInput and size >= 0: 
        x = x + origin[size]
        size = size-1

print(x)