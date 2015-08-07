
'''

A good use for OOP is to create new data types. So let's do that. We are going to create a new data type to handle fractions.

Fix the following code to be able to add and equate fractions.

'''

def gcd(m,n):
     """ Greatest Common Divisor """
     while m%n != 0:
          oldm = m
          oldn = n

          m = oldn
          n = oldm%oldn
     return n

class Fraction:
     def __init__(self,top,bottom):
          # top
          self.top = top
          # bottom
          self.bottom = bottom

     def __str__(self):
          return str(self.top) + "/" + str(self.bottom)

     def __add__(self,otherfraction):
          big_bottom = self.bottom * otherfraction.bottom
          big_top = (self.top * otherfraction.bottom) + (otherfraction.top * self.bottom)

          common = gcd(big_top,big_bottom)
          big_top = big_top / common
          big_bottom = big_bottom / common

          return Fraction(big_top,big_bottom)

     def __eq__(self, other):
          if self.bottom != other.bottom:
               big_top_self = self.top * other.bottom
               big_top_other = other.top * self.bottom

          if self.top == other.top:
               return True
          else:
               return False


    
x = Fraction(2,4)
y = Fraction(2,3)

assert x+y == Fraction(7,6)

x = Fraction(5,6)
y = Fraction(2,3)

assert x+y == Fraction(3,2)



