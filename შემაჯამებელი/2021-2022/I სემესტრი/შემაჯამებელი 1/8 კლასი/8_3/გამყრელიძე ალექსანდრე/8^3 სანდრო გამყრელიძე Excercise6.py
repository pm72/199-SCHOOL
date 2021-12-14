##Excercise 6
import random
x=random.randint(1, 10**12-1)
y1=0
x1=10
while (x>0):
    y2 = x%10
    y1 = max(y2, y1)
    x1= min(y2, x1)
    x//=10
print((y1+x1)**2)
