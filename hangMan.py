import random
print("Welcome to Hang man")
print("for hint type hint")
print("Good Luck!!!")
f = open("words.txt", "r")

l = []
for word in f.readlines():
	l.append(word)
chosenWord = l[random.randint(0, len(l))].lower()[:-1]
discovered = [0 for _ in range(len(chosenWord))]

lives = len(chosenWord)
unfound = len(chosenWord)

while lives > 0 and unfound > 0:
	for n in range(len(chosenWord)):
		if discovered[n] == 0:
			print("_"),
		else:
			print(chosenWord[n]),
	print("")
	guess = raw_input("Guess a letter\n").lower()
	if guess == 'quit':
		break
	elif guess == "hint":
		discovered[random.randint(0, len(discovered)-1)] = 1
		continue

	found = False
	for n in range(len(chosenWord)):
		if chosenWord[n] == guess:
			discovered[n] = 1
			unfound = unfound - 1
			found = True
	if not found:
		lives = lives - 1
		print("Wrong, " + str(lives) + " left")
print(chosenWord)
if unfound == 0:
	print("You win")

