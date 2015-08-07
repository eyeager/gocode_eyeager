#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

total = sum([threes for threes in (range(0,100,3))] + [fives for fives in (range(0,100,5))])

print total

'''
total = 0
for threes in range(0,100,3):
	total += threes
for fives in range(0,100,5):
	total += fives

print total
'''