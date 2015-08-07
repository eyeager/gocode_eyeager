# Part A.  Don't look at your notes for this section

#1) Using Big-O notation, describe the worst-case scenario following algorithm:
# What is the best case scenario for the algorithm?
# Worst case = len(data)-1 ** len(data)-1 ?
# Best case = Items are already in order. For loop only runs through 2*len(data)-1 times (since False flag and test are after the loop)

def algo(data):
    swap = True
    while True:   
        for i in range(0,len(data)-1):
            if data[i] > data[i+1]:
                data[i],data[i+1] = data[i+1],data[i]
                swap == True          
        if swap == False:
            return data   
        swap = False


#2) When would you use exceptions in writing a Python program?
'''
This is useful when unsure of the outcome of a command. Exceptions deal with error cases in a more controlled way
and can allow your program to continue running. 

For example, you'd want to use this when ensuring/testing user input is an integer. 
Instead of the program crashing, you can ask for more input.
'''
print "\nQuestion 2"

def test_int(user_input):
    while True:
        try:
            user_input = int(user_input)
            print "Yay! Thanks! That's an integer."
            return user_input
        except:
            user_input = raw_input("That was not an integer. Please give me an integer: ")

user_input = test_int(raw_input("Please give me an integer: "))
print type(user_input)

#3) Loops Hashes Arrays Re-cap!

'''
print all the keys in d using a for-loop

Output should be
    
Phone-Number
Address
Phone-Number
Address
'''
print "\nQuestion 3"

d = [{"Phone-Number": "555-1212","Address":"306 S. Lamar"},
     {"Phone-Number":"555-1213","Address":"Sonnenallee 14"}]

for entry in d:
    for keys in entry: # or entry.keys() - keys are the default called. Must specify .values() if you want the values
        print keys


#4) Solve this iteratively or recursively.  Feel free to use a whiteboard

'''The Fibonacci numbers are the numbers of the following sequence of integer values: 

0,1,1,2,3,5,8,13,21,34,55,89, ... 

The Fibonacci numbers are defined by: 
Fn = Fn-1 + Fn-2 
with F0 = 0 and F1 = 1 

The Fibonacci sequence is named after the mathematician Leonardo of Pisa, who is better known as Fibonacci. In his book "Liber Abaci" (publishes 1202) he introduced the sequence as an exercise dealing with bunnies. His sequence of the Fibonacci numbers begins with F1 = 1, while in modern mathematics the sequence starts with F0 = 0. But this has no effect on the other members of the sequence. 

The Fibonacci numbers are easy to write as a Python function. It's more or less a one to one mapping from the mathematical definition:
'''

print "\nQuestion 4"

def fib_calc(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib_calc(number-1) + fib_calc(number-2)

def call_fib_calc(number):
    fib_array = []
    number = test_int(number)

    for each in range(0,number):
        fib_array.append(fib_calc(each))

    print fib_array

call_fib_calc(raw_input("How many Fibonacci numbers would you like to print?: "))

#5) Describe the stack data structure.  When would you use it?
'''
This is a Last In, Last Out structure. It is actually just a list, but used like a stack by using only the append and pop functions. 
We used this in a few exercises for HTML and other syntax checking. Useful when trying to match pairs or keeping a history 
when you'd like to know the last actions completed- like a web browser back button.

'''


# Part B. You can look at your notes for this section


#1) Count the number of instances of each client in the list below, and build a hash with those counts

a = [('client1','blah'),('client1','other'),('client1','other'),('client2','blah'),('client2','other'),('client3','other')]

r = {}
for client_data in a:
    if client_data[0] in r:
        r[client_data[0]] +=1
    else:
        r[client_data[0]] = 1

assert r == {'client1': 3, 'client2': 2, 'client3': 1}


#2) Add exception handling around the following
print "\nPart B. Question 2"

try:
    f = open("I-Dont-exist.jpg","r")
except:
    print "Cannot open file. File does not exist."


#3) Square all the numbers recursively,returning a new list/array

a = [1,2,3,4]

def square_r(values):
    return map(lambda x: x**2, a)

assert square_r(a) == [1,4,9,16]


#4) Update the hash value to be a lambda that adds 2 to a number

a = {"+2":lambda x: x+2}

assert a["+2"](5) == 7

#5) Use a list comprehension to add two to all numbers in a

a = [5,7,9]

r = [num+2 for num in a]

assert r == [7,9,11]


#6) Write a recursive algorithm that sums all the values of a nested hash
print "\nPart B. Question 6"

# Grrr. I'm close, but I end up getting 5 or 1. Needed more time
def sumhash(hash_input,total=0):
    for value in hash_input.values():
        print value, total

        if type(value) == int:
            total += value
        elif type(value) == dict:
            sumhash(value,total)
    print total
    #return total

sumhash({'a':1,'b':{'c':3}})

assert sumhash({'a':1,'b':{'c':3}}) == 4



