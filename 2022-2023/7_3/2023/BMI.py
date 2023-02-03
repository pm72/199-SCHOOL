weight = eval(input("Enter weight in kilogram: "))
height = eval(input("Enter height in metre: "))

bmi = weight / height ** 2

if bmi < 18.5:
  helth = "Underweight"
elif bmi < 25:
  helth = "Normal"
elif bmi < 30:
  helth = "Overweight"
else:
  helth = "Obese"


print(f"\nBMI is {bmi:.2f}\n" + \
      f"{helth}")
