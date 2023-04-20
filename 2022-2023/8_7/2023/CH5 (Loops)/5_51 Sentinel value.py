data = -1
s = 0
n = 0

while data != 0:
  data = eval(input())

  if data > 0:
    print(data, end='  ')
    s += data
  else:
    continue

  n += 1

if s == 0:
  print(f"The average is {s:.2f}")
else:
  print(f"\n\nThe average is {(s / (n)):.2f}")



''' command promt   cmd
კლავიშები:
  WIN + R   ===> cmd გაშვება

  dir   ===> ფაილების და საქაღალდეების დათვალიერება
  d:    ===> D დისკზე გადასვლა
  cd D:\199\7_3\2023\CH 5 (Loops)  ====> საქაღალდეში გადასვლა
  cls   ===> კონსოლის (ეკრანის) გასუფთავება

'''
