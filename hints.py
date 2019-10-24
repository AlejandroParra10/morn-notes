# how to turn a string into a list 
myString = "arizona"
myList = list(myString)
print(myList)
secret =[]

# how to create a list with _ in place of letters
for a in myList: 
	secret.append("_")
print(secret)

# how to replace an _ with a letter
secret[2] = "i"
print(secret)

# how to keep track of misses
secret = "christmas"
misses = 0 
secret = list(secret)

hangList = ['''pic 1''', 
'''pic 2''',]

while misses < 7:
	print(hangList[misses])
	guess = input("Guess a letter: ")
	if guess in secret:
		#loop through secret and find all the matching letters
		print("The letter is in the secret word")
	else:
		misses = misses + 1

# How to replace an item in a list 

mystery = list("Halloween")
guessList = list("_________")

guess = input("Guess a letter")

index = 0
for letter in mystery: 
	if letter == guess:
		guessList[index] = letter 
		index += 1

print(guessList)