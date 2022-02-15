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
a = "i am here!"
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.title())

print()
print(a)


#3. მეთოდი .count()  ===>  string.count(word)
a = '''Susan is a lovely girl.
Burky is Susan's friend.
Burky plays with Susan'''
print(a.count('Susan'))
print(a.count('Burky'))
print(a.count('burky'))