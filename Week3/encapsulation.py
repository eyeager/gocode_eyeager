'''

A key concept in OOP is encapsulation. The idea that data and the code that works on that data are bound together. The other benefit is you can limit how other code can access the data. It is always good to limit how data can change and by whom, to prevent bugs. 

To give an example. Lets say I need to keep count of something. The easiest way is just to define a variable "my_counter" and throughout the code I increment the counter in various places.

Everything is great until... some other developer doesn't understand the code and wants to use the counter, so they somewhere in the code call my_counter = 0. Now every once and a while the count of things get screwed up. While this is a little simplified, this type of bug happens all the time!

Usually it won't be as straight forward as setting the var back to zero, but somewhere along the way some code mucks with a varibale. The bug presents itself at erratic times and is very difficult  to debug. In a large code base with multiple people working on it, it is very easy for things like this to happen.

So instead of just using a variable, lets use a class to encapsulate the data!  This allows us to hide the data and reduce bugs like the one just mentioned.

Try the exercise below to see how we can "encapsulate" data and create functions that that modify the data that is encapsulated.

'''


class Counter:
	def __init__(self):
	    self.counter = 0 
	def current_count(self):
		return self.counter
	def increment(self):
		self.counter += 1
		return self.counter
	def increment_10(self):
		self.counter += 10
		return self.counter
	def increment_input(self,number):
		self.counter += number
		return self.counter
	def reset(self):
		self.counter = 0
		return self.counter


#Create a new instance of Counter
c = Counter()

assert c.__class__.__name__ == 'Counter'

#add a method to Counter called .current_count() to get the current value of counter


assert c.current_count() == 0


#add a new method to Counter to increment the counter by 1

c.increment()

assert c.counter == 1

#add a new method to Counter to increment the counter by 10
c.increment_10()

assert c.counter == 11


#add a new method to Counter to increment the counter by any integer passed into the method
c.increment_input(4)

assert c.counter == 15

#add a new method to Counter to reset the counter to zero
c.reset()

assert c.counter == 0





