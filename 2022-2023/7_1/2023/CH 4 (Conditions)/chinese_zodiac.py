year = int(input("Enter an year: "))

zodiac_year = year % 12

if zodiac_year == 0:
  animal = 'Monkey'
elif zodiac_year == 1:
  animal = 'Rooster'
elif zodiac_year == 2:
  animal = 'Dog'
elif zodiac_year == 3:
  animal = 'Pig'
elif zodiac_year == 4:
  animal = 'Rat'
elif zodiac_year == 5:
  animal = 'Ox'
elif zodiac_year == 6:
  animal = 'Tiger'
elif zodiac_year == 7:
  animal = 'Rabbit'
elif zodiac_year == 8:
  animal = 'Dragon'
elif zodiac_year == 9:
  animal = 'Snake'
elif zodiac_year == 10:
  animal = 'Horse'
else:
  animal = 'Sheep'

print(animal)
  
