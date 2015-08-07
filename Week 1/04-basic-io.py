'''

Every process has three built-in file handles. Standard out, Standard in, and Standard error. Abreiviated as stdout,stdin,stderr.

A process can output data to stdout, read data from stdin, and output errors to stderr.

When you run an application in terminal, these file handles are connected to the terminal you are in.

So if you run a program in terminal and it has a print command in it, the string data gets sent to stdout, which is connected to the terminal screen. 

Unix is based on this idea of chaining commands or processes together, using stdin and stdout.

cat largefile.txt | more

In the case above the cat process prints out the file - largefile.txt to stdout, the more process is invoked which gets that stdout as stdin and can then do further processing on it.


'''


#print "Hello World" to the screen


#print out your name

my_name = "Emilie"

print "Hello, I am %s" % my_name

#print out your city, and country 

my_city = "Austin"
my_country = "United States"

print "I come from %s,%s" % (my_city,my_country)

#use the method raw_input to ask the user for thier city, and then their country, print out both
your_city = raw_input("What city do you live in?: ")
your_country = raw_input("What country do you live in?: ")

print "You come from %s, %s" % (your_city,your_country)

#ask the user to enter a number, then print out that number
your_number =  int(raw_input("Give a number: "))

print "Here's what you typed: %i" % your_number


#ask the user to enter their birth year, calculate their age and print it to the screen
your_birth_year = int(raw_input("What year were you born?: "))
age = 2015 - your_birth_year

print "This is your age: %i" % age


#ask the user for the tempature in fahrenheit, convert it to celsius and print out the result
#c = (f - 32) * (5/9)
f = float(raw_input("What's the current temperature(in Fahrenheit)?: "))
c = (f - 32) * (5.0/9.0)
print "The current temperature in Celsius is: %f" % c


#ask the user for a price (ex: 20.54) and calculate a 20% tip. Print out both the total amount and the tip amount
price = float(raw_input("What is the price of your meal?: "))
tip = price * .2

print "The tip is: %s \n The total price and tip is: %s" % ('${:,.2f}'.format(tip), '${:,.2f}'.format(price + tip))