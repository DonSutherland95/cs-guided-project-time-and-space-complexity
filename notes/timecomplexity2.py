def foo(a):
	for elem in a:   # O(n) over length of a, n refers to the length of a
		print(elem)
​
foo([1,2,3,4])
foo([1,2,3,4,5,6,7,8])
​
​
def bar(a):
	print(a[7])  # O(1) over the length of a, "constant time"
​
bar([1,2,3,4])
bar([1,2,3,4,5,6,7,8])
​
​
def baz(a):
	for i in range(1000000000000):  # O(1) over the length of a
		print(a[0])
​
baz([1,2,3,4])
baz([1,2,3,4,5,6,7,8])
baz([1,2,3,4,5,6,7,8,9,10,11,12])
baz([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
​
​
def qux(n):
	for i in range(n // 2):   # O(n/2) == O(1/2 * n) == O(n)
		print(i)