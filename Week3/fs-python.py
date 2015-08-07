'''

Create a File System and simple terminal emulator.


A filesystem has a root, and on a unix based system the root is /

Thre can then be directories and files underneath each path.

/
users/
     steve/
          budget.csv
     racheal/
          books.txt
lib/
   shared/
         man.so


Mimic an fs using basic Python data structures.

Then allow a user through a simple input

ls
pwd
cd .. or cd <name>

Bonus: 

Create a directory.
Allow commands to work with ../../<name>

'''

from filesystem import FileSystem

def ui_loop():
	fs = FileSystem()

	print "****Welcome to the terminal emulator****"
	user_command = ""

	while user_command != "quit" or user_command != "exit":
		user_command = raw_input ("$ ")
		# Separate first word from rest of command
		user_command = user_command.split(" ",1)
		fs.run_command(user_command)

ui_loop()