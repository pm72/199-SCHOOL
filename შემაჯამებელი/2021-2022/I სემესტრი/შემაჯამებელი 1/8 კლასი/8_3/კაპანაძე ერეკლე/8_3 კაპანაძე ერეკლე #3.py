import random
n = random.randint(100,1000)
mins = n//60
secs = n%60
print(str(mins) + "mins and" + str(secs) + "secs")
