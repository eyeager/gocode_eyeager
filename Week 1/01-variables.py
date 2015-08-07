""" 
    GoCode

    Variables are used to store pieces of data.

    You can assign values to an arbitrary name. Variable naming is important. It helps not only you but other developers understand the function of a variable in code.

    A variable stores some value. That value has a type. Basic types in Python are an integer, float, string and a bool. 

    Why do we have types? It is so that Python can understand how to operate on the data, ultimately making it easier for the developer. 

    If I ask Python to execute this line 8 + 3, it knows that 8 and 3 are integers (by the lack of quotes) it can apply the mathmatical add operation to them.

    If I ask Python to execute this line "Hello " + "World" by the fact of the quote character " Python knows that those are strings. So it combines both strings to create "Hello World"

    If you need additional challenges, go here:
    http://www.coderbyte.com/CodingArea/Challenges/
"""

#Before we get started on variables a quick note on commenting.
#(anythig in this line is ignored by Python, only for humans)
#Code is created for two audiences. The first is a computer to run the instructions, but secondly people. People need to be able to work on code. So a comment (in python the # character),
#tells the interpreter to ignore a line.
#That way we can leave a comment or note to ourselves in the future or for future developers. Now as you can see typing # every time can be annoying if we have several lines of comments.
#Python and many languages have the concept of a multi-line comment. To create a multi-line comment use """ to start and """ to end
#just like the top of this file

""" 

Multi-line
Comment
(We could write anything here, for as many lines as we want, ignored completely by Python)

*** Important ***

How these files are laid out.

Below are a set of exercises. Python has a builtin method called assert. Assert checks to see if some condition is true (we will cover this later), if the condition is not true it throws
an exception, basically everything blows up. The goal is to update the code until it no longer blows up after running.

Correct the program by adding a line or two of code prior to the assert. Do not change the assert line.

Run:

python 01-variables.py

"""

#create and set a variable named result to the number 3
result = 3
assert result == 3

#set result to the string "What's up"
result = "What's up"
assert result == "What's up"

#set result to the floating point number 2.99

result = 2.99
assert result == 2.99

#set result to the boolen value True

result = True
assert result == True

#set result to the boolean value False

result = False
assert result == False

#set result to None

result = None
assert result == None

#set result to any interger value. Note the type function returns the data type of a variable.

result = 2
assert type(result) is int

#set result to any float value
result = 3.14
assert type(result) is float

#set result to any string value
result = "I'm a string"
assert type(result) is str

#set result to any boolean value

result = False
assert type(result) is bool 

print "Good Job!"

