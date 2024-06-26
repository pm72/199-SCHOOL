import sys

try:
  import single_filer as sf
  import married_jointly as mj
  import married_separately as ms
  import head_of_household as hoh
except ModuleNotFoundError as error:
  print(error)
  input("\nPlease, type 'ENTER' to exit...")
  sys.exit()

status = ''   # str
while type(status) != int:
  try:
    status = int(input("0 – Single filer\n" + \
                       "1 – Married jointly\n" + \
                       "2 – Married separately\n" + \
                       "3 – Head of household\n\n" + \
                       "Enter the filing status: "))
  except ValueError:
    print("\nPlease, enter an integer...\n")
    continue

  if status < 0 or status > 3:
    print("\nError: invalid status\n")
    status = ''

income = ''
while type(income) != int and type(income) != float:
  try:
    income = eval(input("Enter income: "))
  except SyntaxError:
    print("\nPlese, enter number for 'Income'...\n")
  except NameError:
    print("\nPlese, enter number for 'Income'...\n")
  
if status == 0:
  tax = sf.tax(income)
  status = "Single filer"
elif status == 1:   # else if == 1:
  tax = mj.tax(income)
  status = "Married jointly"
elif status == 2:
  tax = ms.tax(income)
  status = "Married separately"
else:
  tax = hoh.tax(income)
  status = "Head of household"

print(f"\nStatus: {status}\n" + \
      f"Tax: {tax:.2f}\n" + \
      f"Remamaining income: {income - tax:.2f}")


# ===============
input()
