import random
num = random.randint(1, 100)
guess = 0
attempt = 0
while (guess != num):
	guess = int(input("Guess the number: "))
	attempt += 1
	print("attempt: ", attempt)
	if guess > num:
		print("Go Lower", guess)
	elif guess < num:
		print("Go Higher", guess)
	else:
		print("Correct Answer!")
		print("You won in", attempt, "attempts")

