'''
Binary Search in English:
1) Sort the list.

2) Let i = length / 2

3) Compare term at index i to your key.

a. If they are equal, return the index.

b. If key is greater than this term, repeat 3 (recurse) on upper half of list i = (i + length) / 2 (or (i + top) / 2 depending how you implement)

c. If key is less than this term, repeat 3 on lower half i = i/2 or (i + bottom)/2

4) Stop recursion if/when the new i is the same as the old i. This means you've exhausted the search. Return -1

Tips: Be careful for off-by-one errors, which can make you exclude certain terms by mistake, or cause infinite recursion, but this is the general idea. Pretty straightforward.

Think of it as playing 'Guess the number' for the numbers 1 through 100. 

You take a guess, I tell you higher or lower. 
You say 50, I say lower. 
You say 25, I say higher. 
You say 37, etc...

Additional reading for Big-O notation:

http://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/
https://justin.abrah.ms/computer-science/big-o-notation-explained.html
'''

#Write a binary search algorithm
import timeit


def binary_search_recursion(value,data):
	i = (len(data)/2)

	if value == data[i]:
		return True
	elif i < 1:
		return False
	elif value < data[i]:
		return binary_search_recursion(value, data[:i])
	elif value > data[i]:
		return binary_search_recursion(value, data[i:])

start = timeit.timeit()
assert binary_search_recursion(3,[1,2,3]) == True
end = timeit.timeit()
print "For binary_search recursive: ", end - start

start = timeit.timeit()
assert binary_search_recursion(500,range(0,400)) == False
end = timeit.timeit()
print "For binary_search recursive: ", end - start


def binary_search(value,data):
	i = len(data)
	search_flag = False

	while i > 0 and search_flag == False:
		i = i/2

		if value == data[i]:
			search_flag = True
		elif value < data[i]:
			data = data[:i+1]
		elif value > data[i]:
			data = data[i:]


	return search_flag

assert binary_search(4,[1,2,3,4]) == True

# Bonus: Write a binary search algorithm recursively - DONE

# Bonus: Compare the performance of the two algorithms and for different arrays with different lengths using timeit.
