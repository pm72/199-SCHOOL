##numb1 = eval(input("Enter number1: "))
##numb2 = eval(input("Enter number2: "))
##numb3 = eval(input("Enter number3: "))

numb1, numb2, numb3 = eval(
  input("Enter three numbers separated by commas: "))

average = (numb1 + numb2 + numb3) / 3

print("The average of", numb1, numb2, numb3, "is", round(average, 2))

