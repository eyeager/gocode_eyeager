# Write a recursive algorithm that goes into a nested hash structure and sums all key, value pairs - where the value is not a hash

test_hash = {1:2,3:{4:5}}


def sum_hash(test_hash):
	total = 0
	for keys,values in test_hash.items():
		for each in keys,values:
			if type(each) != dict:
				total += int(each)
			else:
				total += sum_hash(each)
	return total

r = sum_hash(test_hash)

assert r == 15

# Write a recursive algorithm that goes into a nested array with integers and sums all the integers.

array = [1,2,3,[4,5,6,[2,3,4,5]]]


def sum_array(array):
	total = 0
	for item in array:
		if type(item) == list:
			total += sum_array(item)
		else:
			total += item
	return total

r = sum_array(array)

assert r == 35


# Write a function permute such that:
# permute('abc') returns ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
'''
def permute(string):
	new_string = ""
	if len(string) == 0:
		return ""

	print "String: ", string
	for letter in string:
		i = 0
		print "String portion:", string[1:]
		new_string += letter + permute(string[1:])
		#for i < len(string):
#
#			i++
		#new_string += letter
	print "New String: ",new_string
	return new_string


permute('abc')
'''

# Write a function that computes factorials using tail call recursion
def compute_factorials(number, count):
	if count == 1:
		return 1
 	return compute_factorials(number*count, count-1)

def call_factorials(number):
	compute_factorials(number,number-1)

print call_factorials(5)

# Write a function that returns the greatest common denominator of two numbers using tail call recursion

