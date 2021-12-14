from random import randint
x = randint(100,999)
mins = x//60
secs = x - mins*60
print(str(mins),'mins and', str(secs), 'secs')
print(x)
