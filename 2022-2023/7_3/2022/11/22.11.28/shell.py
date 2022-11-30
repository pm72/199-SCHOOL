Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x, y = 2.589458, 1.897456
print(x, y)
2.589458 1.897456
print(f"{x} + {y} = {x + y}")
2.589458 + 1.897456 = 4.4869140000000005

print(f"{x:.2f} + {y:.2f} = {(x + y):.2f}")
2.59 + 1.90 = 4.49


print(f"{x:10.2f}{y:10.2f}")
      2.59      1.90

print(f"{x:>10.2f}{y:>10.2f}")
      2.59      1.90
2.59      1.90
SyntaxError: invalid syntax

print(f"{x:>10.2f}{y:>3.2f}")
      2.591.90

print(f"{x:>10.2f}{y:>.2f}")
      2.591.90


header = f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age}\n{'-' * 69}\n"
SyntaxError: f-string expression part cannot include a backslash

header = f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n"

print(header)
   Player              Country             Rating              Age
---------------------------------------------------------------------


info = f"{' ':<3s}{'Jobava':<20s}{'Georgia':<20s}{2588:<20d}{38}\n{'-' * 69}\n"

print(info)
   Jobava              Georgia             2588                38
---------------------------------------------------------------------

>>> 
>>> print(header, info)
   Player              Country             Rating              Age
---------------------------------------------------------------------
    Jobava              Georgia             2588                38
---------------------------------------------------------------------

>>> 
>>> info += f"{' ':<3s}{'Caruana':<20s}{'USA':<20s}{2781:<20d}{29}\n{'-' * 69}\n"
>>> 
>>> print(header, info)
   Player              Country             Rating              Age
---------------------------------------------------------------------
    Jobava              Georgia             2588                38
---------------------------------------------------------------------
   Caruana             USA                 2781                29
---------------------------------------------------------------------

>>> 
>>> print(header, info, sep='')
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------
   Caruana             USA                 2781                29
---------------------------------------------------------------------

