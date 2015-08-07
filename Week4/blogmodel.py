
'''

Blog Model

Create a class to interface with sqlite3.  This type of object is typically called a "Model".

The table in sqlite3 will have two columns: post_name and post_text

Discuss with your neighbour on how to solve this challenge.

To connect Python to SQL, reference the following:
http://www.pythoncentral.io/introduction-to-sqlite-in-python/

Your model should be able to:

1) Open a sqlite3 db connection
2) Close the connection
3) Create a new table with the correct fields
4) Read by id where id is the primary key of the row
   this will return the blog data associated with that row in a string format
5) Insert a new blogpost - where you can add a new blog post and title

'''

import sqlite3

class BlogModel():
    def __init__(self,db_file,table):
        self.db_file = db_file
        self.db_table = table

        self.post_name = None
        self.post_text = None

        self.open()
        self.create_table(self.db_table)

    def open(self):
        "open sqlite3 db connection"
        self.connection = sqlite3.connect(self.db_file)
        return self.connection

    def close(self):
        "close the connection to sqlite3"
        self.connection.close()

    def create_table(self,table):
        #create the table
        db_cursor = self.connection.cursor()
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS %s(id INTEGER PRIMARY KEY,
                    post_name TEXT, 
                    post_text TEXT);''' % table)
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS pages(id INTEGER PRIMARY KEY,
                    page_name TEXT, 
                    page_text TEXT);''')
        self.connection.commit()

    def insert(self, post_name, post_text):
        #create a new row with data that you pass in
        self.post_name = post_name
        self.post_text = post_text

        db_cursor = self.connection.cursor()
        db_cursor.execute('''INSERT INTO %s(post_name,post_text) VALUES ("%s","%s");''' % (self.db_table,post_name,post_text))
        self.connection.commit()

    def read(self,blog_id):
        # "search for id, and return post_name and post_text as a string"
        db_cursor = self.connection.cursor()
        db_cursor.execute('''SELECT post_name,post_text FROM %s WHERE id=%s;''' % (self.db_table,blog_id))
        return db_cursor.fetchall()

    def read_title(self,blog_title):
        db_cursor = self.connection.cursor()
        db_cursor.execute('''SELECT page_name,page_text FROM pages WHERE page_name="%s";''' % blog_title)
        return db_cursor.fetchall()

    def get_archive(self):
        db_cursor = self.connection.cursor()
        db_cursor.execute('''SELECT page_name,page_text FROM pages;''' % blog_title)
        return db_cursor.fetchall()
