def make_prime_array(end):

	#prime_test_numbers = range(2,int(round(end ** .5))+1) # Range from 2 to the sq rt of the ending number
	prime_array = range(2,end+1)

	# Loop for removing primes
	for testing_number in range(2,int(round(end ** .5))+1):			#For each number that exists in the array of numbers to test
		for number_in_array in prime_array:				#For each number that exists in the prime array (2 - end)
			#if number_in_array % testing_number == 0:	#Tests if the number in the prime_array is divisible by the test array
				#for index,non_prime in enumerate(prime_array):			#Loops again over the prime_array 

					#Tests if number in array is divisible by the non_prime number. Also won't remove itself from the array
					#if non_prime % testing_number == 0 and non_prime != testing_number:
						prime_array[index] = FalseIOError: [Errno 2] No such file or directory: 'idontexist.txt'	#Removes any that are divisible by the number we just proved to be non-prime

	return prime_array

def is_prime(start,end):

	prime_array = make_prime_array(end)
	return prime_array

'''
	for test_number in range(start,end+1):
		prime_flag = True
		for divider in range(2, test_number / 2 + 1):
			if test_number % divider == 0:
				prime_flag = False

		# 0 and 1 are not prime numbers
		if prime_flag == True and test_number != 0 and test_number != 1:
			prime_array.append(test_number)
'''


start = int(raw_input("Select a starting number: "))
end = int(raw_input("Select an ending number: "))

print "Prime numbers between %i and %i are: %s" % (start, end, is_prime(start,end))