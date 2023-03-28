day = 0

# set1
print("=====> SET 1 <====")
print(" 1   3   5   7\n" + \
      " 9  11  13  15\n" + \
      "17  19  21  23\n" + \
      "25  27  29  31\n")

answer = int(input("Is your birthday date in set 1?\n" + \
                   "Enter 0 for NO or 1 for YES: "))

if answer == 1:
  day += 1


# set2
print("\n")
print("=====> SET 2 <====")
print(" 2    3    6   7\n" + \
      "10   11   14   15\n" + \
      "18   19   22   23\n" + \
      "26   27   30   31\n")

answer = int(input("Is your birthday date in set 2?\n" + \
                   "Enter 0 for NO or 1 for YES: "))

if answer == 1:
  day += 2


# set3
print("\n")
print("=====> SET 3 <====")
print(" 4    5    6    7\n" + \
      "12   13   14   15\n" + \
      "20   21   22   23\n" + \
      "28   29   30   31\n")

answer = int(input("Is your birthday date in set 3?\n" + \
                   "Enter 0 for NO or 1 for YES: "))

if answer == 1:
  day += 4


# set4
print("\n")
print("=====> SET 4 <====")
print(" 8   9    10   11\n" + \
      "12   13   14   15\n" + \
      "24   25   26   27\n" + \
      "28   29   30   31\n")

answer = int(input("Is your birthday date in set 4?\n" + \
                   "Enter 0 for NO or 1 for YES: "))

if answer == 1:
  day += 8


# set5
print("\n")
print("=====> SET 5 <====")
print("16  17  18  19\n" + \
      "20  21  22  23\n" + \
      "24  25  26  27\n" + \
      "28  29  30  31\n")

answer = int(input("Is your birthday date in set 5?\n" + \
                   "Enter 0 for NO or 1 for YES: "))

if answer == 1:
  day += 16


print(f"\nYour birthday is {day}")

input()
