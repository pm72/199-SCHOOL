from sets import set1, set2, set3, set4, set5

day = 0

print("=====> SET 1 <=====")
print(set1)
answer = int(input("Is your birthday in set 1?\n" + \
                   "Enter 0 for 'NO' or 1 for 'YES': "))

if answer == 1:
  day += 1


print("\n=====> SET 2 <=====")
print(set2)
answer = int(input("Is your birthday in set 2?\n" + \
                   "Enter 0 for 'NO' or 1 for 'YES': "))

if answer == 1:
  day += 2


print("\n=====> SET 3 <=====")
print(set3)
answer = int(input("Is your birthday in set 3?\n" + \
                   "Enter 0 for 'NO' or 1 for 'YES': "))

if answer == 1:
  day += 4


print("\n=====> SET 4 <=====")
print(set4)
answer = int(input("Is your birthday in set 4?\n" + \
                   "Enter 0 for 'NO' or 1 for 'YES': "))

if answer == 1:
  day += 8


print("\n=====> SET 5 <=====")
print(set5)
answer = int(input("Is your birthday in set 5?\n" + \
                   "Enter 0 for 'NO' or 1 for 'YES': "))

if answer == 1:
  day += 16


print(f"\nYour birthday is {day}")

input()
