import random
b = random.randint(100, 1000)

minutes = b//60

seconds = b%60

print(str(minutes) + " minutes and " + str(seconds) + " seconds")
