import random
a = random.randint(100, 1000)
minutes = a//60
seconds = a%60
print(str(minutes) + " minutes and " + str(seconds) + " seconds")
