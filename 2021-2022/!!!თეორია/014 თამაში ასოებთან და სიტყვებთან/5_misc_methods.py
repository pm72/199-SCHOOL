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
