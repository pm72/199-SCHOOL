data = -1
s = 0

while data != 0:
  data = eval(input("Enter a number [0 – ends input]: "))

  s += data

print(f"The sum is {s}")
