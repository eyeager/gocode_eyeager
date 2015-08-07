
#use a for loop to print out each element of the array

a = ["A","B","C"]
for letter in a:
	print letter


#use a while loop to print out each item in the array but also its index as well Ex: 0 A 
index = 0
while index < len(a):
	print "%i %s" % (index, a[index])
	index += 1

#use a for loop plus the enumerate method to print out the item but also its index as well
for each in enumerate(a):
	print each

#using a loop sum the array

a = [25,35,45]
r = 0
for num in a:
	r += num

assert r == 105


#using a loop get the avg for the array

a = [25,35,45]
total = 0
for num in a:
	total += num
r = total / len(a)
assert r == 35

#use a for loop and iteritems to print all the keys and values in this hash

a = {"key1":"value1","key2":"value2"}
for pair in a:
	print pair,' ',a[pair]


#use the items method to turn the hash into an array

a = {"key1":"value1","key2":"value2"}
r = []
for i in a.items():
	r.append(i)
assert r == [('key2', 'value2'), ('key1', 'value1')]


#create an array of hashes
r = [{"key1":"value1"},{"key2":"value2"}]
assert type(r[0]) is dict


#create any hash where the value of the keys is a dictionary
r = {"key1" : {"inner_key1" : "value1"}, "key2" : {"inner_key2" : "value2"}}
assert type(r.values()[0]) is dict

#use for x in a to print all the keys of a

a = {"key1":"value1","key2":"value2"}
for x in a.keys():
	print x


'''
use a nested for loop to print all the keys in a

output should be

outer_key1
inner_key1
outer_key2
inner_key2
'''

a = {"outer_key1":{"inner_key1": "inner_key_value1"},
     "outer_key2":{"inner_key2": "inner_key_value2"}}

for outer_key in a:
	print outer_key
 	for inner_key in a[outer_key]:
 		print inner_key


'''
print all the keys and the array values in a

output should be

second_array
4
5
6
first_array
1
2
3
'''


a = {"first_array": [1,2,3],
     "second_array": [4,5,6]}

for key in a:
	print key
	for value in a[key]:
		print value


'''
print all the keys in a

Phone-Number
Address
Phone-Number
Address
'''

a = [{"Phone-Number": "555-1212","Address":"306 S. Lamar"},
     {"Phone-Number":"555-1213","Address":"Sonnenallee 14"}]

for each in a:
	for i in each.keys():
		print i






