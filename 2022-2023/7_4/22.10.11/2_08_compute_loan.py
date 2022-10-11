# Enter loan amount  (სესხი)
loan_amount = eval(input("Enter loan amount, e.g., 120000.95: "))

# Enter number of years  (წლების რაოდენობა)
number_of_years = eval(
  input("Enter number of years as an integer, e.g., 5: "))

# Enter annual interest rate as a percentage, e.g., 7.25
# წლიური საპროცენტო განაკვეთი პროცენტებში
annual_interest_rate = eval(
  input("Enter annual interest rate, e.g., 7.25: "))

# obtain monthly interest rate
# მიიღეთ ყოველთვიური საპროცენტო განაკვეთი
monthly_interest_rate = annual_interest_rate / 1200

# Calculate payment  (გამოვთვალოთ გადახდა)
monthly_payment = (loan_amount * monthly_interest_rate) / (
  1 - 1 / (1 + monthly_interest_rate) ** (number_of_years * 12))

total_payment =  monthly_payment * number_of_years * 12

# Display results
print("The montly payment is", round(monthly_payment, 2))
print("The total payment is", round(total_payment, 2))
