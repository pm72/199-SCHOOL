import sys

try:
  import single_filer as sf
  import married_jointly as mj
  import married_separately as ms
  import head_of_household as hoh
except ModuleNotFoundError as error:
  print(error)
  input("\nPress 'ENTER' to exit...")
  sys.exit()

status = ''
while type(status) != int:
  try:
    status = int(input("0 – Single filer\n" + \
                       "1 – Married jointly\n" + \
                       "2 – Married separately\n" + \
                       "3 – Head of household\n\n" + \
                       "Enter the filing status: "))
  except ValueError:
    print("\nPlease, enter an integer for status...\n")
    continue

  if status < 0 or status > 3:
    print("\nError: invalid status\n")
    status = ''

income = ''
while type(income) != int and type(income) != float:
  try:
    income = eval(input("Enter income: "))
  except SyntaxError:
    print("\nPlease, enter number for income...\n")
  except NameError:
    print("\nPlease, enter number for income...\n")

if status == 0:
  tax = sf.tax(income)
  status = 'Single filer'
elif status == 1:    # else if status == 1
  tax = mj.tax(income)
  status = 'Married jointly'
elif status == 2:
  tax = ms.tax(income)
  status = 'Married separately'
else:
  tax = hoh.tax(income)
  status = 'Head of household'


print(f"\n{status}" + \
      f"\nTax: {tax:.2f}\n" + \
      f"Remaining income: {(income - tax):.2f}")


# =================
input("\nPress 'ENTER' to exit...")
