# სტრიქონები   string

# a = "This is a string"
# print(a)
#
# a = '1234.23'
# print(a, type(a))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata Mamporia, \
# I love Rugby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is Paata Mamporia, " \
#         "I love Rugby."
# print(intro)
#
# print()
#
# intro = "Hello there!\n\
# My name is Paata Mamporia,\n\
# I love Rugby."
# print(intro, "\n")
#
# intro = """Hello there!
# My name is Paata Mamporia,
# I love Rugby."""
# print(intro, "\n")
#
# intro = '''Hello there!
#       My name is Paata Mamporia,
#               I love Rugby.'''
# print(intro, "\n")


# ბრჭყალები ბრჭყალებში
# "Hello!", said Susan.
# print('"Hello!", said Susan.')
# print("'Hello!', said Susan.")
#
# print()
#
# # "That's my Teddy", said Pedro
# print("\"That's my Teddy\", said Pedro")
# print('"That\'s my Teddy", said Pedro')
# print(""""That's my Teddy", said Pedro""")
# print('''"That's my Teddy", said Pedro''')


# სტრიქონების კონკატენაცია
# str1 = "Hello"
# str2 = "there"
# string = str1 + " " + str2 + "!"
# print(string)
#
# # Susan sais "Hi!"
# a = 'Hi!'
# print('Susan sais "' + a + '"')
# print('Bob sais "' + a + '", How are you?')


# ცარიელი სტრიქონი
# a = ''
# a = ""
# print(a)


# წვდომა სტრიქონის ელემენტებთან
# a = 'Hello there!'
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[11], "\n")
#
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტრიქონში  Slice
# a = 'Hello there!'
# print(a[0:4])       # პირველი ოთხი სიმბოლო
# print(a[:4])        # პირველი ოთხი სიმბოლოდ
# print(a[5:9], "\n") # სიმბოლოები მოცემულ დიაპაზონში
#
# print(a[-4:])       # ბოლო ოთხი სიმბოლო
# print(a[-8: -3])

# a = "Hello there!"
# print(a, id(a))
#
# a = 'P' + a[1:]
# print(a, id(a))
#
# a = 'H' + a[1:]
# print(a, id(a))


# სტრიქონული მეთოდები

#1. სტრიქონის სიგრძე    len()  ===>  len(string)
# a = "Hello there!"
# print(len(a))

#2. მეთოდები .capitalize(), .upper(), .lower(), .title()
# string.capitalize()  string.upper()
# a = "i am here!"
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.title())
#
# print()
# print(a)


#3. მეთოდი .count()  ===>  string.count(word)
# a = '''Susan is a lovely girl.
# Burky is Susan's friend.
# Burky plays with Susan'''
# print(a.count('Susan'))
# print(a.count('Burky'))
# print(a.count('burky'))


#4. .strip(), .lstrip(), .rstrip()
# a = "   Helllo there!    "
# print(a.strip())
#
# a = "#####I am Here!#############"
# print(a.strip('#'))

# a = "\t\tMy name is Paata mamporia I am Here! I am a teacher.\n\n\n"
# a = a.strip('\n')
# a = a.strip('\t')
# print(a)
#
#
# a = "\t\t\nMy name is Paata mamporia I am Here! I am a teacher.\t\n\n\n"
# a = a.strip('\t\n')
# print(a)


#5. .replace(), .find(), .index()
# a = '''Susan is a lovely girl.
# Burky is Susan's friend.
# Burky plays with Susan'''
# print(a.replace('Susan', 'Ronny'), "\n")
# print(a.replace('susan', 'Ronny'))

# a = 'I cyan love coding. I have fun with Python coding.'
# print(a.find('coding'))
# print(a.find('c'))
# print(a.find('Coding'), "\n")
#
# print(a.index('Coding'), "\n")
# print(a.index('coding'))
# print(a.index('c'))


#6. .split()
# სინტაქსი:  string.split(separator, limit)
# a = "I love coding."
# print(a.split())      # separator=' ' and separator='\n' and separator='\t' limit = inf
#
# a = "I love coding.\nI have fun with Python\t\tcoding."
# print(a.split())      # separator=' ' and separator='\n' and separator='\t' limit = inf
#
# a = "I love coding.\nI have fun with Python\t\tcoding."
# print(a.split('.'))      # separator=' ' and separator='\n' and separator='\t' limit = inf
#
# a = "I love coding.\nI have fun with Python\t\tcoding."
# print(a.split('.\n'))      # separator=' ' and separator='\n' and separator='\t' limit = inf
#
# print('numbers#12345#numbers#67890'.split('#'))
# print('numbers#12345#numbers#67890'.split('#', 1))
# print('numbers#12345#numbers#67890'.split('#', 2))


#7. ოპერატორი 'in'   ====>  True ან False (ჭეშმარიტი / მცდარი)
a = "Burku is Ronny's best friend."
print('best friend' in  a)
print('Best friend' in  a)


#8. .isalnum(),  .isalpha(),  .isnumeric()