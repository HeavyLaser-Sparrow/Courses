# get sentence from user

original = input("Please enter a sentence: ").strip().lower() 

# split sentence into words

words = original.split()
print(words)

# loop through words and convert into pig latin

newWords = [] 
	
for word in words: 
	if word[0] in "aeiou":
		newWord= word+"yay"
		newWords.append(newWord)  
	else: 
		vowelPos = 0 
		for letter in word: 
			if letter not in "aeiou": 
				vowelPos = vowelPos + 1
			else: 
				break
		cons = word[:vowelPos]
		theRest = word[vowelPos:]
		newWord = theRest+cons+"ay"
		newWords.append(newWord)
			

# stick words back together

output = " ".join(newWords) 

# output final string

print(output)








