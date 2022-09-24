purshase_amount = eval(input("Enter purshase amount: "))

tax = purshase_amount * 0.06

print("Sales tax is", int(tax * 100) / 100.0)
print(f"Sales tax is {tax:.2f}")

tax = round(tax, 2)
print(tax)
 
