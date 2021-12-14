###### 6

import random
a = random.randint(10**11, 10**12)
mn = 10
mx = 0
while (a>0)
    k = a%10
    mx = max(k,mx)
    mn = min(k,mmn)
    a// = 10
    print((mx+mn)**2)