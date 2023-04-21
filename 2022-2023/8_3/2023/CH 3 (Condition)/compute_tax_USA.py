import sys
import single_filer as sf
import Married_jointly as mj
import Married_separately as ms
import head_of_household as hoh

status = 0.0
while type(status) == float:
  try:
    status = int(input("0 – Single filer\n" + \
                       "1 – Married jointly\n" + \
                       "2 – Married separately\n" + \
                       "3 – Head of household\n\n" + \
                       "Enter the filing status: "))
  except ValueError:
    print("\nPlease, enter an integer...\n")

if status < 0 or status > 3:
  print("Error: invalid status")
  input()
  sys.exit()

income = -1
while income < 0:
  income = eval(input("Enter taxable income: "))

if status == 0:
  tax = sf.tax(income)
elif status == 1:
  tax = mj.tax(income)
elif status == 2:
  tax = ms.tax(income)
else:
  tax = hoh.tax(income)


print(f"\nTax is {tax:.2f}\n" + \
      f"total income is {income - tax:.2f}")

input()
