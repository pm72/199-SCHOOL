Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x, y = 45, 58
print(x, "+", y, "=", x + y)      # 45 + 58 = 103
45 + 58 = 103

print(f"{x} + {y} = {x + y}")
45 + 58 = 103


x, y = 2/3, 1/3
print(f"{}{}")
SyntaxError: f-string: empty expression not allowed
print(f"{x}{y}")
0.66666666666666660.3333333333333333

print(f"{x:.2f} {y.2f}")
SyntaxError: invalid decimal literal
print(f"{x:.2f} {y:.2f}")
0.67 0.33

round(2/3, 2)
0.67

)
SyntaxError: unmatched ')'


a = 5

print(round(float(a), 2))
5.0
print(round(a, 2))
5

print(f"{a:.2f}")
5.00
print(f"{a:.12f}")
5.000000000000

x, y = 45, 2.589214
print(f"{x} {y:.2f}")
45 2.59

print(f"{x:10d} {y:10.2f}")
        45       2.59

print(f"{x:10d}{y:10.2f}")
        45      2.59

print(f"{x:010d}{y:010.2f}")
00000000450000002.59

print(f"{x:>10d}{y:>10.2f}")
        45      2.59
print(f"{x:->10d}{y:*>10.2f}")
--------45******2.59

print(f"{x:<10d}{y:<10.2f}")
45        2.59      
print(f"{x:<10d}{y:-<10.2f}")
45        2.59------

print(f"{x:<10d}{'Paata':<10
      }{y:<10.2f}")
SyntaxError: unterminated string literal (detected at line 1)
print(f"{x:<10d}{'Paata':<10}{y:<10.2f}")
45        Paata     2.59      

print(f"{x:<10d}{'Paata':<3}{y:<10.2f}")
45        Paata2.59      


print(f"{x:<10d}{'Paata'}{y:<10.2f}")
45        Paata2.59      


print(f"{' ':<3s}{'Player':<20s}{'Rating':<20s}{}{'Age'}")
SyntaxError: f-string: empty expression not allowed

print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}")
   Player              Country             Rating              Age

print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}")
   Player              Country             Rating              Age
---------------------------------------------------------------------







print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n")
   Player              Country             Rating              Age
---------------------------------------------------------------------




result = f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n"
>>> 
>>> result = result + f"{' ':<3s}{'Jobava':<20s}{'Georgia':<20s}{2588:<20d}{38}\n{'-' * 69}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------

>>> 
>>> 
>>> 
>>> result += f"{' ':<3s}{'Caruana':<20s}{'USA':<20s}{2781:<20d}{29}\n{'-' * 69}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------
   Caruana             USA                 2781                29
---------------------------------------------------------------------

>>> 
>>> 
>>> 
