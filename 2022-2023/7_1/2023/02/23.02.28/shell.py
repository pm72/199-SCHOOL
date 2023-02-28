Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2 < 3
True
1.25 == 0
False


(2 + 3) / (7 * 8)
0.08928571428571429


2 < 3 or 1.25 == 0
True
2 < 3 and 1.25 == 0
False

# ჭეშმარიტობის ცხრილი AND-ისთვის
'''
True and True = True       1 * 1 = 1
True and False = False     1 * 0 = 0
False and True = False     0 * 1 = 0
False and False = False    0 * 0 = 0
'''
'\nTrue and True = True       1 * 1 = 1\nTrue and False = False     1 * 0 = 0\nFalse and True = False     0 * 1 = 0\nFalse and False = False    0 * 0 = 0\n'


# ჭეშმარიტობის ცხრილი OR-ისთვის
'''
True or True = True       1 + 1 = 1
True or False = True      1 + 0 = 1
False or True = True      0 + 1 = 1
False or False = False    0 + 0 = 0
'''
'\nTrue or True = True       1 + 1 = 1\nTrue or False = True      1 + 0 = 1\nFalse or True = True      0 + 1 = 1\nFalse or False = False    0 + 0 = 0\n'


# not
# not True = False
# not False = True

not 5
False

not 0
True

int(not 5)
0

int(not 0)
1

not(5 > 3)
False

not not(3 != 2)
True



# ნაკიანი წელიწადი

year = 1900
print((year % 4 == 0 and year % 100 != 0) or \)
      
SyntaxError: unexpected character after line continuation character

print((year % 4 == 0 and year % 100 != 0) or \)
      
SyntaxError: unexpected character after line continuation character

print((year % 4 == 0 and year % 100 != 0) or \ year % 400 == 0)
      
SyntaxError: unexpected character after line continuation character
print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
      
False

year = 300
      
print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
      
False

year = 2024
      
year = 2024
      
print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
      
True

============== RESTART: D:/199/7_1/2023/leep_year.py ==============
Enter a year: 1900
False

============== RESTART: D:/199/7_1/2023/leep_year.py ==============
Enter a year: 3100
False

============== RESTART: D:/199/7_1/2023/leep_year.py ==============
Enter a year: 2028
True

============== RESTART: D:/199/7_1/2023/leep_year.py ==============
Enter a year: 2005
False
2005 is not leap.

============== RESTART: D:/199/7_1/2023/leep_year.py ==============
Enter a year: 2006
2006 is not leap.

============== RESTART: D:/199/7_1/2023/leep_year.py ==============
Enter a year: 2008
2008 is leap.
>>> 
===== RESTART: D:/199/7_1/2023/leep_year.py =====
Enter a year: 2000
2000 is leap
>>> 
===== RESTART: D:/199/7_1/2023/leep_year.py =====
Enter a year: 0
1
>>> 
>>> 
===== RESTART: D:/199/7_1/2023/leep_year.py =====
Enter a year: 0
1
-1
>>> 
===== RESTART: D:/199/7_1/2023/leep_year.py =====
1
1
>>> 
====== RESTART: D:/199/7_1/2023/lottery.py ======
Enter your lottery pick (two digits): 77
Match one digit: you win $1,000
>>> 
====== RESTART: D:/199/7_1/2023/lottery.py ======
Enter your lottery pick (two digits): 69
The lottery number is 37
Sorry, no match
>>> 
