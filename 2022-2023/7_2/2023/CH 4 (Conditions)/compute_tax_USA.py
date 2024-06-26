import sys

try:
  import single_filer as sf
  import married_jointly as mj
  import married_separately as ms
  import head_of_household as hoh
except ModuleNotFoundError as error:
  print(error)
  input("\nPress ENTER to exit...")
  sys.exit()

status = 0.0
while type(status) == float:
  try:
    status = int(input("0 – Single filer\n" + \
                       "1 – Married jointly\n" + \
                       "2 – Married separately\n" + \
                       "3 – Head of household\n\n" + \
                       "Enter the filing status: "))

    if status < 0 or status > 3:
      print("\nError: invalid status\n")
      status = 0.0
      continue
  except ValueError:
    print("\nPlease, enter an integer...\n")

income = ''
while type(income) != int and type(income) != float:
  try:
    income = eval(input("Enter the taxable income: "))
  except NameError:
    print("\nPlease, enter number for income \n")

if status == 0:
  tax = sf.tax(income)
elif status == 1:
  tax = mj.tax(income)
elif status == 2:
  tax = ms.tax(income)
else:
  tax = hoh.tax(income)

print(f"\nTax is {tax:.2f}\n" + \
      f"Total income is {income - tax:.2f}")

input("\nPress ENTER to exit...")
