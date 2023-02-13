import sys
import single_filer as sf
import married_jointly as mj

status = 0.0
while type(status) == float:
  try:
    status = int(input(
      "0 – Single filer\n" + \
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

income = eval(input("Enter the taxable income: "))

tax = 0

if status == 0:
  tax = sf.tax(income)
elif status == 1:
  tax = mj.tax(income)
elif status == 2:
  pass
elif status == 3:
  ...
else:
  print("Error: invalid status")
  sys.exit()

print(f"\nTax is {tax:.2f}")
print(f"Total income is {income - tax:.2f}")


# =============
input()
