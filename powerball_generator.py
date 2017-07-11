import random 


def lottery(n):
	for i in range(n):
		for numbers in range(6):
			numbers = random.randint(0, 53)
			print("numbers:  " + str(numbers))

		powerball = random.randint(0, 42)
		print("Powerball: " + str(powerball))


print(lottery(12))







