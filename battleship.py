import random

difficulty = raw_input("Easy, Medium, Hard, or Impossible? ").lower()

if difficulty == "easy":
	sizeOfOcean = 10
	missiles = 7
elif difficulty == "medium":
	sizeOfOcean = 20
	missiles = 10
elif difficulty == "hard":
	sizeOfOcean = 30
	missiles = 15
else:
	sizeOfOcean = 30
	missiles = 5



ocean = [0 for _ in range(sizeOfOcean)]

for _ in range(5):
	position = random.randint(0, sizeOfOcean-1)
	ocean[position] = 1


ships = 0
for square in ocean:
	if square == 1:
		ships = ships + 1

found = 0

while found < ships and missiles > 0:
	for number in range(sizeOfOcean):
		print(number % 10),
	print(" ")
	for square in ocean: 
		if square == 1 or square == 0:
			print("#"),
		elif square == -1:
			print("X"),
		else:
			print("@"),
	print(" ")
	print("Where to aim?")

	guess = raw_input()
	if guess == "q":
		break

	guess = int(guess)
	missiles = missiles - 1

	if ocean[guess] == 1:
		ocean[guess] = 2
		print("Bullseye!")
		found = found + 1
	else:
		print("Miss")
		ocean[guess] = -1

	print(str(missiles) + " missiles left")

if found == ships:
	print("You win!!!")
else:
	print("You loser :(")