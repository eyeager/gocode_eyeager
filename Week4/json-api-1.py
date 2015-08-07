'''
Build out the program below to ask the user for their zipcode, and then display the city and state for that zipcode.

This is an example of an HTTP GET request - you are sending a request via your browser to the server, which responds with a bunch of json data.

Example:

http://api.zippopotam.us/us/78704

'''

import requests

zipcode = raw_input("What is your zipcode?: ")

url = "http://api.zippopotam.us/us/" + zipcode

json_data = requests.get(url).json()

print "City: " + json_data["places"][0]["place name"]
print "State: " + json_data["places"][0]["state"]
