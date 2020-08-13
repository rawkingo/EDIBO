Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> int
<class 'int'>
>>> a
10
>>> 10 == int
False
>>> type(a) == int
True
>>> int(0)
0
>>> int(24)
24
>>> int(False)
0
>>> a=10
>>> if type(a) ==int:
	print("labi")
else:
	print("slikti")

	
labi
>>> a="10"
>>> 
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
slikti
>>> a=5.5
>>> type(a)
<class 'float'>
>>> if type(a) == int:
print("labi")
SyntaxError: expected an indented block
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
        print("ari labi")
else:
	print("slikti")

	
ari labi
>>> a=10
>>> f type(a) == int:
	print("labi")
else:
	print("slikti")
	
SyntaxError: invalid syntax
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
        print("ari labi")
else:
	print("slikti")

	
labi
>>> print ("aaa bbb ccc")
aaa bbb ccc
>>> print ("aaa \n bbb \n ccc")
aaa 
 bbb 
 ccc
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> petter = fruit[4]
>>> print(petter)
n
>>> fruit = "carlson"
>>> fruit(len)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    fruit(len)
TypeError: 'str' object is not callable
>>> len(fruit)
7
>>> fruit
'carlson'
>>> type(carlson)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    type(carlson)
NameError: name 'carlson' is not defined
>>> type(fruit)
<class 'str'>
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
c
a
r
l
s
o
n
>>> while index > len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
>>> index = 7
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> while index > len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
>>> while index > len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> index = 6
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
n
>>> while index <len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> while index > len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> 
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index+6]
	print(letter)
	index = index + 1

	
n
Traceback (most recent call last):
  File "<pyshell#77>", line 2, in <module>
    letter = fruit[index+6]
IndexError: string index out of range
>>> while index < len(fruit):
	letter = fruit[index+5]
	print(letter)
	index = index + 1

	
n
Traceback (most recent call last):
  File "<pyshell#79>", line 2, in <module>
    letter = fruit[index+5]
IndexError: string index out of range
>>> while index < len(fruit):
	letter = fruit[index+6]
	print(letter)
	index = index - 1

	
Traceback (most recent call last):
  File "<pyshell#81>", line 2, in <module>
    letter = fruit[index+6]
IndexError: string index out of range
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#83>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> while index > len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

>>> 
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
Traceback (most recent call last):
  File "<pyshell#87>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> while index < len(fruit):
	letter = fruit[index+1]
	print(letter)
	index = index - 1

	
c
Traceback (most recent call last):
  File "<pyshell#89>", line 2, in <module>
    letter = fruit[index+1]
IndexError: string index out of range
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 2

	
Traceback (most recent call last):
  File "<pyshell#91>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
Traceback (most recent call last):
  File "<pyshell#93>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1while index < len(fruit):
		letter = fruit[index]
		print(letter)
		index = index - 1
		
SyntaxError: invalid syntax
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
Traceback (most recent call last):
  File "<pyshell#96>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
Traceback (most recent call last):
  File "<pyshell#98>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index = 7
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> index = 6
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#104>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index = 5
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
o
s
l
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#107>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
Traceback (most recent call last):
  File "<pyshell#109>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#112>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index
-8
>>> index = 1
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#116>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index
-8
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
c
a
r
l
s
o
n
>>> index
7
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#124>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index
-8
>>> fruit
'carlson'
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
Traceback (most recent call last):
  File "<pyshell#128>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#131>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
Traceback (most recent call last):
  File "<pyshell#133>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index
-7
>>> index = 0
>>> while index > len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
>>> while index >len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index + 1

	
>>> 
>>> index
0
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 7

	
n
Traceback (most recent call last):
  File "<pyshell#143>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
Traceback (most recent call last):
  File "<pyshell#145>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index
-7
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#149>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index
-7
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#153>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index = 0
>>> letter = fruit[index-1]
>>> letter
'n'
>>> index
0
>>> int(letteR)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    int(letteR)
NameError: name 'letteR' is not defined
>>> 
>>>  int(letter)
SyntaxError: unexpected indent
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#162>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index
-7
>>> index 7
SyntaxError: invalid syntax
>>> index = 7
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
>>> index = 6
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
o
s
l
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#170>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index
-7
>>> index = 0
>>> letter = fruit[-7]
>>> letter
'c'
>>> letter = fruit[0]
>>> letter
'c'
>>> letter = fruit[-14]
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    letter = fruit[-14]
IndexError: string index out of range
>>> letter = fruit[8]
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    letter = fruit[8]
IndexError: string index out of range
>>> index
0
>>> while index > len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
>>> index =
SyntaxError: invalid syntax
>>> index
0
>>> index = -7
>>> while index > len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
>>> while index > len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index + 1

	
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
c
Traceback (most recent call last):
  File "<pyshell#190>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index
