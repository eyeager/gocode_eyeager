'''

Build a simple user info database.

'''


#create a new function that asks the user for the same three pieces of information but this time store the data in an dictionary (hint: {age: 1,name:'asdf',city:'test'}.
def get_user_info():
	user_info = {}
	user_info.update({"name" : raw_input("What is your name?:")})
	user_info.update({"age" : raw_input("What is your age?:")})
	user_info.update({"city" : raw_input("What is your city?:")})
	return user_info

#create a new function to ask for data from 3 users using the function above (use a for loop). return an array of hashes (hint: [{age: 1,name:'asdf',city:'test'},{age: 1,name:'asdf',city:'test'}])
def get_many_users():
	user_db = []
	user_num = int(raw_input("How many users would you like to input?: "))
	i = 0
	while i < user_num:
		user_db.append(get_user_info())
		i += 1
	return user_db


#create a new function that prints out all the user data
#Ex: User 1 - First Name: Bob, Age: 76, City: Bethesda
#(doesn't have to be printed out in one line)

def print_users():
	full_user_list = get_many_users()

	for user in full_user_list:
		print "User %i" % (full_user_list.index(user) + 1)
		for info in user:
			print "\t%s: %s" % (info, user[info])

print_users()