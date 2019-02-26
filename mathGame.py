import random

print("Welcome to Ben's forced math game")

difficulty = raw_input("Easy, Medium, or Hard? ").lower()

def get_operation():
	if difficulty == "easy":
		number1 = random.randint(0, 40)
		number2 = random.randint(0, 40)

		number3 = random.randint(0, 12)
		number4 = random.randint(0, 12)

		op = random.randint(0, 3)
	elif difficulty == "medium":
		number1 = random.randint(-40, 40)
		number2 = random.randint(-40, 40)

		number3 = random.randint(0, 20)
		number4 = random.randint(0, 20)

		op = random.randint(0, 3)
	else:
		number1 = random.randint(-100, 10000)
		number2 = random.randint(-100, 10000)

		number3 = random.randint(-40, 40)
		number4 = random.randint(-40, 40)

		op = random.randint(0, 4)


	if op == 0:
		print(str(counter) + ". " + str(number3) + "/" +  str(number4))
		an = number3 / number4
	elif op == 1: 
		print(str(counter) + ". " + str(number3) + "*" + str(number4))
		an = number3 * number4
	elif op == 2: 
		print(str(counter) + ". " + str(number1) +  "+" + str(number2))
		an = number1 + number2
	elif op == 3: 
		print(str(counter) + ". " + str(number1) + "-" + str(number2))
		an = number1 - number2
	else:
		print(str(counter) + ". " + str(number1) + "%" + str(number2))
		an = number1 % number2
	return str(an)

lives = 3
counter = 1

while True:	
	an = get_operation()

	guess = raw_input()
	if guess == "q":
		break


	if guess == an or guess == "w":
		print("Correct")
		counter = counter + 1
	else:
		print("Wrong")
		lives = lives - 1
		print(str(lives) +  " lives left")

	if lives == 0:
		print("You SUCK")
		break
