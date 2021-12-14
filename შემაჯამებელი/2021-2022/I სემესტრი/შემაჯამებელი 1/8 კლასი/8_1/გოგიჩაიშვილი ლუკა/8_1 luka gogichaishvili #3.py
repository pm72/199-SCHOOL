import random
x = random.randint(100,1000)
minute = x//60
second = x%60
print(str(minute) + "minutes and " + str(second) + "seconds")
