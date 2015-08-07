'''

Part 1: Make a program that keeps track of your budget.  The user can type in commands via the terminal to make changes/add/show the budget.

- Create a program with a simple ui loop (a function that has a while loop which keeps the program running).  THe loop will repeatedly display a list of commands and ask the user for input. (Commands are listed below)
- Once the input action is complete, display the list of command options again until the user quits (enters "q").
- Each command has an associated function that gets called when the user enters the right letter.  You will write these functions.


Commands:

"a" Add an item to the budget - should ask the user for each field name, amount, monthly
"s" Show items in the budget - calculates the total amount of expenses
"r" Remove an item from the budget
"q" Quit Program


'''

import os 

# Prints out command options for the user
def loop_output():
	print "\nSelect an option:"
	print "\t(a) Add an item to the budget\n \
	(l) List items in the budget\n \
	(d) Delete an item from the budget\n \
	(s) Save total budget to a file\n \
	(r) Read input from file to the budget app \n \
	(q) Quit Program\n"

# Tests if value is a float
def is_float(value):
	try:
		float(value)
		return True
	except ValueError:
  		print "Invalid input! Amount must be a number."
  		return False

def is_yn(value):
	if value == "y" or value == "n":
		return True
	else:
		print "Invalid input! Must input \'y\' or \'n\'."
		return False

# Asks user for input to add items to a dictionary. Returns dictionary
def add_item(full_budget):
	# Asks the user for each field name, amount, monthly
	name = raw_input("Please enter a name for the budget item: ").lower()
	amount = raw_input("Please enter an amount: ")
	monthly = raw_input("Is this budget item a monthly charge?(y/n): ").lower()

	# Verifies that amount is an int or float. Asks for new input if not.
	while is_float(amount) == False:
		amount = raw_input("Please enter an amount: ")
	else:
		amount = float(amount)

	# Verifies that 'monthly' is 'y' or 'n'
	while is_yn(monthly) == False:
		monthly = raw_input("Is this budget item a monthly charge?(y/n): ").lower()

	return full_budget.append({"name" : name, "amount" : amount, "monthly" : monthly})

# Shows user all items in array containing dictionaries. Returns nothing
# Show items in the budget - calculates the total amount of expenses
def list_item(full_budget):
	total = 0
	for item in full_budget:
		total += float(item["amount"])
		print "Name: %s\tAmount: %s\tMonthly: %s" % (item["name"],item["amount"],item["monthly"])
	print "Total in budget: %.2f" % total

# Asks user for input to find item to remove from array of dictionaries. Returns updated array (hm... that's a different return type)
def delete_item(full_budget):
	list_item(full_budget)
	name_delete = raw_input("What item would you like to remove?: ").lower()

	for key,item in enumerate(full_budget):
		if item["name"] == name_delete:
			verify = raw_input("Is this the item you'd like to delete? \n %r\n(y/n):" % item).lower()
	
			while is_yn(verify) == False:
				verify = raw_input("Is this the item you'd like to delete?\n %r" % item).lower()

			if verify == "y":
				full_budget.pop(key)
		else:
			print "Budget item not found. Try running a delete again."

	return full_budget

def save_csv(full_budget):
	filename = raw_input("What would you like to save your file as?: ")

	if filename.find(".csv") == -1:
		filename = ".".join((filename, "csv"))

	try:
		with open(filename,"w") as csv_file:
			csv_file.write("name,item,monthly\n")
			for item in full_budget:
				csv_file.write("%s, %s, %s\n" % (item["name"],item["amount"],item["monthly"]))
	except IOError:
		print "Permissions error. Cannot write to file or folder."

def read_csv(full_budget):
	print "Here are files you may import from:"
	for file in os.listdir("./"):
		if file.endswith(".csv"):
			print(file)

	import_file = raw_input("\nType a file name you'd like to import: ")
	while not os.path.exists(import_file):
		import_file = raw_input("File does not exist. Try again: ")

	with open(import_file,"r") as open_file:
		lines = open_file.readlines()

	for line in lines[1:]:
		line_array = line.strip('\n').split(',')
		full_budget.append({"name": line_array[0], "amount": line_array[1], "monthly": line_array[2]})

	return full_budget

# Calls list_item, says goodbye and returns empty to end the parent while loop.
def quit_program(full_budget):
	print list_item(full_budget)

	save = raw_input("Would you like to save your budget? (y/n): ")
	while is_yn(save) == False:
		save = raw_input("Invalid input. Would you like to save your budget? (y/n): ")
	if save == "y":
		print "Saving..."
		save_csv(full_budget)

	print "\nThanks for using Emilie's budget app. Goodbye!\n"
	return "quit"

def ui_loop():
	return_value = "None"
	full_budget = []

	print "Welcome to the budget app.\nI'll ask you for some info and keep track of your expenses."

	while return_value != "quit":
		loop_output()
		user_input = raw_input("Please type a command listed above:").lower()

		# Gets the function that needs to run, then runs it as "command_output"
		functions = { 
			'a' : add_item,
			'l' : list_item,
			'q' : quit_program,
			'd' : delete_item,
			's' : save_csv,
			'r' : read_csv
		}

		if functions.has_key(user_input):
			return_value = functions[user_input](full_budget)
		else:
			print "Not a valid entry. Try again!"

		if type(return_value) == list:
			full_budget = return_value

ui_loop()

'''
**** Finish part one before moving on to Part 2 ****


A csv file is a very simple file that is used quite often. Usually a csv file will look something like this:

(a simple expenses csv file)

---
name,amount,monthly
food,1000.00,y
rent,2000.00,y
braces,2000.00,n
---


A csv usually starts with a header line that lists the names of the fields so someone reading or importing it into a spreadsheet app knows what each column is for.

Your goal is to write a simple budget app. This application will have a simple interface that shows the list of commands to the user, and allows the user to enter a command and keep doing various commands until they say
quit. 

It will store the data it gets from the user in a csv file. 

Add the following commands

1. "s" - Save file -> this converts your internal data structure to a csv and rights it out
2. "r" - Read File -> reads from a csv and converts the data into your internal data structure.

To test your output, you should be able to open the file in a spreadsheet application (e.g. Excel) after closing.

'''

 
    
