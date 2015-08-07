# Write a function which implements the Pascal's triangle:

# 1
# 1    1
# 1    2    1
# 1    3    3    1
# 1    4    6    4    1
# 1    5    10    10    5    1

# The desired output should be a list of lists where each internal list contains one row of the triangle. Like so:

# [[1], [1, 1], [1, 2, 1]...]

def pascal(n):
	if n == 1:
		return [1]

	new_row = [1]
	last_row = pascal(n-1)
	print last_row
	for i in range(len(last_row)-1):
		new_row.append(last_row[i] + last_row[i+1])
	new_row += [1]

		#print n
		#return (pascal(n-1) + pascal(n-2))
		#n -= 1
		# full_array[n][c] = array[n-1][c-1] + array[n-1][c]


print pascal(5)

#assert pascal(3) == [[1], [1, 1], [1, 2, 1]]