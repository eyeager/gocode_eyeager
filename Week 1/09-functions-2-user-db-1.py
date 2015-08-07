'''

Build a simple user info database.

'''

#create a function that asks a user for three pieces of information, first name, city, age. store the data in an array [name,city,age].
def ask_for_info():
	name = raw_input("What's your name?: ")
	age = raw_input("How old are you?: ")
	city = raw_input("What city do you live in?: ")
	return [name, age, city]


#create a function that uses the previous function to ask 3 people for their info (use a for loop).  for each person you store first name, city, age. use only arrays. this function should return an array with all the user data (hint: use an array of arrays [[name,city,age],[name,city,age],[name,city,age]]).
def multiple_user_info():
	user_num = int(raw_input("How many users would you like to input?: "))
	user_db = []
	i = 0
	while i < user_num:
		user_db.append(ask_for_info())
		i += 1
	return user_db


#create a function that takes the result from the previous function and prints out all the user data.
#Ex: User 1 - First Name: Bob, Age: 76, City: Bethesda
#(tip: doesn't have to be printed out in one line)

def print_users():
	full_user_list = multiple_user_info()
	user_count = 1

	for user in full_user_list:
		print "User %i - First Name: %s \n\tAge: %s \n\tCity: %s " % (user_count,user[0],user[1],user[2])
		user_count += 1
		#for info in user:
		#	print info

print_users()