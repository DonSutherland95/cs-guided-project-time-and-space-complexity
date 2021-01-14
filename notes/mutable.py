def foo(x):   # x = a
	x = x + 10
	return
​
a = 20
​
foo(a)
​
print(a)  # 20 because x pointed to a different immutable object (30)
​
​
def foo(x):   # x = a
	x[1] = 99
	return
​
a = [1,2,3]
​
foo(a)
​
print(a[1])  # 99 because x and a point to the same mutable object (the list)
​
"""
Mutable objects are:
​
	Lists
	Dictionaries
	Sets
	User-defined Classes
​
Bonus info:
​
Re a='hello', b='hello' pointing to same object
​
Certain objects only have 1 copy in memory.
These are "interred" objects.
​
They are:
​
* integers between -6 and 256 inclusive
​
* Any strings consisting of only alphabetic chars or underscores
​
* And None
​
You don't need to know this to be an effective
Python programmer. :)
​
"""