'''

The next pillar of OOP in inheritance. The ability to have classes inherit from other classes, taking on their attributes and behavior. The idea here is to have code reuse. 

You can create a subclass which inherits all of the features of a superclass. The subclass can add or replace method functions of the superclass. 

This is typically used by defining a general-purpose superclass and creating specialized subclasses that all inherit the general-purpose features but add special-purposes features of their own.

Below there are four classes defined. The top most is called Animal. This is called the superclass, because the other classes inherit from it. To denote inhertiance with specify the class name in parenthesis.

    Animal
      |
    Mammal
    |    |
   Dog  Cat


There are two key concepts in inheritance - 'overloading' and 'overriding':

1) Overloading: Overloading is the ability to define the same method, 
with the same name but with a different number of arguments and types. 
It's the ability of one function to perform different tasks, 
depending on the number of parameters or the types of the parameters. 

2) Overriding: Overriding means, that the first definition is not available anymore.
Usually, it is replaced by another function with the same name.

Here are some additional examples of basic inheritance in Python:
http://www.python-course.eu/inheritance_example.php


'''

#isinstance(d,Animal)

class Animal:
    def __init__(self):
        print "Create an Animal"


class Mammal(Animal):
    def __init__(self):
        print "Create a Mammal"
    def speak(self):
        print ""

class Dog(Mammal):
    def __init__(self):
        print "Create a Dog"
    def speak(self):
        print "Woof"

class Cat(Mammal):
    def __init__(self):
        print "Create a Cat"
    def speak(self):
        print "Meow"

class Penguin(Mammal):
    def __init__(self):
        print "Create a Penguin"
    def speak(self):
        print "Squawk"

class Sloth(Mammal):
    def __init__(self):
        print "Create a Sloth"
    def speak(self):
        print "Zzzzz"


#Extend the list of animals by adding two more animal types derived from Mammal


        
#Create a base class called Employee.
#This class takes a name and a salary in its constructor (init).
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


#Create a new class called FullTime. Fulltime inherits from Employee.
class FullTime(Employee):
    pass

#Create a new class called Executive, also inherits from Employee
class Executive(Employee):
    pass

#These classes will be used in the polymorphism exercise.










        

        
