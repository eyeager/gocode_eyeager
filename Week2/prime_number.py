def is_prime(start,end):
	prime_array = []


	for test_number in range(start,end+1):
		prime_flag = True
		for divider in range(2, test_number / 2 + 1):
			if test_number % divider == 0:
				prime_flag = False

		# 0 and 1 are not prime numbers
		if prime_flag == True and test_number != 0 and test_number != 1:
			prime_array.append(test_number)
	return prime_array


start = int(raw_input("Select a starting number: "))
end = int(raw_input("Select an ending number: "))

print "Prime numbers between %i and %i are: %s" % (start, end, is_prime(start,end))