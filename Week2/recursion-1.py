'''

A recursive function is one that calls itself. Using this technique can make it easier and cleaner to solve certain problems.


The most common example is writing a function to compute factorials

4! = 4 * 3 * 2 * 1 

This is an example of linear recursion.  Recursion is a method in programming where a function calls itself one or more times in its body.

Linear recursion solutions often contain a base case.

A base case is the first/most basic case in the problem.  

E.g. In computing factorials, the base case is computing the factorial of 1.  The program should return 1.  Base cases allow the recursive solution to avoid ending up in an infinite loop.

Example: 

4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1 

Replacing the calculated values gives us the following expression 

4! = 4 * 3 * 2 * 1

'''


#iterative version - meaning using standard looping constructs - write a function that takes n and returns factorial


#recursive version - write a function that takes n and returns factorial - don't forget the base case!

#trace through the algorithm to understand it

#add print statements where appropriate so you can debug it easily

# Bonus: Use timeit to see how long each algorithm takes: http://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python

# Using a for loop, sum the values in a

import timeit

start = timeit.timeit()

total = 0
a = [1,2,7,9]

for number in a:
	total += number

end = timeit.timeit()
print "For loop sum: ", end - start

assert total == sum(a)


#Now write a recursive function that takes a list and returns the sum of that list

#Trace through the algorithm to understand it

#Add print statements where appropriate so you can debug it easily

start = timeit.timeit()
b = [2,47,8,10]

def recursive_sum(vals):
	if len(vals) == 1:
		return vals[0]
	return vals[0] + sum(vals[1:])
end = timeit.timeit()
print "Recursive sum: ", end - start

assert recursive_sum(b) == sum(b)

# Bonus: Use timeit to see how long each algorithm takes: http://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python
