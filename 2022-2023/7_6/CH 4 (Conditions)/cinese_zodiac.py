year = int(input("Enter year: "))
z = year % 12

if z == 0:
  zodiac = "Monkey"
elif z == 1:
  zodiac = "Rooster"
elif z == 2:
  zodiac = "Dog"
elif z == 3:
  zodiac = "Pig"
elif z == 4:
  zodiac = "Rat"
elif z == 5:
  zodiac = "Ox"
elif z == 6:
  zodiac = "Tiger"
elif z == 7:
  zodiac = "Cat/Rabbit"
elif z == 8:
  zodiac = "Dragon"
elif z == 9:
  zodiac = "Snake"
elif z == 10:
  zodiac = "Horse"
else:
  zodiac = "Sheep"

print(zodiac)
