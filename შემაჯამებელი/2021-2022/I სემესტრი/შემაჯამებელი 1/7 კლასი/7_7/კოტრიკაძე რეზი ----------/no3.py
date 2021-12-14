import math
import random
n = random. randint(100,999);
seconds = n % 60;
n2 = n - seconds;
minutes = n2 / 60;
print(n,"  ", minutes, "  ", seconds);


input()