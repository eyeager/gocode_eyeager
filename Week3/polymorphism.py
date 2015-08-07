'''

Polymorphism allows you to treat objects the same even though they maybe be different class instances.

Polymorphism exists when you define a number of subclasses which have commonly named methods. A function can use objects of any of the polymorphic classes without being aware that the classes are distinct.

In some languages, it is essential that the polymorphic classes have the same interface (or be subinterfaces of a common parent interface), or be subclasses of a common superclass. This is sometimes called "strong, hierarchical typing", since the type rules are very rigid and follow the subclass/subinterface hierarchy.

Python implements something that is less rigid, often called "duck typing". The phrase follows from a quote attributed to James Whitcomb Riley: "When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck." In short, two objects are effectively of the class Duck if they have a common collection of methods (walk, swim and quack, for example.)

In a child class, we can change how some methods work whilst keeping the same name. We call this "polymorphism" or "overriding" and it is useful because we do not want to keep introducing new method names for functionality that is pretty similar in each class.

Here is a simple example:

class Food(object):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    def tastesLike(self):
        raise NotImplementedException("Subclasses are responsible for creating this method")
 
class HotDog(Food):
    def tastesLike(self):
        return "Extremely processed meat" 
 
class Hamburger(Food):
    def tastesLike(self):
        return "grilled goodness" 
 
class ChickenPatty(Food):
    def tastesLike(self):
        return "tastes like chicken" 
 
dinner = []
dinner.append(HotDog('Beef/Turkey BallPark', 230))
dinner.append(Hamburger('Lowfat Beef Patty', 260))
dinner.append(ChickenPatty('Micky Mouse shaped Chicken Tenders', 170))
 
# even though each course of the dinner is a different type 
# we can process them all in the same loop 

for course in dinner:
    print course.name + " is type " + str(type(course))
    print "  has " + str(course.calories) + " calories " 
    print "  and tastes like " + course.tastesLike()
 
 
# output: 
# 
#Beef/Turkey BallPark is type <class '__main__.HotDog'> 
#  has 230 calories 
#  and tastes like Extremely processed meat 
#Lowfat Beef Patty is type <class '__main__.Hamburger'> 
#  has 260 calories 
#  and tastes like grilled goodness 
#Micky Mouse shaped Chicken Tenders is type <class '__main__.ChickenPatty'> 
#  has 170 calories 
#  and tastes like tastes like chicken 

'''


# Part 1
#1) Copy the animal classes from the inheritence exercise.
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
#2) Add a new method to all of the classes, called speak().


#3) In each speak method add a print that prints an appropriate line for that animal. print "Woof" for a dog, etc.


#4) Create a new array, and create four new instances, one for each of your animal types.
animal_array = []
animal_array.append(Cat())
animal_array.append(Dog())
animal_array.append(Penguin())
animal_array.append(Sloth())

#5) Write a for loop that enumerates each item in the array, calling the speak method on each instance.
for animal in animal_array:
    animal.speak

# Part 2
#1) Copy the Employee, FullTime, and Executive classes from the last exercise here.
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


#Create a new class called FullTime. Fulltime inherits from Employee.
class FullTime(Employee):
    def wage(self):
        return self.salary

#Create a new class called Executive, also inherits from Employee
class Executive(Employee):
    def wage(self):
        self.salary += (self.salary * .25)
        return self.salary

#2) To each class add a new method called wage()

#3) For FullTime employees the method wage returns their salary. For Executives it returns their salary plus a 25% bonus.

#4) Create an array of five FullTime employees with differing salaries, and three executives with differing salaries.
employees = []
employees.append(FullTime('Bob',50000))
employees.append(FullTime('Che',94000))
employees.append(FullTime('Casey', 85000))
employees.append(Executive('Jim', 150000))
employees.append(Executive('Seth', 180000))

#5) Write a for loop to calculate the wage payout for a year for that company.
total_pay = 0
for employee in employees:
    total_pay += employee.wage()
print "Total pay: %.2f" % total_pay
