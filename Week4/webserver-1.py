'''

Build out a webserver.


The code below will accept and return basic http requests.

After starting the script below, in the terminal you will see text like this:

GET /favicon.ico HTTP/1.1
Host: localhost:8888
Connection: keep-alive
Accept: */*
....

You can test it out by going to http://localhost:8888/ in your browser.


**** Test your code after each step ****

Phase one: Basic web server

We will extend the code below that when a user goes to http://localhost:8888/ an html file index.html is read from disk and returned to the user.

And when we go to http://localhost:8888/about.html in browser, about.html is read and returned to the user.

Steps:

1) Extend the program by parsing the http request (request) to parse out the http verb from the request. The verb is the first part of the first line. 

EX: 

GET /favicon.ico HTTP/1.1

GET is the HTTP verb.

Lines are seperated by \r\n so we recommend using .split('\r\n')

2) Extend the webserver to be able to get the file for request (The second part of the first line)

3) Create a directory called templates in the same folder

4) In templates, create two new files index.html and about.html

5) Enter some basic html into those two files.

6) Update to that instruction line. Basically after you can figure out what file the browser is asking for /about.html /cat.html /favicon.ico

7) If a request comes in for "/" return templates/index.html file data

8) If a request comes in for "/about.html" return the data in templates/about.html

'''


import socket


HOST, PORT = '', 8888
VIEWS_DIR = "./templates"


def run_server():
    ''' 
    **** You don't need to change the lines below
    **** These lines allow you to accept connections through a web browser.
    **** If you do want to read more you can look at https://docs.python.org/2/howto/sockets.html
    '''
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
 
    print 'Serving HTTP on port %s ...' % PORT
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(4096)
        if not request:
            continue

        #update and add code here.
        uri = request.split('\r\n')[0].split(" ")[1]
        if uri == "/":
            uri = "/index.html"
        elif uri == "/favicon.ico":
            continue

        with open("templates" + uri) as html_file:
            content = html_file.read()
    
        http_response = """\
    HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
    %s
    """ % content

        
        #you should not have to change the lines.
        client_connection.sendall(http_response)
        client_connection.close()


run_server()
