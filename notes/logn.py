def search(name, lst):
	for elem in lst:   # O(n) over the length of lst
		if name == elem:  # O(m) over the lengths of the compared strings, O(1) over the length of lst
			return True
​
	return False
​
"""
O(n) over the length of the lst
O(n*m) where n is the length of the list, and m is the length of the strings in the list
"""
​
"""
Binary search
​
When you cut the space in half, hints that it's O(log(n))
​
100000
50000
25000
12500
6250
3125
1563
782
391
195
97
48
24
12
6
3
1
​
100000 names, 16 comparisons
"""