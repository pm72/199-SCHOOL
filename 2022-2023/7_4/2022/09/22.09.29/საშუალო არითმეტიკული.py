##number1 = eval(input("Enter the first number: "))
##number2 = eval(input("Enter the second number: "))
##number3 = eval(input("Enter the three number: "))

number1, number2, number3 = eval(
  input("Enter the three numbers separated by commas: "))

average = (number1 + number2 + number3 ) / 3

print("The average of", number1, number2, number3, "is", average)
