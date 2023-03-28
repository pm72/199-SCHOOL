##print("Programming is fun!\n" * 10)

##count = 1
##while count <= 10:
##  print("Programming is fun!")
##
##  count += 1


i = 123
s = 0

print(f"The sum if {i}", end=' ')

if i % 2 == 1:
  i += 1

while i <= 324:
  s += i
  
  i += 2

print(f"and {i - 1} nummbers is {s}")
