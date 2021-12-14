import random
number = random.randint(10**11, 10**12)
maximum = 0
minimum = 10
while(number>0):
    num = number%10
    maximum = max(num, maximum)
    minimum = min(num, maximum)
    number = number//10
print((maximum+minimum)**2)
