# Time and Space Complexity
​
# What is Big O: it's a way to measure how well an algorithm scales.
​
def foo(n):
	for i in range(n):
		print(i)
​
foo(10)   # 10 prints, if this takes a certain amount of time
foo(20)   # 20 prints, how much more time does this take?      TWICE as long
foo(10000)  # 10000 prints
​
"""
foo(n)   n prints
​
O(n)  "Order n"  "linear"
"""
​
def bar(n):
	for i in range(n);
		for j in range(n):
			print(i, j)
​
bar(10)  # 100 prints
bar(20)  # 400 prints
bar(10000)  # 100,000,000 prints
​
"""
bar(n)   n^2 prints
​
O(n^2)
"""

