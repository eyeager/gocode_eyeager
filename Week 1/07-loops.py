'''

Loops are used to repeatedly do something. There are two basic looping constructs in Python. The for loop and the while loop. In general you would use a for loop when looping through a data structure
or when the number of times to loop is known ahead of time. A for loop also helps with book keeping of counts or items out of a data structure. 

A while loop, can be used like a for loop, but it is more commonly used when you do know ahead of time when you need to stop looping. Keep doing something while some condition is true.

Heuristics on which looping constructs.
- If you are looping through a fixed length data structure e.g List, or Dictionary 
and you don't need to modify that data structure then use "for in"
- If need to modify the data structure, then use for i in range of length array of array
or for key in d.keys()
- If you don't know when to end when to start use a while
while something is true keep doing all the things
If you need additional for-loop reading this is a good piece:
https://blog.udemy.com/python-for-loop/
There are additional exercises here for those who need more:
http://www.learnpython.org/en/Loops
http://www.coderbyte.com/CodingArea/Challenges/

If you need additional for-loop reading this is a good piece:
https://blog.udemy.com/python-for-loop/

There are additional exercises here for those who need more homework:
http://www.learnpython.org/en/Loops
http://www.coderbyte.com/CodingArea/Challenges/

'''

#use a for loop to print the numbers 1 to 100, use the range function
for i in range(1,100):
	print i


#use a for loop and if statements to print out the numbers 1 to 100 and print if the number is odd or even
for i in range(1,100):
	if i % 2 == 0:
		print "Even number: %i" % i
	elif i % 2 != 0:
		print "Odd number: %i" % i


#use a for loop to print every character in the string
string = "!@#$%"
for i in string:
	print i



#use a while loop to print out the numbers 1 to 100
i = 1
while i <= 100:
	print i
	i += 1


#use a while loop to keep asking the user for a number until they enter "quit"
user_input = ""

while user_input != "quit":
	user_input = raw_input("Enter a number (type \"quit\" to finish): ")


#create a simple number guessing game
#The program stores a random number between 1 to 10.  
#Use a while loop to repeatedly ask the user to guess the number
#The loop stops when the user guesses correctly

from random import Random

r = Random()

random_number = r.randint(1,10)
guess = ""

while guess != random_number:
	if guess != "":
		print "Your guess is wrong. Try again."
	guess = int(raw_input("Guess a number between 1 and 10: "))

#create a simple summing calculator: Repeatedly ask the user for a number and keep a running sum of the numbers entered. Print the sum each time. Quit when they enter 0.
user_input = float(raw_input("Enter a number to add to the total: "))
total = 0
while user_input != 0:
	total = total + user_input
	user_input = float(raw_input("Enter a number to add to the total (type '0' to end): "))
print "The total is: %f" % total


#create an age guessing program: The program stores a random number between 1 to 100.  Use a while loop to ask the user to guess the number, if the guess is correct, print "correct", else respond with "guess higher" or "guess lower".
r = Random()

age = r.randint(1,100)
guess = 0

while guess != age:
	guess = int(raw_input("Guess my age (between 1 and 100): "))
	if guess < age:
		print "Guess higher!"
	elif guess > age:
		print "Guess lower!"


'''
Using loops and just one print statment, write a program that outputs the following

##### 
#### 
### 
## 
#
'''

for i in range(5,0,-1):
	print "#" * i