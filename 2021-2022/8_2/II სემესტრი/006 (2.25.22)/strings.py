# სტრიქონები  string

# a = "This is a string"
# print(a)
#
# a = "d"
# print(a, type(a))
#
# a = "14562"
# print(a, type(a))
#
# a = 14.562
# print(a, type(a))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata Mamporia, \
# I am 49 years old. \
# I love Rygby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is Paata Mamporia, " \
#         "I am 49 years old. " \
#         "I love Rygby."
# print(intro)
#
# print()

# '\n'  ახალ ხაზზე გადასვლა  New line  End line  ENTER
# intro = "Hello there!\n\
# My name is Paata Mamporia,\n\
# I am 49 years old.\n\
# I love Rygby."
# print(intro, "\n")
#
# intro = """Hello there!
# My name is Paata Mamporia,
# I am 49 years old.
# I love Rygby."""
# print(intro, "\n")
#
# intro = '''Hello there!
# My name is Paata Mamporia,
# I am 49 years old.
# I love Rygby.'''
# print(intro, "\n")
#
# intro = '''Hello there!
#         My name is Paata Mamporia,
#               I am 49 years old.
#                     I love Rygby.'''
# print(intro, "\n")


# ბრჭყალები ბრჭყალებში
# "Hello!", said Susan.
# print(""Hello!", said Susan.")
# print('"Hello!", said Susan.')
# # print("'Hello!', said Susan.")
# # print("""'Hello!', said Susan.""")
# #
# # # "That's is my Teddy", said Pedro.
# # print("\"That's is my Teddy\", said Pedro.")
# # print('"That\'s is my Teddy", said Pedro.')
# # print('''"That's is my Teddy", said Pedro.''')
# #
# # print("c:\\users\\paata\\strings.py")
# # print(r"c:\users\paata\strings.py")
# # print(r"c:\users\paata\strings.py\n")
# # print(r"c:\users\paata\strings.py", "\n")


# ცარიელი სტრიქონი
# a = ''
# a = ""
# print(a, type(a))


# სტრიქონების „შეკრება“ '+' ოპერატორით (კონკატენაცია)
# str1 = "Hello"
# str2 = "there"
# string = str1 + " " +  str2 + "!"
# print(string)

# Susan sais "Hi"!
# a = 'Hi'
# # print('Susan sais "' + a + '"!')
# # print('Daniel sais "' + a + '"!')
# # print('Kety sais "' + a + '"!')


# წვდომა სტრიქონის სიმბოლოებზე
# a = 'Hello there!'
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[11], "\n")
#
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტიქონში Slice. სინტაქსი: string[start:stop-1:step=1]
a = 'Hello there!'
print(a[0:4:1])
print(a[0:4])
print(a[:4])
print(a[2:7])
print(a[2:9:3])
print(a[3:])
print(a[-4:])
print(a[-9::3])
print(a[2::3])
print(a[::3])