
'''

Goal: Write a program that splits a large file into two files based on line number.

First using .open() and write(), create a sample file that has 1000 lines of data in it. Each line contains the line number of that line.

e.g.

1
2
3
4
5
6
...

Then create a function that takes the file name, and a line number as arguments.  This function will split the file at that line number.  This function will create two new files with the orignal file name plus -1 or -2 appended to it. (e.g. filename-1.txt, filename-2.txt)

The filename-1.txt will have all the line numbers up to the number given.

The filename-2.txt will have all the line numbers > than the number given.

'''

f = open("number_file.txt","w")
for i in range(1,1001):
	f.write(str(i) + "\n")
f.close()

# Here are some empty functions that are shown here as examples.  You do NOT have to use these if you don't want to.  You can create your own functions instead. It might be simpler to ignore the examples and to create your own logic rather than trying to use these.
'''
def read_data(filename):
    pass
'''

'''
def write_data(filename,data):
    pass
'''
def split_file(filename,line_number):
	original = open(filename, "r")
	file_1 = "".join((filename.strip(".txt"), "_1", ".txt"))
	file_2 = "".join((filename.strip(".txt"), "_2", ".txt"))
	i = 1

	while i <= 1000:
		if i <= line_number:
			with open(file_1, "a") as file:
				file.write(original.readline())
		elif i > line_number:
			with open(file_2, "a") as file:
				file.write(original.readline())
		i += 1
	
	original.close()

split_file("number_file.txt",500)




