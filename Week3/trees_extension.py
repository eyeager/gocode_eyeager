'''

We looked at a way to interpret or eval a mathmatical string by going through the string left to right.

It is not a bad approach but it ignores operator precedence and over all is not very clean.

What if instead we parsed the string and turned all the operators and operands into a tree.

Below is a version of that, using a tree.

1) Fill out OpNode to store either an operater or operand, and the left/right nodes, which are numbers.  Store all these as instance variables.

2) Write a solve() method that then takes the OpNode tree and solves it and computes the final value of the tree

3) Bonus: Refactor this code to use an Operator class and an Operand class instead of one OpNode class

4) Double Bonus: Write a parser that reads a string ("1+2*6") and builds the tree (using OpNode) that then can be solved using the solve() method

'''

import sys


class OpNode:
    
    def __init__(self,operator=None,operand=None):
        self.operator = operator
        self.operand = operand
        self.left = None
        self.right = None

def in_order_print(root):
	if root == None:
		return

	in_order_print(root.left)
	if root.operator != None:
		print root.operator
	if root.operand != None:
		print root.operand
	in_order_print(root.right)
        
def pre_order_print(root,tab):
	if root == None:
	    return

	if root.operator != None:
		print tab,root.operator
	if root.operand != None:
		print tab,root.operand
	#print root.operand, root.operator
	pre_order_print(root.left,tab[:-1])
	pre_order_print(root.right,tab + "\t")

def solve(root):
    pass
                        



# Our expression is:  2 + 4 * 7

#lets build a tree that represents this

r = OpNode('*')

#Its right is 7

r.right = OpNode(None,7)

#now for the left side

lr = OpNode('+')

lr.left = OpNode(None,2)
lr.right = OpNode(None,4)

#now we set it to the right of the root

r.left = lr


#lets take a look at it
print "Preorder tree"

pre_order_print(r,"\t\t\t\t")

#how about in order

print "Inorder: "
in_order_print(r)
print


assert solve(r) == 42