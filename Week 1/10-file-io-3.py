'''

Create a program that asks a user for data and a filename and saves it into a one line csv.  A csv file contains comma separated values.  The user can enter multiple pieces of data until they type "quit".  Each piece of data is separated by a comma.

'''

def get_data():
	data = []
	filename = raw_input("Please enter a filename: ")

	print "Now we need some data.\nINSTRUCTIONS: hit \"ENTER\" key between each piece of data and type \"quit\" to finish."

	while True:
		data_piece = raw_input("Insert some data: ")
		if str(data_piece) == "done":
			break
		data.append(data_piece)

	return [filename, data]

def write_file(file_data):
	filename, data = file_data
	if filename.find(".csv") == -1:
		filename = "".join((filename, ".csv"))
	with open(filename, "a+") as csv_file:
		for element in data:
			csv_file.write(element)
			if data.index(element) != (len(data)-1):
				csv_file.write(",")
			else:
				csv_file.write("\n")

write_file(get_data())