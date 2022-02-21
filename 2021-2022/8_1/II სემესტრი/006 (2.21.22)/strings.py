# სტრიქონები   string

# a = 'This is a string'
# print(a)
#
# letter = 's'
# print(letter, type(letter))
#
# numbers = '123.56'
# print(numbers, type(numbers))
#
# numbers = 123.56
# print(numbers, type(numbers))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata Mamporia, \
# I love Rugby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is Paata Mamporia, " \
#         "I love Rugby."
# print(intro, "\n")
#
# intro = "Hello there!\n\
# My name is Paata Mamporia,\n\
# I love Rugby."
# print(intro, "\n")
#
# intro = """Hello there!
#     My name is Paata Mamporia,
#                   I love Rugby."""
# print(intro, "\n")
#
# intro = '''Hello there!
#     My name is Paata Mamporia,
#                   I love Rugby.'''
# print(intro, "\n")


# ბრწყალები ბრჭყალებში
# "Hello there!", said Susan
# print('"Hello there!", said Susan')
# print("'Hello there!', said Susan")
#
# print()
#
# # "That's my Teddy", said Pedro
# print("\"That's my Teddy\", said Pedro")
# print('"That\'s my Teddy", said Pedro')
# print('''"That's my Teddy", said Pedro''')
# print(""""That's my Teddy", said Pedro""")
# print(r"c:\user\paata\strings.py")
# print(r"c:\user\paata\strings.py\n")
# print("c:\\user\\paata\\strings.py\n")


# სტრიქონების კონკატენაცია
# str1 = "Hello"
# str2 = "there!"
# string = str1 + " " + str2
# print(string)
#
# string = str2 + " " + str1
# print(string)
#
# print()
#
# # Susan sais 'Hi!'
# a = 'Hi!'
# print("Susan sais '" + a +


# ცარიელი სტრიქონი
# a = ''
# a = ""
#
# print(a)


# წვდომა სტრიქონის სიმბოლოებზე
# a = 'Hello there!'
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტრიქონში
# a = 'Hello there!'
#
# print(a[0:4])     # პირველი ოთხი სიმბოლო
# print(a[:4])      # პირველი ოთხი სიმბოლო
# print(a[7:12])    # სიმბოლოები მითითებული დიაპაზონით
# print(a[1:10:3])  # სიმბოლოები მითითებული დიაპაზონით
# print(a[-4:])     # ბოლო ოთხი სიმბოლო

# a = "Hello there!"
# print(a, id(a))
# # a[0] = 'T'
# a = 'T' + a[1:]
# print(a, id(a))
#
# a = "Hello there!"
# print(a, id(a))
#
# a = a[:6] + 'friends!'
# print(a, id(a))


# ==============================
# სტრიქონული მეთოდები

#1. სტრიქონის სიგრძე   len()   ===>  len(string)
# a = "Hello there!"
# print(len(a))


#2. .capitalize(), .upper(), .lower(), .title()
# a = 'i am here!'
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.title())
#
# print()
# print(a)


#3. .count()  ===>  string.count(word)
# a = '''Susan is a lovely girl.
# Bob is Susan's friend.
# Bob plays with Susan.'''
# print(a.count('Susan'))
# print(a.count('Bob'))
# print(a.count('bob'))
# print(a.count('susan'))


#3. .strip(),  .lstrip(),  .rstrip()
# a = "   I love coding.     "
# print(a)
# a = a.strip()
# print(a)
#
# a = "####My name is Paata! Mamporia!!!!!!!!!"
# a = a.strip('#')
# a = a.strip('!')
# print(a)


#4. .replace(),  .find(),  .index()
# a = '''Susan is a lovely girl.
# Bob is Susan's friend.
# Bob plays with Susan.'''
# a = a.replace('Susan', 'Ronny')
# print(a)

# a = 'I love coding. I have fun with Python coding.'
# print(a.find('coding'))
# print(a.find('Coding'))
# print(a.find('Python'))
# print(a.find('python'))
# print(a.find('P'))
#
# print(a.index('coding'))
# print(a.index('Coding'))


#5. .split()
# სინტქსი: string.split(separator, limit)
# a = 'I love coding.'
# print(a.split())  # separator=' ' and separator='\t' and separator='\n'
#
# a = 'I love coding.\nI have fun with\t\tPython coding.'
# print(a.split())  # separator=' ' and separator='\t' and separator='\n'
# print(a.split('.'))  # separator=' ' and separator='\t' and separator='\n'
# print(a.split('.\n'))  # separator=' ' and separator='\t' and separator='\n'


#6. ოპერატორი 'in'   =====>  True ან False  (შეშმარიტი / მცდარი)
# print('coding' in 'I love coding with Python.')
# print('Coding' in 'I love coding with Python.')
#
# word = 'Coding'
# string = 'I love coding with Python.'
# print(word in string)


#7. isalnum(), isalpha(), isnumeric()
a = 'numbers123numbers123'
print(a.isalnum())

a = 'numbers123numbers 123'
print(a.isalnum())

a = 'PaataMamporia'
print(a.isalpha())

a = 'Paata Mamporia'
print(a.isalpha())

a = '1234567890'
print(a.isnumeric())

a = '1234567.890'
print(a.isnumeric())


#8. sislower(), isupper(), istitle()