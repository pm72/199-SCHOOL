amount = eval(input("Enter a purshuse amount: "))
tax = eval(input("Enter a tax %: "))

sales_tax = amount * (tax / 100)

print("Sales Tax is", round(sales_tax, 2))
print("Total sale is", round(amount + sales_tax, 2))
