'''

Math operations in Python. Python has standard basic math operations built-in. There is a new data type introduced in this section. The float. Floating point numbers are used to store
numbers that have a decimal point. The reason they are split into int and float is that for the computer storing and preforming operations on floats is harder than storing and manipulating integers.

In some cases you may need to convert between the two. Also Python will automatically convert ints to float if they are in an expression with a float.

Assign the proper result to the variable r. 

'''

#add these two numbers together

a = 5
b = 6
r = a + b

assert r == 11

#add these numbers
a = 5.01
b = 6.02
r = a + b

assert r == 11.03

#add these numbers

a = 5
b = 2.01
r = a + b

assert r == 7.01
assert type(r) is float

#subtract these two numbers

a = 15
b = 5
r = a - b

assert r == 10

#subtract these two numbers
a = 5.25
b = 1
r = a - b

assert r == 4.25

#multiply these numbers

a = 7
b = 8
r = a * b

assert r == 56

#divide these numbers

a = 49
b = 7
r = a / b

assert r == 7

#divide these numbers

a = 57
b = 7
r = (a / b) - 1

assert r == 7

#divide these numbers

a = 5.0
b = 2
r = a / b

assert r == 2.5

#use round() to round a
#

a = 2.644
r = round(a)

assert r == 3.0

#exponent a to the power of b using the ** operator

a = 2
b = 4
r = a ** b

assert r == 16


#Use the modulo operator % with a,b to obtain r

a = 17
b = 4
r = a % b

assert r == 1

#even: Create an expression that evalutes a to see if it is even and assigns it to the variable r

a = 2
if a % 2 == 0:
	r = True


assert r == True

#even 2

a = 3
if a % 2 == 0:
	r = True
elif a % 2 != 0:
	r = False
assert r == False


#odd

a = 3
if a % 2 == 0:
	r = False
elif a % 2 != 0:
	r = True
assert r == True

#odd 2

a = 2
if a % 2 == 0:
	r = False
elif a % 2 != 0:
	r = True
assert r == False


#calculate 5 times 2 plus 7

r = 0
r = 5 * 2 + 7

assert r == 17

#calculate 2 plus 7 times 5

r = 0
r = 2 + 7 * 5
assert r == 37

#add parenthesis to get the correct output

r = (3 + 7) * 5
assert r == 50

#convert float to int

a = 1.01
r = int(a)
assert r == 1
assert type(r) is int

#convert int to float

a = 1
r = float(a)
assert r == 1.0
assert type(r) is float

#change a and b to get the assert to work

a = 5
b = 6

assert a < b

#change a and b to get the assert to work

a = 5
b = 4

assert a > b

#create an expression using < operator and assign the result to r

a = 1
b = 5
r = a < b

assert r == True

#use the not operator to make r pass
r = False
a = False
r = not(a)
assert r == True

#use the or operator to make r pass
r = False

a = True
b = False
r = a or b
assert r == True

#use the and operator to make r pass
r = False

a = True
b = True
r = a & b

assert r == True

#TODO
#floor

#TODO
#ceiling 
