import random
x = random.randint(100, 1000)
mins = x // 60
secs = x % 60
print(str(mins) + " minutes and " + str(secs) + " seconds")
