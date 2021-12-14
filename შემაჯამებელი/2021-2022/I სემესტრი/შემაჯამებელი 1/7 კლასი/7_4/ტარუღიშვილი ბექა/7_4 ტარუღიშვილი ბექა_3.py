import random as r

rn = r.randint(100, 999)
print(rn)

minutes = rn//60
seconds = rn - minutes*60
print("Minutes: ",minutes, "Seconds: ",seconds)


