import random
a = random.randint(100, 1000)
b = a//60
c = a%60
print(b)
print(str(b) + " minutes and " + str(c) + " seconds")
