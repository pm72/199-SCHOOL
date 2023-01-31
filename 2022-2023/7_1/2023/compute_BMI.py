weight = eval(input("Enter weight in kilograms: "))
height = eval(input("Enter height in metres: "))

bmi = weight / height ** 2
result = None

if bmi < 18.5:
  result = "Underweight"
elif bmi < 24.9:
  result = "Normal"
elif bmi < 29.9:
  result = "Overweight"
else:
  result = "Obese"

print(f"BMI  is {bmi:.2f}\n" + \
      result)
