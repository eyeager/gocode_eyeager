'''

A classic interview question. 

In python you can evalute expressions on the fly using eval().

In this exercise we are going to create a simple math eval function called my_eval. The function takes a mathmatical expression and evalutes it, returning the correct total. 

It is simplified in that we IGNORE operator precedence and evalute simply from left to right.

What does eval do? http://stackoverflow.com/questions/9383740/what-does-pythons-eval-do

'''
def my_eval(exp):
	total = int(exp[0])

	operations = {
		"+": (lambda x,y: x+y),
		"*": (lambda x,y: x*y)
	}

	for index,value in enumerate(exp):
		if value in operations:
			total= operations[value](total,int(exp[index+1]))

	return total

# tip: consider using lambdas

assert my_eval("2+6*9") == eval("(2 + 6) * 9")