data = -1
s = 0
n = 0

while data != 0:
  data = eval(input("Enter positive number [0 – ends input]: "))

  if data > 0:
    s += data
    n += 1

if n != 0:
  avg = s / n

  print(f"The average is {avg:.2f}")
else:
  print("The average is 0.00")
