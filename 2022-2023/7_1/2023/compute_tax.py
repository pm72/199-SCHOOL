import sys

status = int(input(
  "0 – Single filer\n" + \
  "1 – Married jointly\n" + \
  "2 – Married separately\n" + \
  "3 – Head of household\n" + \
  "Enter the filing status: "))

income = eval(input("Enter the taxable income: "))

tax = 0

if status == 0:
  if income <= 8350:
    tax = income * 0.1
  elif income <= 33950:
    tax = 8350 * 0.1 + (income - 8350) * 0.15
  elif income <= 82250:
    tax = 8350 * 0.1 + 33950 * 0.15 + (income - 33950) * 0.25
  elif income <= 171550:
    tax = 8350 * 0.1 + 33950 * 0.15 + 33950 * 0.25 + \
          (income - 82250) * 0.28
  elif income <= 372950:
    tax = 8350 * 0.1 + 33950 * 0.15 + 33950 * 0.25 + \
          82250 * 0.28 + (income - 171550) * 0.33
  else:
    tax = 8350 * 0.1 + 33950 * 0.15 + 33950 * 0.25 + \
          82250 * 0.28 + 171550 * 0.33 + \
          (income - 372950) * 0.35
elif status == 1:
  ...
elif status == 2:
  pass
elif status == 3:
  ...
else:
  print("Error: invalid status")
  sys.exit()

print(f"Tax is {tax:.2f}")
