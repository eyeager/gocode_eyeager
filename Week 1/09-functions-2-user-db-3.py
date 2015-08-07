'''

Build a simple user info database.


'''
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

#Create a new function to ask 3 users for data using the previous function in exercise two that returns a dictionary for a single user.  This new function will return a dictionary. Each user dictionary should be stored under the key of that user's name. Example {'Bob': {age: 1,name:'asdf',city:'test'},'Susan': {age: 1,name:'asdf',city:'test'}....
def get_many_users():
	user_db = {}
	user_num = int(raw_input("How many users would you like to input?: "))
	i = 0
	while i < user_num:
		user_dict = get_user_info()
		user_db.update({user_dict["name"] : user_dict})
		i += 1
	return user_db

#create a function to print out the new dictionary-based user data.
#Ex: User 1 - First Name: Bob, Age: 76, City: Bethesda
#(doesn't have to be printed out in one line)

def print_users():
	full_user_list = get_many_users()

	for user in full_user_list:
		print "User %s" % (user)
		for info in full_user_list[user]:
			print "\t%s: %s" % (info, full_user_list[user][info])

print_users()

'''

Additional Reading:

Read this short guide about functions up to 1.6.4

'''


