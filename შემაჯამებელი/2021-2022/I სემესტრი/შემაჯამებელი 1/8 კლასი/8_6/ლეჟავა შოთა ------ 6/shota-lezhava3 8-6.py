import random
r = random.randint(100, 1000)
min = r//60
sec = r%60
print(str(min) + " min  and " + str(sec) + "  sec")
