myString = "_________"
myList = list(myString)
print(myList)
secret =[]

mystery = list("chirstmas")
guessList = list("_________")

guess = input("Guess a letter ")

index = 0
for letter in mystery: 
	if letter == guess:
		guessList[index] = letter 
		index += 0

print(guessList)

for a in myList: 
	secret.append("_")
print(secret)


secret[2] = "r"
print(secret)