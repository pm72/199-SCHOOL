import sys

status = int(input("0 – Single filer\n" + \
                   "1 – Married jointly\n" + \
                   "2 – Married separately\n" + \
                   "3 – Head of household\n\n" + \
                   "Enter the taxable income: "))

if status < 0 or status > 3:
  print("\nError: invalid status")
  input()
  sys.exit()

income = eval(input("Enter the taxable income: "))

if status == 0:
  fix10 = 8350
  fix15 = 33950
  fix25 = 82250
  fix28 = 171550
  fix33 = 372950

  if income <= fix10:
    tax = income * 0.1
  elif income <= fix15:
    tax = fix10 * 0.1 + (income - fix10) * 0.15
  elif income <= fix25:
    tax = fix10 * 0.1 + (fix15 - fix10)* 0.15 + \
          (income - fix15) * 0.25
  elif income <= fix28:
    tax = fix10 * 0.1 + (fix15 - fix10)* 0.15 + \
          (fix25 - fix15) * 0.25 + (income - fix25) * 0.28
  elif income <= fix33:
    tax = fix10 * 0.1 + (fix15 - fix10)* 0.15 + \
          (fix25 - fix15) * 0.25 + (fix28 - fix25) * 0.28 + \
          (income - fix28) * 0.33
  else:
    tax = fix10 * 0.1 + (fix15 - fix10)* 0.15 + \
          (fix25 - fix15) * 0.25 + (fix28 - fix25) * 0.28 + \
          (fix33 - fix28) * 0.33 + (income - fix33) * 0.35  
elif status == 1: 
  print("\nMarried jointlyr")
elif status == 2:
  ...
else:
  ...


print(f"Tax is {tax:.2f}\n" + \
      f"Total income: {income - tax:.2f}")

input()