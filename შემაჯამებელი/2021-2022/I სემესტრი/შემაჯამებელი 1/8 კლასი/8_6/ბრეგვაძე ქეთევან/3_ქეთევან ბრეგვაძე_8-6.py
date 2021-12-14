import random
r = random.randint(100, 1000)
l = r//60
l1 = r%60
print(str(l) + " minutes and " + str(l1) + " seconds")