import random as r
n = r.randint(100, 1000)
m = n//60
s = n%60
print(str(m) + " minutes and " + str(s) + " seconds")
