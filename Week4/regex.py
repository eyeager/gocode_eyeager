'''

Regular expressions are a powerful tool to identify patterns in text.

This can be used to:

1) search,
2) validate,
3) extract, and
4) replace data.

Try out this online tool to help test regex: http://pythex.org/

Here is a nice cheatsheet put together by a student at MIT: http://web.mit.edu/hackl/www/lab/turkshop/slides/regex-cheatsheet.pdf

'''



import re



#find the number in this text

a = "In the year 2000"

regex = r"(\d{4})$"

assert re.search(regex,a).groups()[0] == '2000'


#use match to see if the input is valid

a = "<html>"

regex = r"^(<.*>)"

assert re.match(regex,a)

a = "</html>"
regex = r"^(</.*>)$"

assert re.match(regex,a)


a = "me@awesome.com"
regex = r"^(\w+@\w+.\w+)$"

assert re.match(regex,a)

#find and group all the numbers in this text

a = "10 20 30"

regex = r"(\d{2})"

assert re.findall(regex,a) == ['10', '20', '30']


#Using regex pull out all the theater numbers

a = '''Theater 1
Theater 2
'''

regex = r"Theater (\d)\n"

assert re.findall(regex,a) == ['1','2']


#using regex print out all the movie names

a = '''Theater 1: Jurasic Park 
Theater 2: Fight Club
Theater 3: Skyfall
'''

regex = r"Theater (\d): (.*)\b"

assert re.findall(regex,a) == [('1', 'Jurasic Park'), ('2', 'Fight Club'), ('3', 'Skyfall')]








