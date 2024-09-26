# Check if a book is existing in your collection
collectionOfBooks = ["The King", "7 habits to have", "How to Influence People"]
print("Enter the name of the book:")
bookToBeChecked = input()
for book in collectionOfBooks:
	if book == bookToBeChecked: 
		print("Yes, I do have that book!")
		break
else: 
	print("No, I do not have that book!")