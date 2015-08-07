
'''

Using what you've learned about defining classes, create a new class 
called StringHandler that will:

1) Take in a string on initialization

sh = StringHandler("stringgggg")

It has one instance variable - string

2) Has four methods:

i) Method that writes appends a new string to the original string instance variable

sh.append_string(new_string)

ii) Method that appends "this is a uselss method" to the original string instance variable

sh.append_useless_string()

iii) Slices original string based on index that is passed in.
The method prints the first half of the string.
The second half of the string gets stored as the instance variable

sh.slice_string(index)


'''


class StringHandler:
	def __init__(self, string):
		self.string = string

	def append_string(self, new_string):
		self.string += " " + new_string

	def append_useless_string(self):
		self.string += " this is a useless method"

	def slice_string(self, slice_index):
		print self.string[:slice_index]
		self.string = self.string[slice_index:]

some_string = StringHandler("I'm a string")
some_string.append_string("some more string")
some_string.append_useless_string()
some_string.slice_string(10)
print some_string.string
