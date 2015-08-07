'''

OOP (Object Oriented Programming) is a type of programming where instead of defining data and functions that work on that data separately, you can combine them to create an entity that ties together the data and the code that works on them.

The main concepts in OOP are:

1) Encapsulation 
2) Inheritance
3) Polymorphism

We will work through all of these concepts in different exercises.

At a very high level the idea is to create a class or type of entity that can serve as a blueprint, almost like a taxonomy. Once this type or class has been defined you can then have other classes inherit from it and then change its behavior. Classes can inherit from other classes. 

First, read this article for an overview of OOP:
http://www.python-course.eu/object_oriented_programming.php

Then, for a live-code of OOP concepts, please watch the following video:
Part 32 - 35 https://www.youtube.com/watch?v=JToAsK_7GmU

'''


class FirstClass:
    pass #pass just tells python that we are passing on providing anymore details 


#Create a new instance of Firstclass and assign to f
f = FirstClass()

assert f.__class__.__name__ == 'FirstClass'


class SecondClass:
    #this is a class variable, all instances of SecondClass share this variable
    class_items = []

#create two instances of SecondClass s1,s2
s1= SecondClass()
s2= SecondClass()

assert s1.__class__.__name__ == 'SecondClass'
assert s2.__class__.__name__ == 'SecondClass'

#append the string "shared item" to class_items of s1

assert s1.class_items == s2.class_items


#most of the time we do not want to share data across all instances, but tie a variable to each instance.
#__init__ is a special method name, it tells python that when you create a new instance of Counter2 call this method first. If the class is a
#blueprint, then the constructor method "builds" an new instance of the class, creating an object.         

class ThirdClass:
    def __init__(self):
        self.my_instance_var = ""

#create two instances of ThirdClass t1,t2
t1 = ThirdClass()
t2 = ThirdClass()

assert t1.__class__.__name__ == 'ThirdClass'
assert t2.__class__.__name__ == 'ThirdClass'

#assign the string "First Instance" to t1.self.my_instance_var, and "Second Instance" to t2.self.my_instance_var

t1.my_instance_var = "First Instance"
t2.my_instance_var = "Second Instance"

assert t1.my_instance_var == "First Instance"
assert t2.my_instance_var == "Second Instance"

assert t1.my_instance_var != t2.my_instance_var


#classes can also contain functions, when a function is apart of a class it is called a method

class FourthClass:
    def whatami(self):
        print "I am a method of the FourthClass"


#Create a new instance of FourthClass and assign to fourth
fourth = FourthClass()

assert fourth.__class__.__name__ == 'FourthClass'

#call the method .whatami()
fourth.whatami()

class MyNum:
    def __init__(self):
        self.num = 0
    def string_value(self):
        return "MyNum:" + str(self.num)

#create an instance of MyNum and assign to m
m = MyNum()

assert m.__class__.__name__ == 'MyNum'

#change the value of m's num to 5
m.num = 5

assert m.num == 5

#add a new method to MyNum, that returns a string in the following format MyNum:[num]

assert m.string_value() == "MyNum:5"


#Update the __init__ method to take a parameter

class ClassConstruct:
    def __init__(self, more):
        self.more = more
    def __str__(self):
        return "string representation"

cc = ClassConstruct("extra data")

#add a __str__ method to ClassConstruct

assert str(cc) == 'string representation'






        
