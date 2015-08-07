'''

Open Weather Api is a json weather api to get weather data for most major cities.

In this exercise we are going to populate a small local database with all the min and max temperatures for last 16 days for a city.

We will use a json api to get the data, then store parts of that data in sqlite, which is small sql database.

Steps:

1) First inspect what is returned in json_data. You can use python print statements also download and use the chrome json formatter: https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en 

2) The data returned has a key "list" which is an array of hashes (horray!). Each element in the array is one day's temp info.

3) Write a loop to print out each days "min" and "max" temp as well as the "dt" key. dt is short for datetime.

DB)

4) Create a table to store this information. The table should be able to store

- id sql field type - INTEGER PRIMARY KEY
- city_name  sql field type - text
- datetime (dt) sql field type - text
- min_temp  sql field type - real
- max_temp  sql field type- real

5) Refactor your loop so that instead of just printing it inserts new rows for each day into the table.

6) Write queries to find the day with lowest temperature and the highest.

7) Write a query to find the average temp.

Extension:

Expand the code to be able to ask a user for a city, then populate the db with that cities data. 
Then allow the user to find maxes for one city or across all cities.


Further Reading:

http://zetcode.com/db/sqlitepythontutorial/

--------
Examples using the above functions:

conn = db_open("somefile.db")

db_create(conn)

db_insert(conn)

db_close(conn)


'''

import requests
import time
import sqlite3


def db_open(filename):
    return sqlite3.connect(filename)

def db_create(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather(id INTEGER PRIMARY KEY, 
    	city_name TEXT, 
    	datetime TEXT,
    	min_temp REAL,
    	max_temp REAL); ''')
    conn.commit()

def db_insert(conn,city,date,min_temp,max_temp):
    c = conn.cursor()
    c.execute('''INSERT INTO weather(city_name,datetime,min_temp,max_temp) VALUES ("%s",%i,%.2f,%.2f);''' % (city,date,min_temp,max_temp))
    conn.commit()

def db_close(conn):
    conn.close()

def temp_min(conn,city="%"):
	c = conn.cursor()
	c.execute('''select city_name,MIN(min_temp) from weather where city_name like '%s';''' % city)
	return c.fetchall()

def temp_max(conn,city="%"):
	c = conn.cursor()
	c.execute('''select city_name,MAX(max_temp) from weather where city_name like '%s';''' % city)
	return c.fetchall()

def temp_avg(conn,city="%"):
	c = conn.cursor()
	c.execute('''select ROUND(AVG((min_temp+max_temp)/2),2) from weather where city_name like '%s';''' % city)
	return c.fetchall()

city = raw_input("What city would you like to get weather for?: ").lower()

url = "http://api.openweathermap.org/data/2.5/forecast/daily?mode=json&units=imperial&q=%s&cnt=16" % city

json_data = requests.get(url).json()

if json_data["cod"] == "404":
	print "ERROR: City does not exist."
	quit()

conn = db_open(("weather_data.db"))
db_create(conn)

for each in json_data["list"]:
	#print time.strftime('%Y-%m-%d', time.localtime(each["dt"]))
	date = each["dt"]
	min_temp = each["temp"]["min"]
	max_temp = each["temp"]["max"]
	db_insert(conn,city,date,min_temp,max_temp)

print temp_min(conn)
print temp_max(conn)
print temp_avg(conn)

db_close(conn)


