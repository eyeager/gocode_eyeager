'''

Python has a builtin string class to help with common string operations. A string in python is basically a list of characters, with helper methods. Strings do share some commonality with Python lists, which we will cover later.

'''

#create a new string
r = ""

assert r == ""

#use len() to find the length of a string
a = "String"
r = len(a)
assert r == 6

#put these two string together
a = "Hello "
b = "World"
r = a + b

assert r == "Hello World"


#use * to create five fives
a = "5"
r = a + a + a + a + a

assert r == "55555"

#TODO
#get the first letter of a string
a = "1234"
r = a[0]

assert r == "1"

#remove the first character of a string

a = "!Good"
r = a[1:5]

assert r == "Good"

#remove the last character of a string

a = "Good!"
r = a[0:4]

assert r == "Good"

#remove a word from a string

a = "Hello [name]"
r = a.rstrip("[name]")

assert r == "Hello "

#change "[name]" to "Bob"

a = "Hello [name]"
r = a.replace("[name]","Bob")

assert r == "Hello Bob"

#convert the string "5" to 5

a = "5"
r = int(a)


assert r == 5

#create a string from a and b
a = "Price = "
b = 5.99
r = a + str(b)
assert r == "Price = 5.99"

#convert the string "5.99" to 5.99

a = "5.99"
r = float(a)
assert r == 5.99

#use .format() a string using the string format method

a = '{0}, {1}, {2}'
r = a.format('a','b','c')
assert r == 'a, b, c'

#use .rstrip() to remove \n from the string

a = "This is a string with a new line character\n"
r = a.rstrip('\n')

assert r == "This is a string with a new line character"

#use .find() to locate the index or where the substring "string" starts in a

a = "Python's string methods are very powerful"
r = a.find("string")
assert r == 9

#use .upper() to uppercase

a = "this is a lower case string"
r = a.upper()

assert r == 'THIS IS A LOWER CASE STRING'

#use .lower() to lower

a = "THIS IS AN UPPER CASE STRING"
r = a.lower()

assert r == 'this is an upper case string'

#use .replace() to search and replace "is" with "was"

a = "This is a simple string"
r = a.replace("is","was")

assert r == 'Thwas was a simple string'


