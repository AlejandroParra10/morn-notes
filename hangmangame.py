# Hangman Game
# Alejandro Parra P6
print("Welcome to Hangman")

mystery = list("christmas")
guessList = list("_________")

guess = input("Guess a letter")

index = 0
for letter in mystery: 
	if letter == guess:
		guessList[index] = letter 
		index += 1

print(guessList)
