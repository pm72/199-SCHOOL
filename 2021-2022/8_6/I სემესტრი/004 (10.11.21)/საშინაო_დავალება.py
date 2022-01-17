num1 = 3
num2 = 5.5
num3 = 3 + 5j

# Convert num1 into a floating point number
# გარდაქმენით num1 რიცხვი ათწილადად
num1 = float(num1)


# Convert num2 into an integer
# გარდაქმენით num2 რიცხვი მთელ ტიპად
num2 = int(num2)


# Extract the imaginary part of num3 and place it back in num3
# num3 კომპლექსური რიცხვიდან ამოიღეთ imag ნაწილი და
# მიღებული რიცხვი მოათავსეთ num3 ცვლადში
num3 = num3.imag


# Convert the imaginary number (floating) into an int
# მიღებული imag რიცხვი გარდაქმენით მთელი ტიპის რიცხვად
num3 = int(num3)


#Print everything
# დაბეჭდეთ ყველა ცვლადი
print(num1)
print(num2)
print(num3)
