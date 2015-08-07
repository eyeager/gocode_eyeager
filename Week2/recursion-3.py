'''

Recursively walk a filesystem.

'''

import os

# write a function that takes in dirname and prints all the directories and files as well as prints subdirectories and files in all subdirectories. use recursion.

def print_all_contents(dirname):
	for content in os.listdir(dirname):
		full_path = os.path.join(diranme, content)
		if os.path.isdir(full_path) == True:
			print_all_contents(full_path)
		else:
			print full_path

print_all_contents(".")

#Trace through the algorithm to understand it
#Add print statements where appropriate so you can debug it easily

#Bonus: Create a directory with a bunch of sub-folders. Recursively delete all of them.  Make sure you don't do this on anything you need...

def delete_all_contents(dirname):	
	# Deletes all files
	for content in os.listdir(dirname):
		full_path = os.path.join(dirname, content)
		if os.path.isdir(full_path) == True:
			delete_all_contents(full_path)
			print "FOLDER delete: ", full_path
			os.rmdir(full_path)
		else:
			print "FILE delete: ", full_path
			os.remove(full_path)
	print "PARENT FOLDER delete: ", dirname
	os.rmdir(dirname)

delete_all_contents("./" + raw_input("What sub-folder would you like to delete?: "))