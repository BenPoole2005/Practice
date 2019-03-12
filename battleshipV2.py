import random


def startGame():

	difficulty = raw_input("Easy, Medium, Hard, or Impossible? ").lower()
	sizeOfOcean = 0
	missiles = 0

	if difficulty == "easy":
		sizeOfOcean = 6
		missiles = 15
	elif difficulty == "medium":
		sizeOfOcean = 10
		missiles = 50
	elif difficulty == "hard":
		sizeOfOcean = 20
		missiles = 75
	else:
		sizeOfOcean = 30
		missiles = 30

	return sizeOfOcean, missiles

def buildMap(sizeofOcean):
	ocean = [
			 [0 for _ in range(sizeOfOcean)]
			 for _ in range(sizeOfOcean)
			]
	
	ocean = placeShip(5, ocean, -1, -1, -1)
	for _ in range(2):
		ocean = placeShip(4, ocean, -1, -1, -1)
	for _ in range(3):
		ocean = placeShip(3, ocean, -1, -1, -1)
	for _ in range(4):
		ocean = placeShip(2, ocean, -1, -1, -1)
	return ocean
	
def buildUserMap(sizeofOcean):
	ocean = [
			 [0 for _ in range(sizeOfOcean)]
			 for _ in range(sizeOfOcean)
			]

	position = raw_input("Location of length 5 ship? (x, y, o)\n").replace(" ", "")
	
	try:
		x, y, o = position.split(",")
		x, y, o = int(x), int(y), int(o)
		placeShip(5, ocean, y, x, o)
	except:
		print("You're so stupid, you did it wrong!")
	printMap(ocean, True)

	for _ in range(2):
		position = raw_input("Location of length 4 ship? (x, y, o)\n").replace(" ", "")
		try:
			x, y, o = position.split(",")
			x, y, o = int(x), int(y), int(o)
			placeShip(4, ocean, y, x, o)
		except:
			print("You're so stupid, you did it wrong!")
		printMap(ocean, True)

	for _ in range(3):
		position = raw_input("Location of length 3 ship? (x, y, o)\n").replace(" ", "")
		try:
			x, y, o = position.split(",")
			x, y, o = int(x), int(y), int(o)
			placeShip(3, ocean, y, x, o)
		except:
			print("You're so stupid, you did it wrong!")
		printMap(ocean, True)

	for _ in range(4):
		position = raw_input("Location of length 2 ship? (x, y, o)\n").replace(" ", "")
		try:
			x, y, o = position.split(",")
			x, y, o = int(x), int(y), int(o)
			placeShip(2, ocean, y, x, o)
		except:
			print("You're so stupid, you did it wrong!")
		printMap(ocean, True)

	return ocean

def placeShip(length, ocean, xCoord, yCoord, orient):
	orientation = random.randint(0, 1) if orient == -1 else orient
	sizeOfOcean = len(ocean)

	if orientation == 0:
		startX = random.randint(0, sizeOfOcean - length - 1) if xCoord == -1 else xCoord
		startY = random.randint(0, sizeOfOcean - 1) if yCoord == -1 else yCoord
		for i in range(length):
			ocean[startY][startX + i] = 1
	else:
		startX = random.randint(0, sizeOfOcean - 1) if xCoord == -1 else xCoord
		startY = random.randint(0, sizeOfOcean - length - 1) if yCoord == -1 else yCoord
		for i in range(length):
			ocean[startY + i][startX] = 1

	return ocean

def printMap(ocean, userMap):
	print(" "),
	for n in range(len(ocean)):
		print(n%10),
	print("")
	for n, line in enumerate(ocean):
		print(n%10),
		for square in line:
			if userMap:
				if square == 0:
					print("_"),
				elif square == 1:
					print("X"),
				else:
					print("@"),
			else:
				if square <=1:
					print("#"),
				elif square == 2:
					print("X"),
				else:
					print("@"),
		print("")

def playGame(ocean, userOcean, missiles):
	nShips = 0
	for line in ocean:
		for square in line:
			if square == 1:
				nShips = nShips + 1

	nUserShips = 0
	for line in userOcean:
		for square in line:
			if square == 1:
				nUserShips = nUserShips + 1
	while True:
		if nShips == 0:
			print("You Win!!")
			break
		elif nUserShips == 0:
			print("Computer Wins!")
			break
			
		printMap(ocean, False)
		guess = raw_input("Where to aim? ").replace(" ", "")
		
		try:
			x, y = guess.split(",")
			#print("X coordinate is: " + x)
			#print("Y coordinate is: " + y)
			x = int(x)
			y = int(y)
		except:
			missiles = missiles - 1
			print(str(missiles) + " missiles left")
			continue

		if x >= len(ocean) or y >= len(ocean):
			print("F@#$")
			continue

		if ocean[x][y] == 1:
			print("Hit!")
			ocean[x][y] = 2
			nShips = nShips - 1
		elif ocean[x][y] == 2:
			print("Already Guessed")
		else:
			print("Miss")
			ocean[x][y] = 3
			missiles = missiles - 1
			print(str(missiles) + " missiles left")

		computerX = random.randint(0, len(ocean) - 1)
		computerY = random.randint(0, len(ocean) - 1)
		if userOcean[computerX][computerY] == 1:
			userOcean[computerX][computerY] = 2
			nUserShips = nUserShips - 1
			print(str(nUserShips) + " of your ships left")
		





sizeOfOcean, missiles = startGame()
oceanMap = buildMap(sizeOfOcean)
userMap = buildUserMap(sizeOfOcean)
playGame(oceanMap, userMap, missiles)



