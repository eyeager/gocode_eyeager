'''

Working with files is a very common task in programming. Many times you will get data in a weird format and have to process it to incorparate it into your application. 

When with working with files you can tell Python and the operating system how you intend to work with the file (read a file or write or append or combinations of these).

'''

#change 'f = None' below.  use open() to with the 'w' argument to create a file called 'blah.txt'

f = open("blah.txt","w")

#note you should always .close() on a file if you use the "w" argument
f.close()

#Here is an example of how to open a file using "r" and closing it afterwards.
f = open("blah.txt", "r")
f.close()

#It can be easy to forget to close a file. Especially in a large amount of code. Forgetting is bad because the operating system may not flush the data to disk (i.e. the system will stall). The operating system tries to optimize disk writing and will sometimes wait until it thinks you are done.

#Python has a better way to interact with files, it is called "with".  Here is an example of how to use the "with" function.

with open("blah.txt", "r") as f:
    print "We now can use f"
    f.read(1)
    print "After this line with will automactically call close on f"

#use with and .write() to write "*Test Data*" to blah.txt
with open("blah.txt","w") as f:
	f.write('*Test Data*')

#use with and .readline() to read from blah.txt
with open("blah.txt","r") as f:
	r = f.readline()

assert r == "*Test Data*"

#use the "a" flag, write some more data to blah.txt. The "a" says lets append data to this file! Check your file afterwards to make sure it appended what you wrote.
with open("blah.txt","a") as f:
	f.write('\nsomething new\n')

#Google Research: What is the difference between "w" and "w+" flags?


