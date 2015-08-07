'''

Phase two: Routing + Controllers

On older websites, the url was just a reference to a file, so the url would be about.html.

On modern what we now call webapps, instead of asking for /about.html which is a reference to a file on disk, we use just /about 

This is because in modern webapps there is usually some code that runs before just returning the html. In our
case we want some python code to run first, maybe to apply some logic or read from the database, before html is returned.

In your browser a user would request <your site.com> + 

/ 
/about
/blog
/blog/1

In this section we are going to extend the work we do in the previous section, by creating a link in code
that for each url we call a python function. That function is then resposible for returning html.

Take code from Webserver1 for the next part of the exercise.

**** Test your code after each step ****

1) Add two new functions index_page() and about_page()

2) Create a hash called urls that maps between a http request like:
 "/" ====> calls index_page(), 
 "/about" =====>calls about_page()

3) Move your file reading code into both of those functions:
	index_page() ====> reads index.html, returns that data.
	about_page() ====>  about.html filereturns that data. 


So now when the webserver asks for the /about the webserver parses or sees that the request is for about. Then using the hash created calls about_page() which returns the html
that is given back to the browser.

'''

import socket


HOST, PORT = '', 8888
VIEWS_DIR = "./templates"

def index_page():
	with open("templates/index.html") as html_file:
		content = html_file.read()

	http_response = """\
	HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
	%s
	""" % content
	return http_response

def about_page():
	with open("templates/about.html") as html_file:
		content = html_file.read()

	http_response = """\
	HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
	%s
	""" % content
	return http_response

def cat_page():
	with open("templates/cat.html") as html_file:
		content = html_file.read()

	http_response = """\
	HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
	%s
	""" % content
	return http_response

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

    urls = {
    	"/" : index_page,
    	"/about" : about_page,
    	"/cat" : cat_page
    }
 
    print 'Serving HTTP on port %s ...' % PORT
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(4096)
        if not request:
            continue

        #update and add code here.
        uri = request.split('\r\n')[0].split(" ")[1]
        if uri == "/favicon.ico":
            continue

        if urls.has_key(uri):
        	http_response = urls[uri]()
        else:
        		http_response = """\
	HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n
	404 Not Found
	"""
        
        #you should not have to change the lines.
        client_connection.sendall(http_response)
        client_connection.close()


run_server()