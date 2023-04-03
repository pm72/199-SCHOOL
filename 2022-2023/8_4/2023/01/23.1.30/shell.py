Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: D:/199/8_4/2023/addition_quiz.py ==================
What is 1 + 3? 4

=== RESTART: D:/199/8_4/2023/addition_quiz.py ===
What is 6 + 1? 7
6 + 1 = 7 is True

=== RESTART: D:/199/8_4/2023/addition_quiz.py ===
What is 2 + 10? 18
2 + 10 = 18 is False

=== RESTART: D:/199/8_4/2023/addition_quiz.py ===
What is 3 + 3? 12
3 + 3 = 12 is False
3 + 3 = 6


import random as r

r.random()
0.11829265304890135
r.random()
0.758523966272433
r.random()
0.15598353709245916


r.uniform(5.5, 5.6)
5.5461098448875825
r.uniform(5.5, 5.6)
5.5778111786547155


for i in range(20):
    print(r.uniform(5.5, 5.55))

    
5.500306677620865
5.525796106274885
5.546840556316638
5.5378065411990836
5.519393589909429
5.529328093534344
5.515745728812014
5.5429551400686075
5.541452895559477
5.515486729636571
5.537766381598482
5.515998508476033
5.517460592015233
5.548860349641029
5.531865799042792
5.544295317773005
5.513277317007584
5.535888676223725
5.502910854187598
5.536416563871256


numbs = [15, 25, 62, 3, -48, 1, 0, 55, 21]
r.choice(numbs)
55
r.choice(numbs)
25
r.choice(numbs)
15


names = ['Paata', 'Tedo', 'Nana', 'Levani', 'eka', 'lika', 'Manana']

r.choice(names)
'Levani'
r.choice(names)
'Levani'
r.choice(names)
'lika'
r.choice(names)
'Levani'
r.choice(names)
'eka'


name = "Paata Mamporia"
r.choice(name)
'a'
r.choice(name)
't'
r.choice(name)
'M'

name1 = ""
for i in range(len(name)):
    name1.append(r.choice(name))

    
Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    name1.append(r.choice(name))
AttributeError: 'str' object has no attribute 'append'
for i in range(len(name)):
    name1 += r.choice(name)

    
nameq
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    nameq
NameError: name 'nameq' is not defined. Did you mean: 'names'?
name1
'aaarraPmi MMap'

== RESTART: D:/199/8_4/2023/simple)_if_demo.py ==
Enter an integer: 14
Hi even!

== RESTART: D:/199/8_4/2023/simple)_if_demo.py ==
Enter an integer: 20
Hi five!
Hi even!
>>> 
== RESTART: D:/199/8_4/2023/simple)_if_demo.py ==
Enter an integer: 11
>>> 
== RESTART: D:/199/8_4/2023/subtraction_quiz.py =
What is 3 - 0? 0
3 - 0 = 0 is False
3 - 0 = 3
>>> 
== RESTART: D:/199/8_4/2023/subtraction_quiz.py =
What is 6 - 0? 6
6 - 0 = 6 is True
>>> 
== RESTART: D:/199/8_4/2023/subtraction_quiz.py =
What is 5 - 5? 0
5 - 5 = 0 is True
>>> 
== RESTART: D:/199/8_4/2023/subtraction_quiz.py =
What is 9 - 8? 1
9 - 8 = 1 is True
>>> 
== RESTART: D:/199/8_4/2023/subtraction_quiz.py =
What is 3 - 0? 2
3 - 0 = 2 is False
3 - 0 = 3
