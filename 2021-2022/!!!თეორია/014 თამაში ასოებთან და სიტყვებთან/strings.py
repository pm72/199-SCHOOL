# a = 'This is a striing'
# print(a)

# a = "This is a string too"
# print(a)

# a = '1234'
# print(type(a))


# a = "This is the first line.
# This is the second line.
# This is the last line."

# print(a)


# intro = '''This is the first line.
# This is the second line.
# This is the last line.
# '''

# print(intro)


# intro = ""Hello!", said susan"

# intro = '"Hello!", said susan'
# print(intro)


# intro = '"that\'s my Teddy", said susan'
# print(intro)

# სტრიქონების შეერთება, კონკატენაცია
# str1 = "Hello"
# str2 = 'there!'
# string = str1 + str2
# string = str1 + " " + str2
# print(string)


# სტრიქონების კონკატენაცია print-ში
# a = 'Hi'
# print("Susan says, " + a)
# print('Susan says, "' + a + '"')


# ცარიელი სტრიქონი
# a = ''


# სიმბოლოებთან წვდომა სტრიქონში
# a = "Hello there!"

# print(a[0])
# print(a[12-1])
# print(a[-1])
# print(a[-8])


# ჭრები სტრიქონში slice
# a = "Hello there!"
# print(a[0: 4])
# print(a[8: 12])
# print(a[-4: -1])
# print(a[-4:])


# მ ე თ ო დ ე ბ ი

#  სტრიქონის სიგრძე
# a = 'Hello there!'

# print(len(a))

# .capitalize(), .upper(), .lower(), .title(), .swapcase()
# a = "i am here"

# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.title())

# a = "I love LIONES"
# print(a.swapcase())


# სხვადასხვა მეთოდები
# 1. .count()
# a = '''Susan is lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan.'''

# print(a.count('Susan'))
# print(a.count('Barky'))

# 2. .strip(), .lstrip(), .rstrip()
# a = '    Hello there!   '
# print(a.strip())
# print(a)

# 3. .replace()
# a = '''Susan is lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan.'''

# print(a.replace('Susan', 'Ronny'))

# 4. .find()
# a = "I love coding. I have fun with coding."

# print(a.find('coding'))
# print(a.find('Coding'))

# 5. .index()
# a = "I love coding. I have fun with coding."

# print(a.index('coding'))
# print(a.index('Coding'))  # ERROR

# 6. .split()
# a = "I love coding."

# print(a.split(' '))
# print(a.split())
# print(a.split('.'))
# print(a.split('I '))

# 7. in
# string = "Barky is Ronny's best friend."

# print("best friend" in string)
# print("Best friend" in string)

# print('Python' in 'Python is fun')
# print('Coding' in 'Python is fun')

# 8. .isalnum()  #  მხოლოდ ციფრები და ასოები
# a = 'number123number253'
# print(a.isalnum())

# a = 'number 123 number 253'
# print(a.isalnum())

# 9. .isalpha(), .isnumeric()
# a = 'number123number253'
# print(a.isalpha())

# a = 'number is fun'
# print(a.isalpha())

# a = 'numbers'
# print(a.isalpha())

# a = '5482'
# print(a.isnumeric())

# 10. .isupper(), .islower(), .istitle()
# a = "My name is Paata Mamporia"

# print(a.isupper())
# print(a.islower())
# print(a.istitle())


# სტრიქონების ფორმატირება
# a = 4
# b = 5
# sum_ = a + b

# მინდა დავბეჭდო 4 + 5 = 9
# print(a + " + " + b + " = " + sum_)
# print(str(a) + " + " + str(b) + " = " + str(sum_))
# print(a, "+", b, "=", sum_)
# print("{} + {} = {}".format(a, b, sum_))
# print(f"{a} + {b} = {sum_}")
# print(f"The answer is: {a} + {b} = {sum_}")

# a = 'apple'
# print(f"This is an {a}")
# print(f"This is an '{a}'")

# a = "Apples"
# b = "Bananas"

# print(f"{a} and {b} are good for your health.")

# recept = f"{a} and {b} are very good for your health."
# print(recept)


# ინფორმაციის შეტანა კლავიატურიდან, ეკრანიდან
# ფყნქცია input()
# message = input("Enter your message: ")
# print("Here is your message: " + message)

# სტრიქონების გარდაქმნა რიცხვებად ფუნქციები int() და float()
