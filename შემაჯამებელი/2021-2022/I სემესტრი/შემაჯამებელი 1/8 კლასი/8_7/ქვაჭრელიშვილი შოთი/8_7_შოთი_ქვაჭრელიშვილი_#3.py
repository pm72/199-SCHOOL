import random
a = random.randint(100, 1000)

m= a//60

s = a%60

print(str(m) + " minutes and " + str(s) + " seconds")