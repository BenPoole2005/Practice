import random


def startGame():

	difficulty = raw_input("Easy, Medium, Hard, or Impossible? ").lower()
	sizeOfOcean = 0
	missiles = 0

	if difficulty == "easy":
		sizeOfOcean = 6
		missiles = 20
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
	
	ocean = placeShip(5, ocean)
	for _ in range(2):
		ocean = placeShip(4, ocean)
	for _ in range(3):
		ocean = placeShip(3, ocean)
	for _ in range(4):
		ocean = placeShip(2, ocean)
	return ocean

	
def placeShip(length, ocean):
	orientation = random.randint(0, 1)
	sizeOfOcean = len(ocean)

	if orientation == 0:
		startX = random.randint(0, sizeOfOcean - length - 1)
		startY = random.randint(0, sizeOfOcean - 1)
		for i in range(length):
			ocean[startY][startX + i] = 1
	else:
		startX = random.randint(0, sizeOfOcean - 1)
		startY = random.randint(0, sizeOfOcean - length - 1)
		for i in range(length):
			ocean[startY + i][startX] = 1

	return ocean

def printMap(ocean):
	for line in ocean:
		for square in line:
			if square <=1:
				print("#"),
			elif square == 2:
				print("X"),
			else:
				print("@"),
		print("")

def playGame(ocean, missiles):
	while True:
		if missiles == 0:
			print("Game Over")
			break 
			
		printMap(ocean)
		guess = raw_input("Where to aim? ").replace(" ", "")
		
		try:
			x, y = guess.split(",")
			print("X coordinate is: " + x)
			print("Y coordinate is: " + y)
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
		else:
			print("Miss")
			ocean[x][y] = 3
			missiles = missiles - 1
			print(str(missiles) + " missiles left")

		


sizeOfOcean, missiles = startGame()
oceanMap = buildMap(sizeOfOcean)
playGame(oceanMap, missiles)



