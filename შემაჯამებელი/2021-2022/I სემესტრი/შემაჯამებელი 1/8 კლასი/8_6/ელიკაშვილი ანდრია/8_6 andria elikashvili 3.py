import random
r = random.randint(100, 1000)
mins=r//60
secs=r%60
print(str(mins) + " minutes and " + str(secs) + " seconds")
