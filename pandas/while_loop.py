x = 256
total = 0

while x > 0:
  x //= 2
  
  if total > 500:
    break

  total += x
  


print(total)


# ===============
input("\n\nDone!\n")
