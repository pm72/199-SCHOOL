##3
a = random.randint(100,999)

aseconds = a%60
aminutes = int((a - a%60)/60)

print(a, aseconds, aminutes)
