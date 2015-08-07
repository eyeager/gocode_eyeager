'''
The bubble sort algorithm compares every two items which are next to each other, 
and swaps them if they are in the wrong order. 
An array of n elements can be sorted within n-1 passes. 

For example, in this array of 4 items:

First pass
(4, 3, 1, 2) > (3, 4, 1, 2)
(3, 4, 1, 2) > (3, 1, 4, 2)
(3, 1, 4, 2) > (3, 1, 2, 4)

Second pass:
(3, 1, 2, 4) > (1, 3, 2, 4)
(1, 3, 2, 4) > (1, 2, 3, 4)
(1, 2, 3, 4) > (1, 2, 3, 4)

Third pass:
(1, 2, 3, 4) > (1, 2, 3, 4)
(1, 2, 3, 4) > (1, 2, 3, 4)
(1, 2, 3, 4) > (1, 2, 3, 4)


'''
#write the bubble sort algorithm

def bubble_sort(data):
	swap_flag = True
	index = 0
	swap_count = 0

	while swap_flag == True:
		while index < len(data)-1:
			if data[index] > data[index+1]:
				data[index], data[index+1] = data[index+1],data[index]
				swap_count += 1
			index += 1

		if swap_count == 0:
			swap_flag = False
		else:
			swap_count = 0
			index = 0

	return data    

assert bubble_sort([6,4,7,8]) == [4,6,7,8]
assert bubble_sort([4,3,1,2]) == [1,2,3,4]