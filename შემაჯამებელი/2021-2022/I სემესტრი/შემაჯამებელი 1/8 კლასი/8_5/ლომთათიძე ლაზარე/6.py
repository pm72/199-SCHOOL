##6
a = random.randint(100000000000,999999999999)
b = a
lowestnumber2 = 0
highestnumber = 0
amountoftries = 0
amountoftries2 = 0
print(b)
while (amountoftries < 12):
    amountoftries = amountoftries + 1

    b = b//10
    if highestnumber < b%10:
        highestnumber = b%10

c = a
while (amountoftries2 < 12):
    amountoftries2 = amountoftries2 + 1
    print(c)
    c = c//10
    if lowestnumber22 > b%10:
        lowestnumber2 = b%10
print(highestnumber)
print(lowestnumber2)
print((highestnumber + lowestnumber2)**2)

