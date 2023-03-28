Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: D:/199/7_7/2023/addition_quiz.py ==================
What is 9 + 2? 11

= RESTART: D:/199/7_7/2023/addition_quiz.py
What is 0 + 6? 6
0 + 6 = 6 is True

= RESTART: D:/199/7_7/2023/addition_quiz.py
What is 10 + 7? 15
10 + 7 = 15 is False

= RESTART: D:/199/7_7/2023/addition_quiz.py
What is 1 + 6? 5
1 + 6 = 5 is False
1 + 6 = 7


import random as r

r.randint(10, 25)
17
r.randint(10, 25)
22

for i in range(20):
    print(r.randint(10, 25))

    
17
24
21
15
11
17
23
12
15
11
24
25
23
12
21
11
25
14
15
12


r.randrage(1, 5)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    r.randrage(1, 5)
AttributeError: module 'random' has no attribute 'randrage'. Did you mean: 'randrange'?

r.randrange(1, 5)
2
r.randrange(1, 5)
1
r.randrange(1, 5)
3
r.randrange(1, 5)
3

r.randrange(0, 1)
0
r.randrange(0, 1)
0
r.randrange(0, 1)
0
r.randrange(0, 1)
0


r.random()
0.9344448974108244

for i in range(20):
    print(r.random())

    
0.13396012435461357
0.8156241955723659
0.1732891274273931
0.14097518891053928
0.5308347547680573
0.9842060093974705
0.22105260622191691
0.24392697309842148
0.6480145038230497
0.5071441201702621
0.5988523532128067
0.7936360844464032
0.045853929580706
0.41525845537971695
0.46835133260339534
0.7240573739736702
0.030632037780734422
0.7672204143679429
0.824157291920133
0.95148659714096


for i in range(20):
    print(r.uniform(5.4, 5.5))

    
5.431181935720771
5.445677900103906
5.493086127493706
5.44685092447469
5.4964676583024135
5.437350846983588
5.472589931891966
5.473803233929777
5.456157499358682
5.401019141874697
5.457625798279085
5.490627933602405
5.40268355107501
5.479041230288391
5.405709948436671
5.412105441848424
5.444709118766601
5.43559029106967
5.40681717669296
5.405734036208267

for i in range(20):
    print(r.uniform(0, 1))

    
0.9299960242393523
0.13640582100493004
0.6411901623582505
0.8945879167805004
0.18907176818758265
0.4494316023682773
0.8162747442242162
0.8816745245256968
0.9412494473005697
0.7738693744751117
0.5629648785865968
0.8701532128586232
0.9486561986404051
0.2903819558364753
0.9892603296442313
0.03418092293207309
0.3606380316213409
0.806436198254329
0.898412746742014
0.1572884458141488



s1 = "Paata Mamporia"
s1
'Paata Mamporia'

r.choice(s1)
' '
r.choice(s1)
't'
r.choice(s1)
'a'
r.choice(s1)
'p'




= RESTART: D:/199/7_7/2023/simple_if_demo.py
Enter an integer: 4
Hi even!

= RESTART: D:/199/7_7/2023/simple_if_demo.py
Enter an integer: 15
Hi five!

= RESTART: D:/199/7_7/2023/simple_if_demo.py
Enter an integer: 30
Hi five!
Hi even!
>>> 
= RESTART: D:/199/7_7/2023/simple_if_demo.py
Enter an integer: 7
>>> 
= RESTART: D:/199/7_7/2023/simple_if_demo.py
Enter an integer: 7
Odd
>>> 
= RESTART: D:/199/7_7/2023/simple_if_demo.py
Enter an integer: 12
Even
>>> 
= RESTART: D:/199/7_7/2023/substraction_quiz.py
What is 8 - 7? 1
8 - 7 = 1 is True
>>> 
= RESTART: D:/199/7_7/2023/substraction_quiz.py
What is 6 - 4? 3
6 - 4 = 3 is False
6 - 4 = 2
>>> 
>>> 
