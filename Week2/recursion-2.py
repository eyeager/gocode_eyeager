
'''

Another example of recursion is binary recursion.  Binary recursion is when two recursive calls are made to the function (i.e. the function calls itself twice).  The fibonacci problem is a common problem that can be solved using binary recursion.

The Fibonacci numbers are the numbers of the following sequence of integer values: 

0,1,1,2,3,5,8,13,21,34,55,89, ... 

The Fibonacci numbers are defined by: 

Fn = Fn-1 + Fn-2 
with F0 = 0 and F1 = 1 

The Fibonacci sequence is named after the mathematician Leonardo of Pisa, who is better known as Fibonacci. In his book "Liber Abaci" (publishes 1202) he introduced the sequence as an exercise dealing with bunnies.

The Fibonacci numbers are easy to write as a Python function. It's more or less a one to one mapping from the mathematical definition:
'''
import time

# Solve this iteratively
def fib_iterate(limit):
	sum_num = 0
	i = 0
	fib_array = [0,1]

	while i < limit-2:
		sum_num = fib_array[i] + fib_array[i+1]
		fib_array.append(sum_num)
		i+=1
		
	return fib_array

start = time.time()
print fib_iterate(20)
end = time.time()
print "fib_iterate: ", end - start


# Solve this recursively
def build_fib_array(size):
	count = 0
	fib_array = []

	while count < size:
		fib_array.append(fib_recursive(count))
		count += 1

	return fib_array

def fib_recursive(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	return fib_recursive(num-1) + fib_recursive(num-2)


start = time.time()
print build_fib_array(20)
end = time.time()
print "build_fib_array: ", end - start

# Trace through the algorithm to understand it - using tree diagrams

# Tip: Step through the algorithm here:
# http://pythontutor.com/visualize.html#mode=display

# Bonus: Use timeit to see how long each algorithm takes: http://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python
