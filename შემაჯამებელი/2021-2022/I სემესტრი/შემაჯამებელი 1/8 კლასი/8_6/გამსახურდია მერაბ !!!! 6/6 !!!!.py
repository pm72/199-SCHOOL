from random import randint
#q = randint(100000000000, 999999999999 + 1)
q = randint(1, 10**12 - 1)
minimumi = min(str(q))
maximumi = max(str(q))
minimumi = int(minimumi)
maximumi = int(maximumi)

print(q)
print((minimumi + maximumi)**2)


input()