import random
x = random.randint(100,1000)
minutes = x//60
seconds = x%60
print(str(minutes) + "minutes and" + str(seconds) + "seconds")
