import random
a = random.randint(100, 1000)
mins=a//60
secs=a%60
print(str(mins) + " minute and " + str(secs) + " second")
