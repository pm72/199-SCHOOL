import random
x=random.randint(100,999)
s=x%60
m=(x-s)/60       # ??????  m = int((x - s) / 60)  an  (x - s) // 60   an   m = x % 60
print(x,m,s)


input()