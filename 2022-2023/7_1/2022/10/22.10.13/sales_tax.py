# Prompt the user for input
purchase_amount = eval(input("Enter purchase amount: "))

# Compute sales tax
tax = purchase_amount * 10 / 100

# Display tax amount with two digits after decimal point
print("Sales tax is", round(tax, 2))
print("Total pay is", round(purchase_amount + tax, 2))
