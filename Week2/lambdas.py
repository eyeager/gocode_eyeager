 
'''

Lambdas are functions that you can create on the fly, also referred to as anonymous functions, because they lack a name.

The concept comes from functional programming languages like LISP. Python has incorprated some of these concepts into the language.

Lambda functions are mainly used in combination with the functions filter(), map() and reduce().

In many interview settings, you will be presented with a new function/concept and be asked to use it in your program.

'''

import math


def square_root1(x):
    return math.sqrt(x)

square_root2 = lambda x: math.sqrt(x)


#create an anonymous function and assign to a variable called one_up
#this function should add one to its argument

one_up = lambda x:x+1

assert type(lambda x:x) == type(one_up)

assert one_up(1) == 2


#create an anonymous function and assign to a variable my_add
#this function will take two arguments and add them together

my_add = lambda x,y: x + y

assert type(lambda x:x) == type(my_add)

assert my_add(1,2) == 3


#use a list comprehension plus one_up to tranform a into r where each element is one_up'ed

a = [1,2,3]
r = [x+1 for x in a]

assert r == [2, 3, 4]


#now can you use map() to do the same thing but in one line

a = [1,2,3]
r = map(one_up,a)

assert r == [2, 3, 4]


# The function filter(function, list) offers an elegant way to filter out all the elements of a list, for which the function function returns True. 

# The function filter(f,l) needs a function f as its first argument. f returns a Boolean value, i.e. either True or False. This function will be applied to every element of the list l. Only if f returns True will the element of the list be included in the result list.

#use filter() to filter out even numbers from a

a = range(0,10)
r = filter(lambda x: x%2 != 0,a)

assert r == [1, 3, 5, 7, 9]

# The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value. 
#use reduce() to sum a

a = [1, 3, 5, 7, 9]
r = reduce(lambda x,y: x+y,a)

assert r == 25

#use reduce to find the largest number in a

a = [1, 3, 5, 7, 9]
r = reduce(lambda x,y: max(x,y), a)

assert r == 9


# The advantage of the lambda operator can be seen when it is used in combination with the map() function. 
# map() is a function with two arguments:

# r = map(func, seq)

# The first argument func is the name of a function and the second a sequence (e.g. a list) seq. map() applies the function func to all the elements of the sequence seq. It returns a new list with the elements changed by func

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]

# add values for each index for all three arrays (a + b + c) using map() and lambdas

r = map(lambda x,y,z: x+y+z, a,b,c)

assert r == [17, 10, 19, 23]

# add a + b and subtract c using map() and lambdas
r = map(lambda x,y,z: x + y - z, a,b,c)

assert r == [19, 18, 9, 5]









