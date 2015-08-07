'''

Coursera has a json api that lists all their courses.

Note: For name strings use .encode('ascii', 'ignore') on each one.

The goal of this program is to learn to use an very popular API and understand how to read documentation.

Coursera's API is well-designed and stuctured, but know not all APIs are like that!

Here is the documentation - skim through it:
https://tech.coursera.org/app-platform/catalog/

Pro-tip - it is often easier to just look at the data returned by the endpoint, than to read endless pages of documentation...

'''

import requests

url = "https://api.coursera.org/api/catalog.v1/courses"

coursera_data = requests.get(url).json()

#print out all the course names from coursera_data
for value in coursera_data.values():
	for course_info in value:
		print "Course Name: " + course_info["name"]

#create a new dictionary from coursera_data where each key is the id, and the value of that key is the "name" of that course
course_ids = {}
for value in coursera_data.values():
	for course_info in value:
		course_ids[course_info["id"]] = course_info["name"]

#print out all ids, and names from this new dict.
#Ex: print course_id,course_name
for keys,values in course_ids.iteritems():
	print str(keys) + ": " + values

#filter out all the courses that do not have python in the name and create a new dict of only the python courses.
print "\nCourses about Python: "
python_classes = {}
for keys,values in course_ids.iteritems():
	if values.encode('ascii', 'ignore').lower().find("python") != -1:
		print str(keys) + ": " + values


#write out an html file that has an html table with the list of all ids and course names
with open("json-api-2.html", "w") as html_file:
	html_file.write("<table style=\"width:100%\">")
	html_file.write("\n\t<tr>\n\t\t<th>Course ID</th>")
	html_file.write("\n\t\t<th>Course Name</th>\n\t</tr>")
	for keys,values in course_ids.iteritems():
		html_file.write("\n\t\t<td>%s</td>" % keys)
		html_file.write("\n\t\t<td>%s</td>" % values.encode('ascii', 'ignore'))
		html_file.write("\n\t</tr>")
	html_file.write("\n</table>")

        




