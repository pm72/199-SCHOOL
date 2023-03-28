import sys
import single_filer as sf
import married_jointly as mj
import married_separately as ms
import head_of_household as hoh

status = 0.0
income = ''
while type(status) == float or type(income) == str:
  try:
    status = int(input(
      "0 – Single filer\n" + \
      "1 – Married jointly\n" + \
      "2 – Married separately\n" + \
      "3 – Head of household\n\n" + \
      "Enter the filing status: "))

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
      tax = ms.tax(income)
    elif status == 3:
      tax = hoh.tax(income)
    else:
      print("Error: invalid status")
      sys.exit()

    print(f"\nTax is {tax:.2f}")
    print(f"Total income is {income - tax:.2f}")

  except ValueError:
      print("\nPlease, enter an integer between 0 and 3 ...\n")
  except SyntaxError:
    print("\nPlease enter correct value for income... \n")
  except NameError:
    print("\nIncome value must be numeric...\n")


# =============
input()
