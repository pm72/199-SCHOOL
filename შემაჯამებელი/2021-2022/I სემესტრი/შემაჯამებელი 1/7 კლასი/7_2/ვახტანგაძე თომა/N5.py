import random
import math as m
x1=random.randint(1, 999);
x2=random.randint(1, 999);
y1=random.randint(1, 999);
y2=random.randint(1, 999);
x3=(x2-x1)**2;
y3=(y2-y1)**2;
z=x3+y3;
b=m.sqrt(z);
print(x1, x2, x3, y1,y2,y3,z,b);
