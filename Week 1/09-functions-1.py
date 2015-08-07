'''

Functions are a way of grouping code together. This allows the programmer to break code into easy to use chunks, that can be called over and over again. 

Here are the key things to learn:

1) A function can take in some data, called arguments or parameters.

2) Functions can return values that can then be assigned to variables or evaluated.

3) The "return" keyword will return a value from a function.

Hint: Using the "pass" keyword, you can create empty functions that does nothing.

'''

#create a function called my_func that does nothing
def my_func():
	pass

#create a function with one argument that does nothing
def my_func_2(a):
	pass

#create a function with two arguments that does nothing
def my_func_3(a,b):
	pass

#create a function that returns the string "my return value"
def func_return():
	return "my return value"

assert "my return value" == func_return()

#create a func that returns the integer 5
def func_return_int():
	return 5

assert 5 == func_return_int()


#create a func that takes in two arguments and adds them up
def func_return_add(a,b):
	return a + b

assert 9 == func_return_add(5,4)

#create a function that returns True
def func_return_bool():
	return True

assert func_return_bool()

#create a function that takes in a number and does a conversion from celsius to farenheit 
def celsuis_to_farenheit(cel):
	far = (cel * (9.0/5.0)) +32
	return far