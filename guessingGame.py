print("guess a number between 1 and 20")
import random

number = random.randint(1,22)


guess = 0

while guess != number:
	guess = raw_input()
	if guess == "q":
		break
	else:
		guess = int(guess)
	if number == 21:
		print("NO")
	elif guess > 20:
		print("Idiot")
	elif guess == number:
		print("You win!!")
	elif guess > number:
		print("Too high")
	else:
		print("too low")
