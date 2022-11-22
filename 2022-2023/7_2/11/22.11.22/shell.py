Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
x, y = 45, 58
print(x, "+", y, "=", x+y)
45 + 58 = 103

r = 3.89457
length = 2 * m.pi * r
area = m.pi * r ** 2

print("Length =", round(length, 2), "and area =", round(area, 2))
Length = 24.47 and area = 47.65

print(f"Length = {length} and {area}")
Length = 24.4703050017824 and 47.65065787539584

print(f"Length = {length:.2f} and {area:.2}")
Length = 24.47 and 4.8e+01
print(f"Length = {length:.2f} and {area:.2f}")
Length = 24.47 and 47.65

print(f"{x:.2f}")    # 45.00
45.00

print(f"{x}{y}")
4558

print(f"{x:10d}{y:10d}")
        45        58

print(f"{x:<10d}{y:<10d}")
45        58        

print(f"{x:<010d}{y:<010d}")
45000000005800000000
print(f"{x:010d}{y:010d}")
00000000450000000058

print(f"*{x:10d}{y:10d}")
*        45        58
print(f"{x:*10d}{y:10d}")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(f"{x:*10d}{y:10d}")
ValueError: Invalid format specifier
print(f"{*x:10d}{y:10d}")
SyntaxError: f-string: cannot use starred expression here

print(f"{x*:10d}{y:10d}")
SyntaxError: f-string: invalid syntax


print(f"{x:>*10d}{y:>*10d}")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(f"{x:>*10d}{y:>*10d}")
ValueError: Invalid format specifier

print(f"{x:*>10d}{y:*>10d}")
********45********58

print(f"{x:1>10d}{y:*>10d}")
1111111145********58
print(f"{x:*>10d}{y:*>10d}")
********45********58
print(f"{x:12>10d}{y:*>10d}")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(f"{x:12>10d}{y:*>10d}")
ValueError: Invalid format specifier
print(f"{x:12>10d}{y:*>10d}")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(f"{x:12>10d}{y:*>10d}")
ValueError: Invalid format specifier


print(f"{x:-<10d}{y:-<10d}")
45--------58--------


print(f"{x:<10d}{y:<10d}{2.584125:10.2f}")
45        58              2.58

print(f"{x:<10d}{y:<10d}{2.584125:<10.2f}")
45        58        2.58      


print(f"{x:<10d}{y:<10d}{
      4125:<10.2f}")
SyntaxError: unterminated string literal (detected at line 1)


print(f"{x:<10d}{y:<10d}{112.584125:<10.2f}")
45        58        112.58    


print(f"{x:<10d}{y:<10d}{112.584125:<10.2f}{'Paata':<10s}")
45        58        112.58    Paata     


print(f"{' ':<3s}{}{}{}")
SyntaxError: f-string: empty expression not allowed


print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}")
   Player              Country             Rating              Age

print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n")
   Player              Country             Rating              Age
---------------------------------------------------------------------

>>> result = f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------

>>> result = result + f"{' ':<3s}{'Jobava':<20s}{'Georgia':<20s}{2588:<20d}{38}\n{'-' * 69}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------

>>> result += f"{' ':<3s}{'Caruana':<20s}{'USA':<20s}{2781:<20d}{29}\n{'-' * 69}\n"
>>> 
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------
   Caruana             USA                 2781                29
---------------------------------------------------------------------

