import time

password = 12345

p = eval(input("Enter password: "))
i = 0

while i < 4:
  i += 1
  if p == password:
    break

  p = eval(input("Enter password:"))

time.sleep(3)
