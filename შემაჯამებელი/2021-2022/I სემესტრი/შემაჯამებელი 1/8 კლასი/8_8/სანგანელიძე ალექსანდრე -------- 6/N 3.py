import random
randomNumber = random.randint(100, 999)
minutes = int(randomNumber / 60)
seconds = int(randomNumber % 60)
print( randomNumber, minutes, seconds)
