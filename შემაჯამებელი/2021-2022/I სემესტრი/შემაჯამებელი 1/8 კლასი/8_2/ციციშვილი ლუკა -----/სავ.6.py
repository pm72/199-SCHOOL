#6
a = random.randint(100000000000,999999999999)
b = a
lowestnum = 0
biggestnum = 0
amountoftries = 0
amountoftries2 = 0
print(b)
while (amountoftries < 12):
    amountoftries = amountoftries + 1

    b = b//10
    if biggestnum < b%10:
        biggestnum = b%10

c = a
while (amountoftries2 < 12):
    amountoftries2 = amountoftries2 + 1
    print(c)
    c = c//10
    if lowestnum > b%10:
        lowestnum = b%10
print(biggestnum)
print(lowestnum)
print((biggestnum + lowestnum)**2)

