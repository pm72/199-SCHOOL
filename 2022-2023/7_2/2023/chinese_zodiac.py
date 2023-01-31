year = int(input("Enter an year: "))
z = year % 12

if z == 0:
  animal = "Monkey"
elif z == 1:
  animal = 'Rooster'
elif z == 2:
  animal = 'Dog'
elif z == 3:
  animal = 'Pig'
elif z == 4:
  animal = 'Rat'
elif z == 5:
  animal = 'Ox'
elif z == 6:
  animal = 'Tiger'
elif z == 7:
  animal = 'Rabbit'
elif z == 8:
  animal = 'Dragon'
elif z == 9:
  animal = 'Snake'
elif z == 10:
  animal = 'Horse'
else:
  animal = 'Sheep'


print(animal)
