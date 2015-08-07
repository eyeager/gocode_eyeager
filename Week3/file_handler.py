
'''

Using what you've learned about defining classes, create a new class 
called FileHandler that will:

1) Take in a filename on initialization

fh = FileHandler("filename.txt")

It has two instance variables - filename and filedata

2) Parse the file using readlines and store it in an instance variable called filedata

You might want to create your own dummy text file to test this.

3) Has three methods:

i) A method that writes data to file

fh.write_new_data(data_in_array_format)

ii) A method that splits current file based on line_number passed into it.  

The first part of the file gets stored in the original filedata/filename.

The second part of the file is returned in an array of strings format.

fh.splitfile(line_number)

iii) A method that prints out the current file data into console

fh.__print

The reason why we call it '__print()' as opposed to 'print()' is because of Python conventions.

Python engineers often add '__' in front of a method name to make it 'private'.  

The name scrambling is used to ensure that subclasses don't accidentally override the attributes of their superclasses. 

In this case, we don't want to override or conflict with the print() method.

You can reference code from exercise 10-file-io-1.

'''

class FileHandler:
	def __init__(self, filename):
	    self.filename = filename
	    self.__print()

	def refresh_filedata(self):
		with open(self.filename) as file_open:
			self.filedata = file_open.readlines()
		return self.filedata

	# Writes data to the file
	def write_new_data(self, data_array):
		self.filedata.append((" ".join(data_array) + "\n"))
		with open(self.filename,"w") as file_open:
			file_open.writelines("".join(self.filedata))

	# Splits the file based on a line number passed in
	# First part is stored in filedata/name. Second part is stored in a returned array of strings.
	def split_file(self, line_split):
		array_remainder = self.filedata[line_split:]
		self.filedata = self.filedata[0:line_split]
		self.write_new_data("")
		self.__print
		return array_remainder

	def __print(self):
		print "Filename %s current content:\n%s" % (self.filename, "".join(self.refresh_filedata()))

fh = FileHandler('filename.txt')
fh.write_new_data(["test","testdata"])
fh.split_file(10)


# Bonus: Write an additional method:
# 1) A method that takes in a new file and appends the data to the stored file and saves it