-8
>>> index = -7
>>> while index > len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
>>> index
-7
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#198>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index
-7
>>> index = 0
>>> index = 6
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#203>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index
-8
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#207>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index = -6
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
c
Traceback (most recent call last):
  File "<pyshell#210>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index
-7
>>> index = -6
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index + 1

	
c
a
r
l
s
o
n
c
a
r
l
s
o
>>> o
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    o
NameError: name 'o' is not defined
>>> index
7
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#219>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index = 0
>>> len(fruit)
7
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)

	
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c

c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
cTraceback (most recent call last):
  File "<pyshell#222>", line 3, in <module>
    print(letter)
KeyboardInterrupt
>>> while index < len(fruit):
	letter = fruit[index-7]
	print(letter)
	index = index + 1

	
c
a
r
l
s
o
n
>>> index
7
i
>>> index
7
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index+7]
	print(letter)
	index = index - 1

	
Traceback (most recent call last):
  File "<pyshell#229>", line 2, in <module>
    letter = fruit[index+7]
IndexError: string index out of range
>>> index
0
>>> while index < len(fruit):
	letter = fruit[index+7]
	print(letter)
	index = index + 1

	
Traceback (most recent call last):
  File "<pyshell#232>", line 2, in <module>
    letter = fruit[index+7]
IndexError: string index out of range
>>> index
0
>>> while index < len(fruit):
	letter = fruit[index+6]
	print(letter)
	index = index + 1

	
n
Traceback (most recent call last):
  File "<pyshell#235>", line 2, in <module>
    letter = fruit[index+6]
IndexError: string index out of range
>>> index
1
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index+6]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#239>", line 2, in <module>
    letter = fruit[index+6]
IndexError: string index out of range
>>> index
-14
>>> index = 0
>>> while index > len(fruit):
	letter = fruit[index+6]
	print(letter)
	index = index - 1

	
>>> index
0
>>> index = 12
>>> while index > len(fruit):
	letter = fruit[index+6]
	print(letter)
	index = index - 1

	
Traceback (most recent call last):
  File "<pyshell#247>", line 2, in <module>
    letter = fruit[index+6]
IndexError: string index out of range
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#250>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index = 0
>>> letter = fruit[-1]
>>> letter
'n'
>>> letter = fruit[-2]
>>> letter
'o'
>>> index
0
>>> while index < len(fruit)-1:
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#258>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index = 0
>>> while index < len(fruit)-1:
	letter = fruit[index]
	print(letter)
	index = index - 1

	
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#261>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index = 6
>>> fruit
'carlson'
>>> fruit[6]
'n'
>>> fruit[index]
'n'
>>> while index <- len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> index
6
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#270>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#273>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index = 0
>>> letter = fruit[index+6]
>>> fruit
'carlson'
>>> letter = fruit[index-1]
>>> fruit
'carlson'
>>> letter
'n'
>>> letter = fruit[index+6]
>>> letter
'n'
>>> while index < len(fruit):
	letter = fruit[index+6]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#283>", line 2, in <module>
    letter = fruit[index+6]
IndexError: string index out of range
>>> index
-14
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#287>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#290>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index = -1
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#293>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index = 0
>>> while index < len(fruit)-1:
	letter = fruit[index]
	print(letter)
	index = index - 1

	
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#296>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index
-8
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index+6]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#300>", line 2, in <module>
    letter = fruit[index+6]
IndexError: string index out of range
>>> index = 6
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#303>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index
-8
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#307>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index
-7
>>> index = 0
>>> while index < len(fruit)-1:
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#311>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index
-7
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index+6]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#315>", line 2, in <module>
    letter = fruit[index+6]
IndexError: string index out of range
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
Traceback (most recent call last):
  File "<pyshell#317>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#320>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index = 6
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#323>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index
-8
>>> index = 6
>>> while index <= len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#327>", line 2, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> index = 0
>>> while index <=len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1

	
n
o
s
l
r
a
c
Traceback (most recent call last):
  File "<pyshell#330>", line 2, in <module>
    letter = fruit[index-1]
IndexError: string index out of range
>>> index
-7
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index-1]
	print(letter)
	index = index - 1
