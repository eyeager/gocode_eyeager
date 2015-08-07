'''

Programs need to change their logic based on conditions. To do this we use if/else/elif statements. 

'''

# add an if statement around the print so that it is only printed when a is True

a = True

if a == True:
	print "A is true"


#do it again around the print statement below

a = False

if a == True:
	print "A is true"


#add an if else statement to make these next lines print properly

a = False

if a == True:
	print "A is true"
else:
	print "A is false"


#add an if elif else to the following print statements to print the lines properly

a = False
b = True
c = False

if a == True:
	print "A is true"
elif b == True:
	print "B is true"
elif c == True:
	print "C is true"


#use the and operator to test two conditions

a = True
b = True

if a == True & b == True:
	print "Both A and B are true"


#use the or operator to test if either condition is true

a = True
b = False

if a == True or b == True:
	print "A or B is true"


#use the not operator to correctly print the line

a = False

if a != True:
	print "A is false"






