Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=["apple","ant","banana"]
>>> b=["cherry","drought","ging"]
>>> a.extend(b)
>>> print(a)
['apple', 'ant', 'banana', 'cherry', 'drought', 'ging']
>>> a.remove("ging")
>>> print(a)
['apple', 'ant', 'banana', 'cherry', 'drought']
>>> a.append("orange")
>>> print(a)
['apple', 'ant', 'banana', 'cherry', 'drought', 'orange']
>>> a[1:3]=["cherry","bdhjeh"]
>>> print(a)
['apple', 'cherry', 'bdhjeh', 'cherry', 'drought', 'orange']
>>> a.insert(1,"ghd")
>>> print(a)
['apple', 'ghd', 'cherry', 'bdhjeh', 'cherry', 'drought', 'orange']
>>> a.remove("cherry")
>>> print(a)
['apple', 'ghd', 'bdhjeh', 'cherry', 'drought', 'orange']
>>> a.pop()
'orange'
>>> print(a)
['apple', 'ghd', 'bdhjeh', 'cherry', 'drought']
>>> a.pop(2)
'bdhjeh'
>>> print(a)
['apple', 'ghd', 'cherry', 'drought']
>>> a.clear()
>>> 
>>> #loop
>>> a=["apple","cherry","banbana","fun","going"]
>>> print(a)
['apple', 'cherry', 'banbana', 'fun', 'going']
>>> a.remove("cherry")
>>> print(a)
['apple', 'banbana', 'fun', 'going']
>>> for i in a:
	print(a)

	
['apple', 'banbana', 'fun', 'going']
['apple', 'banbana', 'fun', 'going']
['apple', 'banbana', 'fun', 'going']
['apple', 'banbana', 'fun', 'going']
>>> for i in range(len(a)):
	print(a[i])

	
apple
banbana
fun
going
>>> print(a)
['apple', 'banbana', 'fun', 'going']
>>> a=["apple","ant","banana"]
>>> newlist=[]
>>> for x in a:
	if "a" in a:
		newlist.append(a)
		print(newlist)

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=["apple","ant","banana"]
>>> a.sort()
>>> print(a)
['ant', 'apple', 'banana']
>>> x=[1,5,7,9,36,798,888]
>>> a.sort()
>>> print(a)
['ant', 'apple', 'banana']
>>> print(x)
[1, 5, 7, 9, 36, 798, 888]
>>> a.sort(remove=True)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.sort(remove=True)
TypeError: 'remove' is an invalid keyword argument for sort()
>>> a.sort(reverse=True)
>>> print(a)
['banana', 'apple', 'ant']
>>> z=a.copy()
>>> print(z?)
SyntaxError: invalid syntax
>>> print(z)
['banana', 'apple', 'ant']
>>> a=["apple","ant","banana"]
>>> b=["cherry","drought","ging"]
SyntaxError: multiple statements found while compiling a single statement
>>> c=a
>>> c=a+b
>>> print(c)
['banana', 'apple', 'ant', 'cherry', 'drought', 'ging']
>>> for x in c:
	print(c)

	
['banana', 'apple', 'ant', 'cherry', 'drought', 'ging']
['banana', 'apple', 'ant', 'cherry', 'drought', 'ging']
['banana', 'apple', 'ant', 'cherry', 'drought', 'ging']
['banana', 'apple', 'ant', 'cherry', 'drought', 'ging']
['banana', 'apple', 'ant', 'cherry', 'drought', 'ging']
['banana', 'apple', 'ant', 'cherry', 'drought', 'ging']
>>> for x in b:
	list.append(x)
	print(a)

	
Traceback (most recent call last):
  File "<pyshell#77>", line 2, in <module>
    list.append(x)
TypeError: descriptor 'append' requires a 'list' object but received a 'str'
>>> print(c)
['banana', 'apple', 'ant', 'cherry', 'drought', 'ging']
>>> a.extend(b)
>>> print(aa)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    print(aa)
NameError: name 'aa' is not defined
>>> print(a)
['banana', 'apple', 'ant', 'cherry', 'drought', 'ging']
>>> 
