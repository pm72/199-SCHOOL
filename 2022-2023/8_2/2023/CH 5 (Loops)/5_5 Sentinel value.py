data = 1
s = 0
n = 0

while data != 0:
  data = eval(input("Enter a number [0 - Ends input]: "))

  if data > 0:
  n += 1


print(f"The average is {((s-1) / (n-1)):.2f}")
