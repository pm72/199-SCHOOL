Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

==================== RESTART: D:\199\chess_players.py ===================
   Player              Country             Rating              Age
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
   Jobava              Georgia             2588                38
---------------------------------------------------------------------
   Caruana             USA                 2781                29
---------------------------------------------------------------------
   Giri                Netherlands         2771                27
---------------------------------------------------------------------
   Mamedyarov          Azerbaijan          2776                36
---------------------------------------------------------------------
   Carlsen             Norway              2864                31
---------------------------------------------------------------------
   Ding                China               2799                29
---------------------------------------------------------------------
   Karjakin            Russia              2747                32
---------------------------------------------------------------------



import math as m
r = 3.8954
print("the circle's length is", round(2 * m.pi * r, 2),)
the circle's length is 24.48
print("the circle's length is", round(2 * m.pi * r, 2), "and tche area is", round(m.pi * r ** 2))
the circle's length is 24.48 and tche area is 48


length = 2 * m.pi * r
area = m.pi * r ** 2

print("the circle's length is", round(length, 2), "and tche area is", round(area, 2))
the circle's length is 24.48 and tche area is 47.67

print(f"the circle's length is {length} and tche area is {area}")
the circle's length is 24.47552004558736 and tche area is 47.6709703927905
print(f"the circle's length is {length:.2f} and tche area is {area:.2f}")
the circle's length is 24.48 and tche area is 47.67


x = 25
print("x = {x:.2f}")
x = {x:.2f}
print(f"x = {x:.2f}")
x = 25.00


print(f"x = {x:10d")
SyntaxError: f-string: expecting '}'
print(f"x = {x:10d}")
x =         25
print(f"x = {x:10}")
x =         25
print(f"x = {x:010}")
x = 0000000025

print(f"x = {x:<10}")
x = 25        

y = 69425
print(f"{x:<10d}{y}")
25        69425

print(f"{x:<10d}{y:<7d}{4598}")
25        69425  4598


print(f"{x:<10d}{y:<10d}{4598:<10d}{'Paata'}")
25        69425     4598      Paata



print(f"{' ':<3}{Player:<20}")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(f"{' ':<3}{Player:<20}")
NameError: name 'Player' is not defined
print(f"{' ':<3}{'Player':<20}")
   Player              

print(f"{' ':<3}{'Player':<20}{'Country':<20}{'Rating:<20'}{'Age'}")
   Player              Country             Rating:<20Age


print(f"{' ':<3}{'Player':<20}{'Country':<20}{'Rating':<20}{'Age'}")
   Player              Country             Rating              Age


result = f"{' ':<3}{'Player':<20}{'Country':<20}{'Rating':<20}{'Age'}"
print(result)
   Player              Country             Rating              Age


result = f"{' ':<3}{'Player':<20}{'Country':<20}{'Rating':<20}{'Age'}\n"
>>> result += "-" * 69
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
>>> 
>>> result += '\n'
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------

>>> 
>>> 
>>> result += f"{' ':<3}{'Jobava':<20}{'Georgia':<20}{2588:<20}{'38'}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38

>>> result += f"{' ':<3}{'Caruana':<20}{'USA':<20}{2781:<20}{29}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
   Caruana             USA                 2781                29

