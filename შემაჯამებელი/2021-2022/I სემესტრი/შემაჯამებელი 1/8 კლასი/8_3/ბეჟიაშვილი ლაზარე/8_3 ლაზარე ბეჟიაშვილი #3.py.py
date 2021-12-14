import random
b = random.randint(100, 1000)
s = b//60
m = b%60
print(b)
print(str(s) + " minutes and " + str(m) + " seconds")
