Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x, y = 45, 58
print(x, "+", y, "=", x+y)    # 45 + 58 = 103
45 + 58 = 103

print(f"{x} + {y} = {x + y}")
45 + 58 = 103

print(f"{}")
SyntaxError: f-string: empty expression not allowed

print(f"{a}")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(f"{a}")
NameError: name 'a' is not defined


print(f"{x}{y}")    # 4558
4558

print(f"{x} {y}")    # 4558
45 58
print(f"{round(x, 2)}")
45

print(f"{float(round(x, 2))}")
45.0

print(f"{x:.2f}")
45.00
x
45

print(f"{x:.2f}{y:.2}")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(f"{x:.2f}{y:.2}")
ValueError: Precision not allowed in integer format specifier

print(f"{x:.2f}{y:.2f}")
45.0058.00
print(f"{x:.2f} {y:.2f}")
45.00 58.00

print(f"{x:10d}{y:10d}")
        45        58

print(f"{x:<10d}{y:<10d}")
45        58        
45        58
SyntaxError: invalid syntax

45        58
SyntaxError: invalid syntax




print(f"{x:<10d}{y:<-10d}")
45        58        

print(f"{x:<-10d}{y:<-10d}")
45        58        

print(f"{x:-10d}{y:<-10d}")
        4558        

print(f"{x:10d}{y:<-10d}")
        4558        
print(f"{x:<010d}{y:<010d}")
45000000005800000000

print(f"{x:010d}{y:>010d}")
00000000450000000058


print(f"{x:*>10d}{y:->10d}")
********45--------58


print(f"{x:>10d}{y:>10d}{2.58945:10.2f}")
        45        58      2.59

print(f"{x:>10d}{y:>10d}{2.58945:<10.2f}")
        45        582.59      


print(f"{x:<10d}{y:<10d}{2.58945:<10.2f}")
45        58        2.59      

print(f"{x:<10d}{y:<10d}{2.58945:<10.2f}{'Paata':<10s}")
45        58        2.59      Paata     


print(f"{x:<10d}{y:<10d}{2.58945:<3.2f}{'Paata':<10s}")
45        58        2.59Paata     

print(f"{x:<10d}{y:<10d}{1122.58945:<.2f}{'Paata':<10s}")
45        58        1122.59Paata     


print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}")
   Player              Country             Rating              Age

print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n")
   Player              Country             Rating              Age
---------------------------------------------------------------------

print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n")
   Player              Country             Rating              Age
---------------------------------------------------------------------


result = f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}\n"

print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------

result = result + f"{' ':<3s}{'Jobava':<20s}{'Georgia':<20s}{2588:<20d}{38}\n{'-' * 69}\n"
print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------

result += f"{' ':<3s}{'Caruana':<20s}{'USA':<20s}{2781:<20d}{29}\n{'-' * 69}\n"

print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
   Jobava              Georgia             2588                38
---------------------------------------------------------------------
   Caruana             USA                 2781                29
---------------------------------------------------------------------

