##data = -1
##s = 0
##while data != 0:
##  data = eval(input("Enter a number [the input ends if it is 0]: "))
##  s += data
##
##print(f"The sum is {s}")


s = 0
while s < 100:
  data = eval(input("Enter a number [the input ends if it is 0]: "))
  s += data

print(f"The sum is {s - data}")
